from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from pyqt_loading_progressbar import LoadingProgressBar


class LoadingDialog(QDialog):
    def __init__(self,parent=None,label='Loading...'):
        super(LoadingDialog, self).__init__(parent)
        bar = LoadingProgressBar()
        self.label = QLabel(label)
        lay = QVBoxLayout()
        lay.addWidget(self.label)
        lay.addWidget(bar)

        self.setLayout(lay)
        self.setWindowFlags(Qt.Dialog  )


