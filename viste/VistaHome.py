from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel

from viste.visteGestioneClienti.VistaGestioneClienti import VistaGestioneClienti
from viste.visteGestioneColorificio.VistaGestioneColorificio import VistaGestioneColorificio
from viste.visteGestioneDocumentazione.VistaGestioneDocumentazione import VistaGestioneDocumentazione
from viste.visteGestioneMagazzino.VistaGestioneMagazzino import VistaGestioneMagazzino


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        self.label_username = QLabel('Username:')
        self.button_logout = QPushButton('Log out')
        grid_layout.addWidget(self.label_username, 0, 0, 1, 1)
        grid_layout.addWidget(self.button_logout, 0, 3, 1, 1)
        grid_layout.addWidget(self.get_generic_button('Gestione magazzino', self.open_magazzino), 1, 0, 1, 2)
        grid_layout.addWidget(self.get_generic_button('Gestione colorificio', self.open_colorificio), 1, 2, 1, 2)
        grid_layout.addWidget(self.get_generic_button('Gestione clienti', self.open_clienti), 2, 0, 1, 2)
        grid_layout.addWidget(self.get_generic_button('Gestione documentazione', self.open_documentazione), 2, 2, 1, 2)
        self.button_impiegati = QPushButton('Gestione impiegati')
        self.button_impiegati.setMinimumHeight(50)
        self.button_impiegati.clicked.connect(self.open_impiegati)
        self.button_impiegati.setStyleSheet('font-size: 20px')
        self.button_fornitori = QPushButton('Lista fornitori')
        self.button_fornitori.setMinimumHeight(50)
        self.button_fornitori.clicked.connect(self.open_fornitori)
        self.button_fornitori.setStyleSheet('font-size: 20px')
        grid_layout.addWidget(self.button_impiegati, 3, 0, 1, 3)
        grid_layout.addWidget(self.button_fornitori, 3, 3, 1, 1)
        self.setLayout(grid_layout)
        self.resize(800, 800)
        self.setWindowTitle("Gestionale ITALMONT")
        self.setFixedSize(QSize(1000, 1000))

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setStyleSheet('font-size: 25px;')
        return button

    def open_magazzino(self):
        self.vista_gestione_magazzino = VistaGestioneMagazzino()
        self.vista_gestione_magazzino.show()

    def open_colorificio(self):
        self.vista_gestione_colorificio = VistaGestioneColorificio()
        self.vista_gestione_colorificio.show()

    def open_clienti(self):
        self.vista_gestione_clienti = VistaGestioneClienti()
        self.vista_gestione_clienti.show()

    def open_documentazione(self):
        self.vista_gestione_documentazione = VistaGestioneDocumentazione()
        self.vista_gestione_documentazione.show()

    def open_impiegati(self):
        pass

    def open_fornitori(self):
        pass