from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox

from Impiegato import Impiegato
from gestione.GestoreImpiegati import GestoreImpiegati
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaModificaImpiegato(QWidget):

    def __init__(self, parent=None, nome_utente=None):
        super(VistaModificaImpiegato, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_nome = QLineEdit()
        self.input_cognome = QLineEdit()
        self.input_nome_utente = QLineEdit()
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_ruolo = QComboBox()
        self.input_ruolo.addItem('Amministratore')
        self.input_ruolo.addItem('Magazziniere')
        self.input_ruolo.addItem('Banconista')
        self.f_layout.addRow('Nome:', self.input_nome)
        self.f_layout.addRow('Cognome:', self.input_cognome)
        self.f_layout.addRow('Nome utente:', self.input_nome_utente)
        self.f_layout.addRow('Password:', self.input_password)
        self.f_layout.addRow('Ruolo:', self.input_ruolo)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(lambda: self.modifica_impiegato(id))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica utente")
        self.setMinimumSize(QSize(300, 200))
        self.setMaximumHeight(250)

    def modifica_impiegato(self, id):
        nome = self.input_nome.text()
        cognome = self.input_cognome.text()
        nome_utente = self.input_nome_utente.text()
        password = self.input_password.text()
        ruolo = self.input_ruolo.currentText()
        nuovo_impiegato = Impiegato(nome, cognome, nome_utente, password, ruolo)
        GestoreImpiegati.modifica_impiegato(nome_utente, nuovo_impiegato)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Utente modificato con successo!')
        self.messaggio_conferma.show()
        self.close()
