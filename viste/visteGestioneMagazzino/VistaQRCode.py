from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from gestione.GestoreMagazzino import GestoreMagazzino


class VistaQRCode(QWidget):

    def __init__(self, parent=None, id=1):
        super(VistaQRCode, self).__init__(parent)
        self.g_layout = QGridLayout()
        self.label = QLabel(self)
        GestoreMagazzino.get_QR_prodotto(id).save('qr.png')
        self.pixmap = QPixmap('qr.png')
        self.label.setPixmap(self.pixmap)
        self.g_layout.addWidget(self.label)
        self.setLayout(self.g_layout)
        self.setFixedSize(380, 350)
        self.setWindowTitle("QR Code ubicazione")