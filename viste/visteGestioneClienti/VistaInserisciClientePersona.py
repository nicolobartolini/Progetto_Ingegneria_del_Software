from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton


class VistaInserisciClientePersona(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciClientePersona, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Inserisci i dati del cliente che vuoi inserire:')
        self.f_layout = QFormLayout()
        self.input_nome = QLineEdit()
        self.input_cognome = QLineEdit()
        self.input_codice_fiscale = QLineEdit()
        self.input_email = QLineEdit()
        self.input_telefono = QLineEdit()
        self.f_layout.addRow('Nome:', self.input_nome)
        self.f_layout.addRow('Cognome:', self.input_cognome)
        self.f_layout.addRow('Codice Fiscale:', self.input_codice_fiscale)
        self.f_layout.addRow('Indirizzo e-mail:', self.input_email)
        self.f_layout.addRow('N. telefono:', self.input_telefono)
        self.button_inserisci_cliente = QPushButton('Inserisci cliente')
        self.button_inserisci_cliente.clicked.connect(self.inserisci_cliente)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_inserisci_cliente)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento cliente (azienda)")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def inserisci_cliente(self):
        pass

    def load_basi_cbox(self):
        pass