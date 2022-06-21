from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QProgressBar, QFormLayout

from viste.visteGestioneColorificio.VistaInformazioniBase import VistaInformazioniBase
from viste.visteGestioneColorificio.VistaInserisciBase import VistaInserisciBase


class VistaScorteColorificio(QWidget):

    def __init__(self, parent=None):
        super(VistaScorteColorificio, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label = QLabel('Ricerca:')
        self.barra_ricerca = QLineEdit()
        self.button_cerca = QPushButton('Cerca')
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.lista_basi = QListWidget()
        self.lista_basi.addItem('prova')
        self.lista_basi.addItem('prova2')
        self.lista_basi.itemActivated.connect(self.open_informazioni_base)
        self.button_inserisci_base = QPushButton('Inserisci base...')
        self.button_inserisci_base.clicked.connect(self.open_inserisci_base)
        self.f_layout = QFormLayout()
        self.quantita_rosso = QProgressBar()
        self.quantita_blu = QProgressBar()
        self.quantita_giallo = QProgressBar()
        self.quantita_rosso.setValue(50)
        self.quantita_rosso.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #DC143C;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.quantita_blu.setValue(71)
        self.quantita_blu.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #1E90FF;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.quantita_giallo.setValue(41)
        self.quantita_giallo.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #FFD700;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.f_layout.addRow('Quantità rosso:', self.quantita_rosso)
        self.f_layout.addRow('Quantità blu:', self.quantita_blu)
        self.f_layout.addRow('Quantità giallo:', self.quantita_giallo)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.lista_basi)
        self.v_layout.addWidget(self.button_inserisci_base)
        self.v_layout.addLayout(self.f_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Scorte Colorificio")
        self.setMinimumSize(700, 900)

    def open_inserisci_base(self):
        self.vista_inserisci_base = VistaInserisciBase()
        self.vista_inserisci_base.show()

    def open_informazioni_base(self, item):
        self.vista_informazioni_base = VistaInformazioniBase()
        self.vista_informazioni_base.show()
