from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from gestione.GestoreImpiegati import GestoreImpiegati


class VistaRimuoviImpiegato(QWidget):

    def __init__(self, parent=None, nome_utente=None):
        super(VistaRimuoviImpiegato, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel(f"Sei sicuro di voler eliminare l'impiegato {nome_utente} dal sistema?")
        self.h_layout = QHBoxLayout()
        self.button_si = QPushButton('Sì')
        self.button_si.clicked.connect(lambda: self.elimina_impiegato(nome_utente))
        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.close)
        self.h_layout.addWidget(self.button_si)
        self.h_layout.addWidget(self.button_no)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Elimina impiegato")
        self.setFixedSize(350, 70)

    def elimina_impiegato(self, nome_utente: str):
        GestoreImpiegati.elimina_impiegato(nome_utente)
        self.close()
