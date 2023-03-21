from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from pyqt_loading_progressbar import LoadingProgressBar


type_dict={
    0:"良性",
    1:"恶性"
}

def get_type_name(type):
    type_name = "良性"
    if type == 1:
        type_name = "恶性"
    return type_name


