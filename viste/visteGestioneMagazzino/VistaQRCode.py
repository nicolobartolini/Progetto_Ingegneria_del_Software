from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class VistaQRCode(QWidget):

    def __init__(self, parent=None):
        super(VistaQRCode, self).__init__(parent)
        self.g_layout = QGridLayout()
        self.label = QLabel(self)
        self.pixmap = QPixmap('qr.png')
        self.label.setPixmap(self.pixmap)
        self.g_layout.addWidget(self.label)
        self.setLayout(self.g_layout)
        self.setFixedSize(310, 290)
        self.setWindowTitle("QR Code ubicazione")

    def check_login(self):
        pass