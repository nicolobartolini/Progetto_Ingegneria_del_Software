from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QComboBox

from gestione.GestoreClienti import GestoreClienti
from viste.visteGestioneClienti.VistaInformazioniCliente import VistaInformazioniCliente
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
        self.cbox_tipo_ricerca.addItem('Ricerca per cognome/marchionimo')
        self.cbox_tipo_ricerca.addItem('Ricerca per codice fiscale/partitaIVA')
        self.button_cerca = QPushButton('Cerca/Aggiorna')
        self.button_cerca.clicked.connect(self.ricerca_lista_clienti)
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.cbox_tipo_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.lista_clienti = QListWidget()
        GestoreClienti.aggiorna_database_gestore_clienti()
        self.set_lista_clienti(GestoreClienti.database_clienti)
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
        cliente_dict = {}
        id_cliente = int(item.text().split(' ')[0])
        for cliente in GestoreClienti.database_clienti:
            if cliente['_id'] == id_cliente:
                cliente_dict = cliente
                break
        self.vista_informazioni_cliente = VistaInformazioniCliente(cliente=cliente_dict)
        self.vista_informazioni_cliente.show()

    def set_lista_clienti(self, lista_clienti):
        self.lista_clienti.clear()
        if len(lista_clienti) != 0:
            for cliente in lista_clienti:
                if cliente['tipo'] == 'persona':
                    self.lista_clienti.addItem(
                        f'{cliente["_id"]} | {cliente["nome"].capitalize()} {cliente["cognome"].capitalize()}')
                elif cliente['tipo'] == 'azienda':
                    self.lista_clienti.addItem(
                        f'{cliente["_id"]} | {cliente["marchionimo"]}')

    def ricerca_lista_clienti(self):
        parametro = self.barra_ricerca.text()
        lista_clienti = []
        if self.cbox_tipo_ricerca.currentText() == 'Ricerca per cognome/marchionimo':
            lista_clienti = GestoreClienti.ricerca_ordina_clienti('cognome', parametro)
        elif self.cbox_tipo_ricerca.currentText() == 'Ricerca per codice fiscale/partitaIVA':
            lista_clienti = GestoreClienti.ricerca_ordina_clienti('cf', parametro)
        self.set_lista_clienti(lista_clienti)
