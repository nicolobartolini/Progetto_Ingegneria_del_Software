from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QComboBox

from viste.visteGestioneClienti.VistaInserisciClienteAzienda import VistaInserisciClienteAzienda
from viste.visteGestioneClienti.VistaInserisciClientePersona import VistaInserisciClientePersona


class VistaGestioneClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneClienti, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label = QLabel('Ricerca:')
        self.barra_ricerca = QLineEdit()
        self.cbox_tipo_ricerca = QComboBox()
        self.cbox_tipo_ricerca.addItem('Ricerca per nome')
        self.cbox_tipo_ricerca.addItem('Ricerca per codice fiscale')
        self.button_cerca = QPushButton('Cerca')
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.lista_clienti = QListWidget()
        self.lista_clienti.addItem('prova')
        self.lista_clienti.addItem('prova2')
        self.lista_clienti.itemActivated.connect(self.open_informazioni_cliente)
        self.button_inserisci_cliente_persona = QPushButton('Inserisci cliente (persona)...')
        self.button_inserisci_cliente_persona.clicked.connect(self.open_inserisci_cliente_persona)
        self.button_inserisci_cliente_azienda = QPushButton('Inserisci cliente (azienda)...')
        self.button_inserisci_cliente_azienda.clicked.connect(self.open_inserisci_cliente_azienda)
        self.h_layout_bottom = QHBoxLayout()
        self.h_layout_bottom.addWidget(self.button_inserisci_cliente_persona)
        self.h_layout_bottom.addWidget(self.button_inserisci_cliente_azienda)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.lista_clienti)
        self.v_layout.addLayout(self.h_layout_bottom)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Clienti")
        self.setMinimumSize(700, 900)


    def open_inserisci_cliente_persona(self):
        self.vista_inserisci_cliente_persona = VistaInserisciClientePersona()
        self.vista_inserisci_cliente_persona.show()

    def open_inserisci_cliente_azienda(self):
        self.vista_inserisci_cliente_azienda = VistaInserisciClienteAzienda()
        self.vista_inserisci_cliente_azienda.show()

    def open_informazioni_cliente(self, item):
        self.vista_informazioni_cliente = VistaInformazioniCliente()
        self.vista_informazioni_cliente.show()
