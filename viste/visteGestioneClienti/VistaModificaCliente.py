from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton


class VistaModificaCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaCliente, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_nome_marchionimo = QLineEdit()
        self.input_cognome = QLineEdit()
        self.input_codice_fiscale_IVA = QLineEdit()
        self.input_email = QLineEdit()
        self.input_telefono = QLineEdit()
        self.f_layout.addRow('Nome/Marchionimo:', self.input_nome_marchionimo)
        self.f_layout.addRow('Cognome:', self.input_cognome)
        self.f_layout.addRow('Codice Fiscale/PartitaIVA:', self.input_codice_fiscale_IVA)
        self.f_layout.addRow('Indirizzo e-mail:', self.input_email)
        self.f_layout.addRow('N. telefono:', self.input_telefono)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(self.modifica_cliente)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica cliente")
        self.setMinimumSize(QSize(250, 175))
        self.setMaximumHeight(175)

    def modifica_cliente(self):
        pass

    def load_basi_cbox(self):
        pass