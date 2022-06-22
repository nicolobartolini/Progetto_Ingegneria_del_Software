from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QComboBox

from generali.Impiegato import Impiegato
from gestione.GestoreImpiegati import GestoreImpiegati
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaInserisciImpiegato(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciImpiegato, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel("Inserisci i dati dell'impiegato che vuoi inserire:")
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
        self.button_conferma.clicked.connect(self.inserisci_impiegato)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento impiegato")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def inserisci_impiegato(self):
        nome = self.input_nome.text()
        cognome = self.input_cognome.text()
        nome_utente = self.input_nome_utente.text()
        password = self.input_password.text()
        ruolo = self.input_ruolo.currentText()
        nuovo_impiegato = Impiegato(nome, cognome, nome_utente, password, ruolo)
        GestoreImpiegati.aggiungi_impiegato(nuovo_impiegato)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Impiegato inserito con successo')
        self.messaggio_conferma.show()
        self.close()
