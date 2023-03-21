from functools import partial

import torch

from net.InterfaceMethod import nodule_net_interface, sanet_interface, nasnet_interface, lungmask_interface
from net.lungmask.mask import get_model
from net.nas_net.cnn_res import CombineModel
from net.nodulenet.config import config as nodulenet_cfg
from net.nodulenet.nodule_net import NoduleNet

from net.sanet.config import net_config as sanet_cfg
from net.sanet.sanet import SANet


def nodule_net_load(Model, path, config=None):
    if config is None:
        model = Model().to(DEVICE)
    else:
        model = Model(config).to(DEVICE)
    model.load_state_dict(torch.load(path, map_location='cpu'))
    if hasattr(model, 'set_mode'):
        model.set_mode('eval')
    model.eval()
    if hasattr(model, 'use_mask'):
        model.use_mask = True
    if hasattr(model, 'use_rcnn'):
        model.use_rcnn = True

    return model


def lungmask_load(path):
    model = get_model('unet', 'R231', path)
    model = model.to(DEVICE)
    return model


device_type = "cuda"

DEVICE = torch.device(device_type if torch.cuda.is_available() else "cpu") if device_type == "cuda" else torch.device(
    "cpu")

segment_models = {
    "nodulenet": {
        "model": partial(nodule_net_load, Model=NoduleNet, path="model/nodulenet.pth", config=nodulenet_cfg),
        "interface_method": nodule_net_interface
    }

}

detect_models = {
    "sanet": {
        "model": partial(nodule_net_load, Model=SANet, path="model/sanet.pth", config=sanet_cfg),
        "interface_method": sanet_interface
    }
}

classification_models = {
    "nasnet": {
        "model": partial(nodule_net_load, Model=CombineModel, path="model/nasnet.pth", config=None),
        "interface_method": nasnet_interface,
    }
}

lung_segment_models = {
    "lungmask": {
        "model": partial(lungmask_load, path="model/unet_r231-d5d2fc3d.pth"),
        "interface_method": lungmask_interface
    }
}


def load_model(seg_model, detect_model, classification_model, lung_model):
    """
    加载模型,返回分割模型，检测模型，分类模型，肺部分割模型
    """
    # 分割模型
    seg_model = {"model": segment_models["nodulenet"]["model"](),
                 "interface_method": segment_models["nodulenet"]["interface_method"]}

    # 检测模型，性能一般，直接用NoduleNet的检测结果
    detect_model = None
    # detect_model=detect_models["sanet"]["model"]()

    # 分类模型
    classification_model = {"model": classification_models["nasnet"]["model"](),
                            "interface_method": classification_models["nasnet"]["interface_method"]}

    # 肺部分割模型
    lung_model = {"model": lung_segment_models["lungmask"]["model"](),
                  "interface_method": lung_segment_models["lungmask"]["interface_method"]}

    return seg_model, detect_model, classification_model, lung_model
