from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QDoubleSpinBox, QSpinBox

from Base import Base
from Fornitore import Fornitore
from gestione.GestoreColorificio import GestoreColorificio
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaModificaGiacenzaColoranti(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaGiacenzaColoranti, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_rosso = QDoubleSpinBox()
        self.input_rosso.setMinimum(0)
        self.input_rosso.setMaximum(100.0)
        self.input_rosso.setValue(GestoreColorificio.colorante_rosso.get_giacenza_litri())
        self.input_blu = QDoubleSpinBox()
        self.input_blu.setMinimum(0)
        self.input_blu.setMaximum(100.0)
        self.input_blu.setValue(GestoreColorificio.colorante_blu.get_giacenza_litri())
        self.input_giallo = QDoubleSpinBox()
        self.input_giallo.setMinimum(0)
        self.input_giallo.setMaximum(100.0)
        self.input_giallo.setValue(GestoreColorificio.colorante_giallo.get_giacenza_litri())
        self.f_layout.addRow('Rosso:', self.input_rosso)
        self.f_layout.addRow('Blu:', self.input_blu)
        self.f_layout.addRow('Giallo:', self.input_giallo)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(lambda: self.modifica_giacenza())
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica giacenza coloranti")
        self.setMinimumSize(QSize(200, 175))
        self.setMaximumHeight(175)

    def modifica_giacenza(self):
        nuovo_valore_rosso = self.input_rosso.value()
        nuovo_valore_blu = self.input_blu.value()
        nuovo_valore_giallo = self.input_giallo.value()
        GestoreColorificio.colorante_rosso.set_giacenza_litri(nuovo_valore_rosso)
        GestoreColorificio.colorante_blu.set_giacenza_litri(nuovo_valore_blu)
        GestoreColorificio.colorante_giallo.set_giacenza_litri(nuovo_valore_giallo)
        GestoreColorificio.aggiorna_database_coloranti()
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Giacenze modificate con successo!')
        self.messaggio_conferma.show()
        self.close()
