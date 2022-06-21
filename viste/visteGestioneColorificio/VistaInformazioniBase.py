from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneColorificio.VistaEliminaBase import VistaEliminaBase
from viste.visteGestioneColorificio.VistaModificaBase import VistaModificaBase


class VistaInformazioniBase(QWidget):

    def __init__(self, parent=None, base: dict = None):
        super(VistaInformazioniBase, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel(str(base['_id']))
        self.label_nome = QLabel(str(base['nome']))
        self.label_giacenza = QLabel(str(base['giacenza']))
        self.label_prezzo_al_litro = QLabel(str(base['prezzo_al_litro']))
        self.label_volume = QLabel(str(base['volume']))
        self.label_fornitore = QLabel(str(base['fornitore']['marchionimo']))
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Nome:', self.label_nome)
        self.f_layout.addRow('Giacenza:', self.label_giacenza)
        self.f_layout.addRow('Prezzo/L:', self.label_prezzo_al_litro)
        self.f_layout.addRow('Volume (L):', self.label_volume)
        self.f_layout.addRow('Fornitore:', self.label_fornitore)
        self.button_modifica_base = QPushButton('Modifica base...')
        self.button_modifica_base.clicked.connect(lambda: self.open_modifica_base(base['_id']))
        self.button_elimina_base = QPushButton('Elimina base...')
        self.button_elimina_base.clicked.connect(lambda: self.open_elimina_base(base['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_modifica_base)
        self.v_layout.addWidget(self.button_elimina_base)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli base")
        self.setMinimumSize(QSize(300, 180))
        self.setMaximumHeight(180)

    def open_modifica_base(self, id: int):
        self.vista_modifica_base = VistaModificaBase(id=id)
        self.vista_modifica_base.show()

    def open_elimina_base(self, id: int):
        self.vista_elimina_base = VistaEliminaBase(id=id)
        self.vista_elimina_base.show()
        self.close()
