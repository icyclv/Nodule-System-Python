import numpy as np
import torch

from net.lungmask.mask import apply


def clean_model(model):
    clear_list=["ensemble_proposals",
                       "crop_boxes",
                       "detections",
                       "keeps",
                       "mask_probs",
                       "rcnn_deltas",
                       "rcnn_logits",
                       "rpn_deltas_flat",
                       "rpn_logits_flat",
                       "rpn_proposals",
                       "rpn_window"]
    for name in clear_list:
        if hasattr(model,name):
            #获取属性并将其设置为空列表
            setattr(model,name,[])

    torch.cuda.empty_cache()


@torch.no_grad()
def nodule_net_interface(model, img, device, detections=None):
    '''
    :param model: NoduleNet model
    :param img: input image,tensor
    :param detections: detection results,if None,then use NoduleNet to detect,numpy
    '''
    if isinstance(img, np.ndarray):
        img = torch.from_numpy(img).float()
    if len(img.shape) == 4:
        img = img.unsqueeze(0)
    img = img.to(device)
    if detections is None:
        model.forward(img, None, None, None, None)
        detections = model.detections.cpu().numpy()
    else:
        model.forward_mask(img, detections)
    mask_probs = [t.cpu().numpy() for t in model.mask_probs]
    # 防止发生广播错误,用大数组填充
    mask_probs.insert(0, np.zeros((120, 120, 120), dtype=np.float32))
    mask_probs = np.array(mask_probs, dtype=np.object)
    mask_probs = mask_probs[1:]
    crop_boxes = model.crop_boxes

    clean_model(model)
    return detections, mask_probs, crop_boxes


@torch.no_grad()
def sanet_interface(model, img, device):
    '''
    :param model: SANet model
    :param img: input image,tensor
    '''
    if isinstance(img, np.ndarray):
        img = torch.from_numpy(img).float()
    if len(img.shape) == 4:
        img = img.unsqueeze(0)
    elif len(img.shape) == 3:
        img = img.unsqueeze(0).unsqueeze(0)
    img = img.to(device)
    model.forward(img, None, None, None, None)
    detections = model.detections.cpu().numpy()
    clean_model(model)
    return detections


@torch.no_grad()
def nasnet_interface(model, img, device):
    '''
    :param model: SANet model
    :param img: input image,tensor
    '''
    if isinstance(img, np.ndarray):
        img = torch.from_numpy(img).float()
    if len(img.shape) == 4:
        img = img.unsqueeze(0)
    img = img.to(device)
    nodule_type = model(img)
    nodule_type = nodule_type.cpu().numpy()[0]
    return nodule_type


@torch.no_grad()
def lungmask_interface(model, img, device, batch_size=20):
    '''
    :param model: SANet model
    :param img: input image,tensor
    '''

    if device.type == "cpu":
        batch_size = 1
    nodule_type = apply(img, model, device, batch_size=batch_size)
    return nodule_type
