from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneColorificio.VistaEliminaBase import VistaEliminaBase
from viste.visteGestioneColorificio.VistaModificaBase import VistaModificaBase
from viste.visteGestioneMagazzino.VistaEliminaProdotto import VistaEliminaProdotto
from viste.visteGestioneMagazzino.VistaModificaProdotto import VistaModificaProdotto
from viste.visteGestioneMagazzino.VistaQRCode import VistaQRCode


class VistaInformazioniBase(QWidget):

    def __init__(self, parent=None):
        super(VistaInformazioniBase, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel('ID')
        self.label_nome = QLabel('NOME')
        self.label_giacenza = QLabel('GIACENZA')
        self.label_prezzo_al_litro = QLabel('PREZZO/L')
        self.label_volume = QLabel('VOLUME')
        self.label_fornitore = QLabel('FORNITORE')
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Nome:', self.label_nome)
        self.f_layout.addRow('Giacenza:', self.label_giacenza)
        self.f_layout.addRow('Prezzo/L:', self.label_prezzo_al_litro)
        self.f_layout.addRow('Volume:', self.label_volume)
        self.f_layout.addRow('Fornitore:', self.label_fornitore)
        self.button_modifica_base = QPushButton('Modifica base...')
        self.button_modifica_base.clicked.connect(self.open_modifica_base)
        self.button_elimina_base = QPushButton('Elimina base...')
        self.button_elimina_base.clicked.connect(self.open_elimina_base)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_modifica_base)
        self.v_layout.addWidget(self.button_elimina_base)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli base")
        self.setMinimumSize(QSize(300, 180))
        self.setMaximumHeight(180)

    def open_modifica_base(self):
        self.vista_modifica_base = VistaModificaBase()
        self.vista_modifica_base.show()

    def open_elimina_base(self):
        self.vista_elimina_base = VistaEliminaBase()
        self.vista_elimina_base.show()
