from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton


class VistaEliminaBase(QWidget):

    def __init__(self, parent=None):
        super(VistaEliminaBase, self).__init__(parent)
        print('OK')
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Sei sicuro di voler eliminare la base?')
        self.h_layout = QHBoxLayout()
        self.button_si = QPushButton('Sì')
        self.button_si.clicked.connect(self.elimina_base)
        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.close)
        self.h_layout.addWidget(self.button_si)
        self.h_layout.addWidget(self.button_no)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Elimina base")
        self.setFixedSize(250, 70)

    def elimina_base(self):
        pass