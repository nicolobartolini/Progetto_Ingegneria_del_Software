from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from gestione.GestoreClienti import GestoreClienti


class VistaEliminaCliente(QWidget):

    def __init__(self, parent=None, id=1):
        super(VistaEliminaCliente, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Sei sicuro di voler eliminare il cliente?')
        self.h_layout = QHBoxLayout()
        self.button_si = QPushButton('Sì')
        self.button_si.clicked.connect(lambda: self.elimina_cliente(id))
        self.button_no = QPushButton('No')
        self.button_no.clicked.connect(self.close)
        self.h_layout.addWidget(self.button_si)
        self.h_layout.addWidget(self.button_no)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Elimina cliente")
        self.setFixedSize(250, 70)

    def elimina_cliente(self, id: int):
        GestoreClienti.elimina_cliente(id)
        self.close()
