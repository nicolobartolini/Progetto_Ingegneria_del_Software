from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton

from gestione.GestoreImpiegati import GestoreImpiegati
from viste.VistaHome import VistaHome
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Inserisci nome utente e password per entrare nel sistema:')
        self.f_layout = QFormLayout()
        self.text_input_username = QLineEdit()
        self.text_input_password = QLineEdit()
        self.text_input_password.setEchoMode(QLineEdit.Password)
        self.f_layout.addRow('Nome utente:', self.text_input_username)
        self.f_layout.addRow('Password:', self.text_input_password)
        self.button_login = QPushButton('Log in')
        self.button_login.clicked.connect(self.check_login)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_login)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestionale Colorificio")
        self.setFixedSize(QSize(300, 120))

    def check_login(self):
        nome_utente = self.text_input_username.text()
        password = self.text_input_password.text()
        impiegato = GestoreImpiegati.collection_impiegati.find_one({'_id': nome_utente})
        if impiegato is None:
            self.messaggio_username_non_trovato = VistaMessaggioGenerico(msg='Nome utente non trovato.')
            self.messaggio_username_non_trovato.show()
        else:
            if password == impiegato['password']:
                self.vista_home = VistaHome(nome_utente=impiegato['_id'], ruolo=impiegato['ruolo'])
                self.vista_home.show()
                self.close()
            else:
                self.messaggio_password_errata = VistaMessaggioGenerico(msg='Password errata.')
                self.messaggio_password_errata.show()
