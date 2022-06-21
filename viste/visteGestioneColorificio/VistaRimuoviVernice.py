from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from gestione.GestoreColorificio import GestoreColorificio


class VistaRimuoviVernice(QWidget):

    def __init__(self, parent=None, id=1):
        super(VistaRimuoviVernice, self).__init__(parent)
        print('OK')
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Sei sicuro di voler eliminare la vernice?')
        self.h_layout = QHBoxLayout()
        self.button_si = QPushButton('Sì')
        self.button_si.clicked.connect(lambda: self.rimuovi_vernice(id))
        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.close)
        self.h_layout.addWidget(self.button_si)
        self.h_layout.addWidget(self.button_no)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Rimuovi vernice")
        self.setFixedSize(250, 70)

    def rimuovi_vernice(self, id: int):
        GestoreColorificio.rimuovi_vernice(id)
        self.close()