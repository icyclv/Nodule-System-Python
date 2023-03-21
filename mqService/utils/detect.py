import io
import time

import SimpleITK as sitk
import numpy as np
import scipy
import math
import torch
import os
import lungmask.mask

from net.ModelConstant import DEVICE
from utils.LIDC.preprocess import resample, get_lung_box, apply_mask
from utils.util import HU2uint8, pad2factor



def classfication_prepross(img,detection,crop_size=32):
    crdz, crdy, crdx = int(detection[2]), int(detection[3]), int(detection[4])
    bgx = int(max(0, crdx - crop_size / 2))
    bgy = int(max(0, crdy - crop_size / 2))
    bgz = int(max(0, crdz - crop_size / 2))
    cropdata = np.ones((crop_size, crop_size, crop_size)) * 170
    cropdatatmp = np.array(img[bgz:bgz + crop_size, bgy:bgy + crop_size, bgx:bgx + crop_size])
    cropdata[
    int(crop_size / 2 - cropdatatmp.shape[0] / 2):int(
        crop_size / 2 - cropdatatmp.shape[0] / 2 + cropdatatmp.shape[0]), \
    int(crop_size / 2 - cropdatatmp.shape[1] / 2):int(
        crop_size / 2 - cropdatatmp.shape[1] / 2 + cropdatatmp.shape[1]), \
    int(crop_size / 2 - cropdatatmp.shape[2] / 2):int(
        crop_size / 2 - cropdatatmp.shape[2] / 2 + cropdatatmp.shape[2])] = np.array(2 - cropdatatmp)
    pix_mean = 179.29
    pix_std = 49.76
    cropdata = (cropdata - pix_mean) / pix_std
    cropdata = np.reshape(cropdata, (1, 1, crop_size, crop_size, crop_size))
    return cropdata

def detect(img,spacing, seg_model, detect_model, classification_model, lung_model,scan_id, threshold=0.8):
    # resize成1*1*1mm
    original_image, resampled_spacing = resample(img, spacing, order=3)



    # 肺部分割
    segmentation = lung_model["interface_method"](lung_model["model"], original_image, DEVICE)
    binary_mask1, binary_mask2 = segmentation == 1, segmentation == 2
    original_image = HU2uint8(original_image)
    img = original_image
    original_image = apply_mask(original_image, binary_mask1, binary_mask2)


    # 3D重建数据
    reconstruction = original_image
    reconstruction[segmentation==0]=0


    # 检测
    original_image = pad2factor(original_image,factor=32, pad_value=0)
    original_image = np.expand_dims(original_image, 0)
    original_image = (original_image.astype(np.float32) - 128.) / 128.
    original_image = torch.from_numpy(original_image).float()

    if detect_model is not None:
        detections = detect_model["interface_method"](detect_model["model"], original_image, DEVICE)
    else:
        detections = None
    detections, mask_probs, crop_boxes = seg_model["interface_method"](seg_model["model"], original_image, DEVICE, detections)

    # 阈值过滤
    wanted = []
    for i, detection in enumerate(detections, start=0):
        if detection[1] > threshold:
            wanted.append(i)
    crop_boxes = crop_boxes[wanted]
    mask_probs = mask_probs[wanted]
    detections = detections[wanted]

    # 距离保留标准
    diameter_coef = 0.5
    result = []
    for d, b, p in zip(detections, crop_boxes, mask_probs):
        # d[1] is prob, d[2,3,4] is x,y,z, d[5] is diameter

        diameter = np.mean(d[5:8]) * diameter_coef

        cropdata=classfication_prepross(img,d)

        cropdata = torch.from_numpy(cropdata).float()

        p =  classification_model["interface_method"](classification_model["model"], cropdata, DEVICE)

        type = 0 if p < 0.5 else 1



        result.append({
            "scanId": scan_id,
            "coordinate": '{},{},{}'.format(int(d[2]), int(d[3]),int(d[4])),
            "diameter" :  float(round(diameter,2)),
            "confidence": float(round(d[1], 2)),
            "type" : type,
            "classificationProbability": float(round(p, 2))
        })


    buf = io.BytesIO()  # create our buffer
    # pass the buffer as you would an open file object
    np.savez_compressed(buf, ct=img,reconstruction = reconstruction, detections=detections, crop_boxes=crop_boxes, mask_probs=mask_probs)
    buf.seek(0)

    return result,buf
