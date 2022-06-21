from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QDoubleSpinBox, QComboBox


class VistaInserisciVernice(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciVernice, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Inserisci i dati della vernice che vuoi inserire:')
        self.f_layout = QFormLayout()
        self.input_descrizione = QLineEdit()
        self.input_base = QComboBox()
        self.load_basi_cbox()
        self.input_quantita_rosso = QDoubleSpinBox()
        self.input_quantita_rosso.setMinimum(0.0)
        self.input_quantita_rosso.setMaximum(1.0)
        self.input_quantita_blu = QDoubleSpinBox()
        self.input_quantita_blu.setMinimum(0.0)
        self.input_quantita_blu.setMaximum(1.0)
        self.input_quantita_giallo = QDoubleSpinBox()
        self.input_quantita_giallo.setMinimum(0.0)
        self.input_quantita_giallo.setMaximum(1.0)
        # FORNITORE
        self.f_layout.addRow('Descrizione:', self.input_descrizione)
        self.f_layout.addRow('Base:', self.input_base)
        self.f_layout.addRow('Quantità rosso:', self.input_quantita_rosso)
        self.f_layout.addRow('Quantità blu:', self.input_quantita_blu)
        self.f_layout.addRow('Quantità giallo:', self.input_quantita_giallo)
        self.button_inserisci_vernice = QPushButton('Inserisci vernice')
        self.button_inserisci_vernice.clicked.connect(self.inserisci_vernice)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_inserisci_vernice)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento vernice")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def inserisci_vernice(self):
        pass

    def load_basi_cbox(self):
        pass