import sys
import torch
import os
import numpy as np
# import matplotlib as mpl
# mpl.use('TkAgg')
# import matplotlib.pyplot as plt
import SimpleITK as sitk
import math
from skimage import measure
from scipy.ndimage import zoom
from scipy.spatial.distance import cdist
import pandas as pd

try:
    # Python2
    from StringIO import StringIO
except ImportError:
    # Python3
    from io import StringIO


class Logger(object):
    def __init__(self, logfile):
        self.terminal = sys.stdout
        self.log = open(logfile, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


def worldToVoxelCoord(worldCoord, origin, spacing):
    stretchedVoxelCoord = np.absolute(worldCoord - origin)
    voxelCoord = stretchedVoxelCoord / spacing
    return voxelCoord


def voxelToWorldCoord(voxelCoord, origin, spacing):
    worldCoord = voxelCoord * spacing
    worldCoord += origin
    return worldCoord



def py_nms(dets, thresh):
    # Check the input dtype
    if isinstance(dets, torch.Tensor):
        if dets.is_cuda:
            dets = dets.cpu()
        dets = dets.data.numpy()

    z = dets[:, 1]
    y = dets[:, 2]
    x = dets[:, 3]
    d = dets[:, 4]
    h = dets[:, 5]
    w = dets[:, 6]
    scores = dets[:, 0]

    areas = d * h * w
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx0 = np.maximum(x[i] - w[i] / 2., x[order[1:]] - w[order[1:]] / 2.)
        yy0 = np.maximum(y[i] - h[i] / 2., y[order[1:]] - h[order[1:]] / 2.)
        zz0 = np.maximum(z[i] - d[i] / 2., z[order[1:]] - d[order[1:]] / 2.)
        xx1 = np.minimum(x[i] + w[i] / 2., x[order[1:]] + w[order[1:]] / 2.)
        yy1 = np.minimum(y[i] + h[i] / 2., y[order[1:]] + h[order[1:]] / 2.)
        zz1 = np.minimum(z[i] + d[i] / 2., z[order[1:]] + d[order[1:]] / 2.)

        inter_w = np.maximum(0.0, xx1 - xx0)
        inter_h = np.maximum(0.0, yy1 - yy0)
        inter_d = np.maximum(0.0, zz1 - zz0)
        intersect = inter_w * inter_h * inter_d
        overlap = intersect / (areas[i] + areas[order[1:]] - intersect)

        inds = np.where(overlap <= thresh)[0]
        order = order[inds + 1]

    return torch.from_numpy(dets[keep]), torch.LongTensor(keep)


def py_box_overlap(boxes1, boxes2):
    overlap = np.zeros((len(boxes1), len(boxes2)))

    z1, y1, x1 = boxes1[:, 0], boxes1[:, 1], boxes1[:, 2]
    d1, h1, w1 = boxes1[:, 3], boxes1[:, 4], boxes1[:, 5]
    areas1 = d1 * h1 * w1

    z2, y2, x2 = boxes2[:, 0], boxes2[:, 1], boxes2[:, 2]
    d2, h2, w2 = boxes2[:, 3], boxes2[:, 4], boxes2[:, 5]
    areas2 = d2 * h2 * w2

    for i in range(len(boxes1)):
        xx0 = np.maximum(x1[i] - w1[i] / 2., x2 - w2 / 2.)
        yy0 = np.maximum(y1[i] - h1[i] / 2., y2 - h2 / 2.)
        zz0 = np.maximum(z1[i] - d1[i] / 2., z2 - d2 / 2.)
        xx1 = np.minimum(x1[i] + w1[i] / 2., x2 + w2 / 2.)
        yy1 = np.minimum(y1[i] + h1[i] / 2., y2 + h2 / 2.)
        zz1 = np.minimum(z1[i] + d1[i] / 2., z2 + d2 / 2.)

        inter_w = np.maximum(0.0, xx1 - xx0)
        inter_h = np.maximum(0.0, yy1 - yy0)
        inter_d = np.maximum(0.0, zz1 - zz0)
        intersect = inter_w * inter_h * inter_d
        overlap[i] = intersect / (areas1[i] + areas2 - intersect)

    return overlap


def center_box_to_coord_box(bboxes):
    """
    Convert bounding box using center of rectangle and side lengths representation to
    bounding box using coordinate representation
    [center_z, center_y, center_x, D, H, W] -> [z_start, y_start, x_start, z_end, y_end, x_end]

    bboxes: list of bounding boxes, [num_bbox, 6]
    """
    res = np.zeros(bboxes.shape)
    res[:, 0] = bboxes[:, 0] - bboxes[:, 3] / 2.
    res[:, 1] = bboxes[:, 1] - bboxes[:, 4] / 2.
    res[:, 2] = bboxes[:, 2] - bboxes[:, 5] / 2.
    res[:, 3] = bboxes[:, 0] + bboxes[:, 3] / 2.
    res[:, 4] = bboxes[:, 1] + bboxes[:, 4] / 2.
    res[:, 5] = bboxes[:, 2] + bboxes[:, 5] / 2.

    return res


def coord_box_to_center_box(bboxes):
    """
    Convert bounding box using coordinate representation to
    bounding box using center of rectangle and side lengths representation
    [z_start, y_start, x_start, z_end, y_end, x_end] -> [center_z, center_y, center_x, D, H, W]

    bboxes: list of bounding boxes, [num_bbox, 6]
    """
    res = np.zeros(bboxes.shape)

    res[:, 3] = bboxes[:, 3] - bboxes[:, 0]
    res[:, 4] = bboxes[:, 4] - bboxes[:, 1]
    res[:, 5] = bboxes[:, 5] - bboxes[:, 2]
    res[:, 0] = bboxes[:, 0] + res[:, 3] / 2.
    res[:, 1] = bboxes[:, 1] + res[:, 4] / 2.
    res[:, 2] = bboxes[:, 2] + res[:, 5] / 2.

    return res


def ext2factor(bboxes, factor=8):
    """
    Given center box representation which is [z_start, y_start, x_start, z_end, y_end, x_end],
    return closest point which can be divided by 8
    """
    bboxes[:, :3] = bboxes[:, :3] // factor * factor
    bboxes[:, 3:] = bboxes[:, 3:] // factor * factor + (bboxes[:, 3:] % factor != 0).astype(np.int32) * factor

    return bboxes


def clip_boxes(boxes, img_size):
    '''
    clip boxes outside the image, all box follows [z_start, y_start, x_start, z_end, y_end, x_end]
    '''
    depth, height, width = img_size
    boxes[:, 0] = np.clip(boxes[:, 0], 0, depth)
    boxes[:, 1] = np.clip(boxes[:, 1], 0, height)
    boxes[:, 2] = np.clip(boxes[:, 2], 0, width)
    boxes[:, 3] = np.clip(boxes[:, 3], 0, depth)
    boxes[:, 4] = np.clip(boxes[:, 4], 0, height)
    boxes[:, 5] = np.clip(boxes[:, 5], 0, width)

    return boxes












def HU2uint8(image, HU_min=-1200.0, HU_max=600.0, HU_nan=-2000.0):
    """
    Convert HU unit into uint8 values. First bound HU values by predfined min
    and max, and then normalize
    image: 3D numpy array of raw HU values from CT series in [z, y, x] order.
    HU_min: float, min HU value.
    HU_max: float, max HU value.
    HU_nan: float, value for nan in the raw CT image.
    """
    image_new = np.array(image)
    image_new[np.isnan(image_new)] = HU_nan

    # normalize to [0, 1]
    image_new = (image_new - HU_min) / (HU_max - HU_min)
    image_new = np.clip(image_new, 0, 1)
    image_new = (image_new * 255).astype('uint8')

    return image_new


def pad2factor(image, factor=16, pad_value=0):
    depth, height, width = image.shape
    d = int(math.ceil(depth / float(factor))) * factor
    h = int(math.ceil(height / float(factor))) * factor
    w = int(math.ceil(width / float(factor))) * factor

    pad = [[0, d - depth], [0, h - height], [0, w - width]]

    image = np.pad(image, pad, 'constant', constant_values=pad_value)

    return image





def normalize(img):
    maximum = img.max()
    minimum = img.min()

    # 0 ~ 1
    img = (img - minimum) / max(1, (maximum - minimum))

    # -1 ~ 1
    img = img * 2 - 1
    return img




def onehot2multi_mask(onehot):
    num_class, D, H, W = onehot.shape
    multi_mask = np.zeros((D, H, W))

    for i in range(1, num_class):
        multi_mask[onehot[i] > 0] = i

    return multi_mask


def load_dicom_image(foldername):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(foldername)
    reader.SetFileNames(dicom_names)
    itkimage = reader.Execute()
    numpyImage = sitk.GetArrayFromImage(itkimage)

    numpyOrigin = np.array(list(reversed(itkimage.GetOrigin())))
    numpySpacing = np.array(list(reversed(itkimage.GetSpacing())))

    return numpyImage, numpyOrigin, numpySpacing


def truncate_HU_uint8(img):
    """Truncate HU range and convert to uint8."""

    HU_range = np.array([-1200., 600.])
    new_img = (img - HU_range[0]) / (HU_range[1] - HU_range[0])
    new_img[new_img < 0] = 0
    new_img[new_img > 1] = 1
    new_img = (new_img * 255).astype('uint8')
    return new_img
