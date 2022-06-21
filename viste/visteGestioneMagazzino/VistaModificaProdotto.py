from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QTextEdit, \
    QDoubleSpinBox, QSpinBox, QSlider


class VistaModificaProdotto(QWidget):

    def __init__(self, parent=None):
        super(VistaModificaProdotto, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_nome = QLineEdit()
        self.input_prezzo = QDoubleSpinBox()
        self.input_prezzo.setMaximum(10000.0)
        self.input_giacenza = QSpinBox()
        self.input_giacenza.setMinimum(-1000)
        self.input_giacenza.setMaximum(1000)
        self.input_numero_scaffale = QSpinBox()
        self.input_numero_scaffale.setMinimum(1)
        self.input_numero_scaffale.setMaximum(15)
        self.input_livello = QSpinBox()
        self.input_livello.setMinimum(1)
        self.input_livello.setMaximum(2)
        self.input_posizione = QSpinBox()
        self.input_posizione.setMinimum(1)
        self.input_posizione.setMaximum(25)
        self.input_lunghezza = QDoubleSpinBox()
        self.input_lunghezza.setMaximum(1000.0)
        self.input_larghezza = QDoubleSpinBox()
        self.input_larghezza.setMaximum(1000.0)
        self.input_profondita = QDoubleSpinBox()
        self.input_profondita.setMaximum(1000.0)
        self.input_peso = QDoubleSpinBox()
        self.input_peso.setMaximum(1000.0)
        self.input_note = QTextEdit()
        self.f_layout.addRow('Nome:', self.input_nome)
        self.f_layout.addRow('Prezzo:', self.input_prezzo)
        self.f_layout.addRow('Giacenza:', self.input_giacenza)
        self.f_layout.addRow('N. Scaffale:', self.input_numero_scaffale)
        self.f_layout.addRow('Livello:', self.input_livello)
        self.f_layout.addRow('Posizione:', self.input_posizione)
        self.f_layout.addRow('Lunghezza (cm):', self.input_lunghezza)
        self.f_layout.addRow('Larghezza (cm):', self.input_larghezza)
        self.f_layout.addRow('Profondità (cm):', self.input_profondita)
        self.f_layout.addRow('Peso (kg):', self.input_peso)
        self.f_layout.addRow('Note:', self.input_note)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(self.check_login)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica prodotto")
        self.setMinimumSize(QSize(400, 450))
        self.setMaximumHeight(450)

    def check_login(self):
        pass