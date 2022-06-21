from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QComboBox

from viste.visteGestioneMagazzino.VistaInformazioniProdotto import VistaInformazioniProdotto
from viste.visteGestioneMagazzino.VistaInserisciProdotto import VistaInserisciProdotto


class VistaGestioneMagazzino(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneMagazzino, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label = QLabel('Ricerca:')
        self.barra_ricerca = QLineEdit()
        self.button_cerca = QPushButton('Cerca')
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.h_layout_2 = QHBoxLayout()
        self.label_scelta_ordinamento = QLabel('Ordinamento')
        self.scelta_ordinamento_cbox = QComboBox()
        self.scelta_ordinamento_cbox.addItem('Nome')
        self.button_cambia_ordinamento = QPushButton('OK')
        self.h_layout_2.addWidget(self.label_scelta_ordinamento)
        self.h_layout_2.addWidget(self.scelta_ordinamento_cbox)
        self.h_layout_2.addWidget(self.button_cambia_ordinamento)  # DA RIVEDERE DISPOSIZIONE
        self.lista_prodotti = QListWidget()
        self.lista_prodotti.addItem('prova')
        self.lista_prodotti.addItem('prova2')
        self.lista_prodotti.itemActivated.connect(self.prova)
        self.button_inserisci_prodotto = QPushButton('Inserisci prodotto...')
        self.button_inserisci_prodotto.clicked.connect(self.open_inserisci_prodotto)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.h_layout_2)
        self.v_layout.addWidget(self.lista_prodotti)
        self.v_layout.addWidget(self.button_inserisci_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Magazzino")
        self.setMinimumSize(700, 900)


    def open_inserisci_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto()
        self.vista_inserisci_prodotto.show()

    def prova(self, item):
        self.vista_informazioni_prodotto = VistaInformazioniProdotto()
        self.vista_informazioni_prodotto.show()
