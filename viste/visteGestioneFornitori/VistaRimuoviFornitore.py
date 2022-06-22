from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreFornitori import GestoreFornitori
from gestione.GestoreImpiegati import GestoreImpiegati


class VistaRimuoviFornitore(QWidget):

    def __init__(self, parent=None, marchionimo=None):
        super(VistaRimuoviFornitore, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel(f"Sei sicuro di voler eliminare il fornitore {marchionimo} dal sistema?")
        self.h_layout = QHBoxLayout()
        self.button_si = QPushButton('Sì')
        self.button_si.clicked.connect(lambda: self.elimina_fornitore(marchionimo))
        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.close)
        self.h_layout.addWidget(self.button_si)
        self.h_layout.addWidget(self.button_no)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Elimina fornitore")
        self.setFixedSize(350, 70)

    def elimina_fornitore(self, marchionimo: str):
        GestoreFornitori.rimuovi_fornitore(marchionimo)
        self.close()
