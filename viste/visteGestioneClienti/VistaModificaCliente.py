from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton

from ClienteAzienda import ClienteAzienda
from ClientePersona import ClientePersona
from gestione.GestoreClienti import GestoreClienti
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaModificaCliente(QWidget):

    def __init__(self, parent=None, id=1, tipo='persona'):
        super(VistaModificaCliente, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        if tipo == 'persona':
            self.input_nome = QLineEdit()
            self.input_cognome = QLineEdit()
            self.input_codice_fiscale = QLineEdit()
            self.f_layout.addRow('Nome:', self.input_nome)
            self.f_layout.addRow('Cognome:', self.input_cognome)
            self.f_layout.addRow('Codice Fiscale:', self.input_codice_fiscale)
        elif tipo == 'azienda':
            self.input_marchionimo = QLineEdit()
            self.input_partita_IVA = QLineEdit()
            self.f_layout.addRow('Marchionimo:', self.input_marchionimo)
            self.f_layout.addRow('Partita IVA:', self.input_partita_IVA)
        self.input_email = QLineEdit()
        self.input_telefono = QLineEdit()
        self.f_layout.addRow('Indirizzo e-mail:', self.input_email)
        self.f_layout.addRow('N. telefono:', self.input_telefono)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(lambda: self.modifica_cliente(id, tipo))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica cliente")
        self.setMinimumSize(QSize(250, 175))
        self.setMaximumHeight(175)

    def modifica_cliente(self, id, tipo):
        if tipo == 'persona':
            nome = self.input_nome.text()
            cognome = self.input_cognome.text()
            codice_fiscale = self.input_codice_fiscale.text()
            indirizzo_email = self.input_email.text()
            telefono = self.input_telefono.text()
            nuovo_cliente = ClientePersona(id, indirizzo_email, telefono, [], codice_fiscale, cognome, nome)
            GestoreClienti.modifica_cliente_persona(id, nuovo_cliente)
        elif tipo == 'azienda':
            marchionimo = self.input_marchionimo.text()
            partitaIVA = self.input_partita_IVA.text()
            indirizzo_email = self.input_email.text()
            telefono = self.input_telefono.text()
            nuovo_cliente = ClienteAzienda(id, indirizzo_email, telefono, [], marchionimo, partitaIVA)
            GestoreClienti.modifica_cliente_azienda(id, nuovo_cliente)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Cliente modificato con successo!')
        self.messaggio_conferma.show()
        self.close()
