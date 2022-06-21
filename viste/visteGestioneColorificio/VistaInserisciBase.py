from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QDoubleSpinBox, QSpinBox, \
    QComboBox


class VistaInserisciBase(QWidget):

    def __init__(self, parent=None):
        super(VistaInserisciBase, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Inserisci i dati della base che vuoi inserire:')
        self.f_layout = QFormLayout()
        self.input_nome = QLineEdit()
        self.input_giacenza = QSpinBox()
        self.input_giacenza.setMinimum(-1000)
        self.input_giacenza.setMaximum(1000)
        self.input_prezzo_al_litro = QDoubleSpinBox()
        self.input_prezzo_al_litro.setMaximum(100.0)
        self.input_volume = QDoubleSpinBox()
        self.input_volume.setMinimum(0.5)
        self.input_volume.setMaximum(15.0)
        self.input_fornitore = QComboBox()
        # FORNITORE
        self.f_layout.addRow('Nome:', self.input_nome)
        self.f_layout.addRow('Giacenza:', self.input_giacenza)
        self.f_layout.addRow('Prezzo/L:', self.input_prezzo_al_litro)
        self.f_layout.addRow('Volume:', self.input_volume)
        self.f_layout.addRow('Fornitore:', self.input_fornitore)
        self.button_login = QPushButton('Inserisci base')
        self.button_login.clicked.connect(self.check_login)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_login)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserimento base")
        self.setMinimumSize(QSize(300, 200))
        self.setMaximumHeight(250)

    def check_login(self):
        pass