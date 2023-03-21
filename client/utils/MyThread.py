import io
import time

import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from requests import Response

from utils.SingletionUtils import Session
import SimpleITK as sitk

class WorkThread(QThread):  # 定义一个工作线程，后面会调用和重写
    # 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(int)

    def run(self):  # 线程启动后会自动执行,这里是逻辑实现的代码
        self.finishSignal.emit(int)  # 发射信号


class TestThread(WorkThread):
    finishSignal = pyqtSignal(Response)

    def __init__(self):
        super(TestThread, self).__init__()


    def run(self):
        try:
            res = Response()
            res.status_code = 500
            time.sleep(3)
            self.finishSignal.emit(res)
        except Exception as e:
            print(e)
            res =Response()
            res.status_code = 500
            self.finishSignal.emit(res)




class RequestThread(WorkThread):
    finishSignal = pyqtSignal(Response)

    def __init__(self,type,url, data=None, headers=None,files=None,json=None):
        super(RequestThread, self).__init__()
        self.url = url
        self.type = type
        self.data = data
        self.headers = headers
        self.files = files
        self.json = json

    def run(self):
        try:


            self.result = Session.request(self.type, self.url, data=self.data, headers=self.headers, files=self.files, json=self.json)
            self.finishSignal.emit(self.result)
        except Exception as e:
            print(e)
            res =Response()
            res.status_code = 0
            self.finishSignal.emit(res)


class LoadDicomThread(WorkThread):
    finishSignal = pyqtSignal(bool,bytes)

    def __init__(self,file_path):
        super(LoadDicomThread, self).__init__()
        self.file_path = file_path

    def run(self):
        try:
            reader = sitk.ImageSeriesReader()
            dcm_series = reader.GetGDCMSeriesFileNames(self.file_path)
            reader.SetFileNames(dcm_series)
            itkimage = reader.Execute()
            spacing = np.array(list(reversed(itkimage.GetSpacing())))
            itkimage = sitk.GetArrayFromImage(itkimage)
            itkimage = itkimage.astype(np.int16) #压缩一下，int32太大了
            buf = io.BytesIO()
            np.savez_compressed(buf, img=itkimage, spacing=spacing)  # 压缩传输
            buf.seek(0)
            buf = buf.getvalue()
            self.finishSignal.emit(True,buf)
        except Exception as e:

            self.finishSignal.emit(False,bytes(0))



class CompressFileThread(WorkThread):
    finishSignal = pyqtSignal(bool,bytes)

    def __init__(self,ct,reconstruction,crop_boxes,mask_probs):
        super(CompressFileThread, self).__init__()
        self.ct = ct
        self.reconstruction = reconstruction
        self.crop_boxes = crop_boxes
        self.mask_probs = mask_probs

    def run(self):
        try:
            buf = io.BytesIO()  # create our buffer
            # pass the buffer as you would an open file object
            np.savez_compressed(buf, ct=self.ct, reconstruction=self.reconstruction,
                                crop_boxes=self.crop_boxes, mask_probs=self.mask_probs)
            buf.seek(0)
            buf = buf.getvalue()
            self.finishSignal.emit(True,buf)

        except Exception as e:

            self.finishSignal.emit(False,None)








