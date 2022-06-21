from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneClienti.VistaEliminaCliente import VistaEliminaCliente
from viste.visteGestioneClienti.VistaModificaCliente import VistaModificaCliente


class VistaInformazioniCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaInformazioniCliente, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel('ID')
        self.label_nome_marchionimo = QLabel('NOME/MARCHIONIMO')
        self.label_cognome = QLabel('COGNOME')
        self.label_codice_fiscale_IVA = QLabel('CODICE FISCALE/PARTITA IVA')
        self.label_email = QLabel('EMAIL')
        self.label_telefono = QLabel('TELEFONO')
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Nome/Marchionimo:', self.label_nome_marchionimo)
        self.f_layout.addRow('Cognome:', self.label_cognome)
        self.f_layout.addRow('Codice Fiscale/Partita IVA:', self.label_codice_fiscale_IVA)
        self.f_layout.addRow('Indirizzo e-mail:', self.label_email)
        self.f_layout.addRow('N. Telefono:', self.label_telefono)
        self.button_modifica_cliente = QPushButton('Modifica cliente...')
        self.button_modifica_cliente.clicked.connect(self.open_modifica_cliente)
        self.button_elimina_cliente = QPushButton('Elimina cliente...')
        self.button_elimina_cliente.clicked.connect(self.open_elimina_cliente)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_modifica_cliente)
        self.v_layout.addWidget(self.button_elimina_cliente)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli cliente")
        self.setMinimumSize(QSize(350, 180))
        self.setMaximumHeight(180)

    def open_modifica_cliente(self):
        self.vista_modifica_cliente = VistaModificaCliente()
        self.vista_modifica_cliente.show()

    def open_elimina_cliente(self):
        self.vista_elimina_cliente = VistaEliminaCliente()
        self.vista_elimina_cliente.show()
