from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

from viste.visteGestioneColorificio.VistaInformazioniVernice import VistaInformazioniVernice
from viste.visteGestioneColorificio.VistaInserisciVernice import VistaInserisciVernice


class VistaStoricoVernici(QWidget):

    def __init__(self, parent=None):
        super(VistaStoricoVernici, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Storico vernici:')
        self.lista_vernici = QListWidget()
        for i in range(100):
            self.lista_vernici.addItem(str(i))
        self.lista_vernici.itemActivated.connect(self.open_dettagli_vernice)
        self.button_inserisci_vernice = QPushButton('Inserisci vernice...')
        self.button_inserisci_vernice.clicked.connect(self.open_inserisci_vernice)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.lista_vernici)
        self.v_layout.addWidget(self.button_inserisci_vernice)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Magazzino")
        self.setMinimumSize(700, 900)


    def open_inserisci_vernice(self):
        self.vista_inserisci_vernice = VistaInserisciVernice()
        self.vista_inserisci_vernice.show()

    def open_dettagli_vernice(self, item):
        self.vista_informazioni_vernice = VistaInformazioniVernice()
        self.vista_informazioni_vernice.show()
