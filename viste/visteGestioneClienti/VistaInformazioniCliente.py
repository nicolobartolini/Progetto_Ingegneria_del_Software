from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton, QListWidget

from gestione.GestoreDocumenti import GestoreDocumenti
from viste.visteGestioneClienti.VistaEliminaCliente import VistaEliminaCliente
from viste.visteGestioneClienti.VistaModificaCliente import VistaModificaCliente


class VistaInformazioniCliente(QWidget):

    def __init__(self, parent=None, cliente: dict = None):
        super(VistaInformazioniCliente, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel(str(cliente['_id']))
        self.f_layout.addRow('ID:', self.label_ID)
        if cliente['tipo'] == 'persona':
            self.label_nome = QLabel(str(cliente['nome']))
            self.label_cognome = QLabel(str(cliente['cognome']))
            self.label_codice_fiscale = QLabel(cliente['codice_fiscale'])
            self.f_layout.addRow('Nome:', self.label_nome)
            self.f_layout.addRow('Cognome:', self.label_cognome)
            self.f_layout.addRow('Codice Fiscale:', self.label_codice_fiscale)
        elif cliente['tipo'] == 'azienda':
            self.label_marchionimo = QLabel(str(cliente['marchionimo']))
            self.label_partita_IVA = QLabel(str(cliente['partitaIVA']))
            self.f_layout.addRow('Marchionimo:', self.label_marchionimo)
            self.f_layout.addRow('Partita IVA:', self.label_partita_IVA)
        self.label_email = QLabel(str(cliente['indirizzo_email']))
        self.label_telefono = QLabel(str(cliente['telefono']))
        self.f_layout.addRow('Indirizzo e-mail:', self.label_email)
        self.f_layout.addRow('N. Telefono:', self.label_telefono)
        self.label_lista_documenti = QLabel('Documenti:')
        self.lista_documenti = QListWidget()
        self.set_lista_documenti(cliente)
        self.button_modifica_cliente = QPushButton('Modifica cliente...')
        self.button_modifica_cliente.clicked.connect(lambda: self.open_modifica_cliente(id=cliente['_id'], tipo=cliente['tipo']))
        self.button_elimina_cliente = QPushButton('Elimina cliente...')
        self.button_elimina_cliente.clicked.connect(lambda: self.open_elimina_cliente(id=cliente['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.label_lista_documenti)
        self.v_layout.addWidget(self.lista_documenti)
        self.v_layout.addWidget(self.button_modifica_cliente)
        self.v_layout.addWidget(self.button_elimina_cliente)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli cliente")
        self.setMinimumSize(QSize(350, 350))
        self.setMaximumHeight(500)

    def open_modifica_cliente(self, id: int, tipo: str):
        self.vista_modifica_cliente = VistaModificaCliente(id=id, tipo=tipo)
        self.vista_modifica_cliente.show()

    def open_elimina_cliente(self, id: int):
        self.vista_elimina_cliente = VistaEliminaCliente(id=id)
        self.vista_elimina_cliente.show()
        self.close()

    def set_lista_documenti(self, cliente: dict):
        if len(cliente['documenti']) != 0:
            for id_documento in cliente['documenti']:
                documento = GestoreDocumenti.collection_documenti.find_one({'_id': id_documento})
                self.lista_documenti.addItem(f'{str(id_documento)} | {str(documento["nome"])} | Pagamento: {str(documento["pagamento"])}')
        else:
            self.lista_documenti.addItem('Nessun documento intestato al cliente')
