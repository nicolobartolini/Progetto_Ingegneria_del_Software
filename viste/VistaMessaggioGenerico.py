from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton


class VistaMessaggioGenerico(QWidget):

    def __init__(self, parent=None, msg='Operazione completata.'):
        super(VistaMessaggioGenerico, self).__init__(parent)
        print('OK')
        self.v_layout = QVBoxLayout()
        self.label = QLabel(msg)
        self.button_ok = QPushButton('OK')
        self.button_ok.clicked.connect(self.close)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button_ok)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Messaggio")
        self.setFixedSize(250, 70)
