from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton

from ClienteAzienda import ClienteAzienda
from gestione.GestoreClienti import GestoreClienti
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaInserisciClienteAzienda(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciClienteAzienda, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Inserisci i dati del cliente che vuoi inserire:')
        self.f_layout = QFormLayout()
        self.input_marchionimo = QLineEdit()
        self.input_partitaIVA = QLineEdit()
        self.input_email = QLineEdit()
        self.input_telefono = QLineEdit()
        self.f_layout.addRow('Marchionimo:', self.input_marchionimo)
        self.f_layout.addRow('PartitaIVA:', self.input_partitaIVA)
        self.f_layout.addRow('Indirizzo e-mail:', self.input_email)
        self.f_layout.addRow('N. telefono:', self.input_telefono)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(self.inserisci_cliente)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento cliente (azienda)")
        self.setMinimumSize(QSize(250, 175))
        self.setMaximumHeight(175)

    def inserisci_cliente(self):
        marchionimo = self.input_marchionimo.text()
        partitaIVA = int(self.input_partitaIVA.text())
        email = self.input_email.text()
        telefono = self.input_telefono.text()
        id_documenti = []
        nuovo_cliente = ClienteAzienda(GestoreClienti.get_prossimo_id_cliente(), email, telefono, id_documenti,
                                       marchionimo, partitaIVA)
        GestoreClienti.aggiungi_cliente_azienda(nuovo_cliente)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Cliente inserito con successo')
        self.messaggio_conferma.show()
        self.close()
