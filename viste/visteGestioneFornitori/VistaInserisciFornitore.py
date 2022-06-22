from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton

from Fornitore import Fornitore
from gestione.GestoreFornitori import GestoreFornitori
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaInserisciFornitore(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciFornitore, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel("Inserisci i dati del fornitore che vuoi inserire:")
        self.f_layout = QFormLayout()
        self.input_marchionimo = QLineEdit()
        self.input_partitaIVA = QLineEdit()
        self.f_layout.addRow('Marchionimo:', self.input_marchionimo)
        self.f_layout.addRow('PartitaIVA:', self.input_partitaIVA)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(self.inserisci_fornitore)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento fornitore")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def inserisci_fornitore(self):
        marchionimo = self.input_marchionimo.text()
        partitaIVA = int(self.input_partitaIVA.text())
        nuovo_fornitore = Fornitore(marchionimo, partitaIVA)
        GestoreFornitori.aggiungi_fornitore(nuovo_fornitore)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Fornitore inserito con successo')
        self.messaggio_conferma.show()
        self.close()
