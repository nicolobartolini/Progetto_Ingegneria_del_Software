from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from viste.visteGestioneColorificio.VistaScorteColorificio import VistaScorteColorificio
from viste.visteGestioneColorificio.VistaStoricoVernici import VistaStoricoVernici


class VistaGestioneColorificio(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneColorificio, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button('Storico vernici', self.open_storico), 0, 0, 1, 1)
        grid_layout.addWidget(self.get_generic_button('Scorte colorificio', self.open_scorte), 0, 2, 1, 1)
        self.setLayout(grid_layout)
        self.setFixedSize(600, 300)
        self.setWindowTitle("Gestione colorificio")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setStyleSheet('font-size: 25px;')
        return button

    def open_storico(self):
        self.vista_storico_vernici = VistaStoricoVernici()
        self.vista_storico_vernici.show()

    def open_scorte(self):
        self.vista_scorte_colorificio = VistaScorteColorificio()
        self.vista_scorte_colorificio.show()
