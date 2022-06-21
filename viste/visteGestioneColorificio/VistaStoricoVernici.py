from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

from gestione.GestoreColorificio import GestoreColorificio
from viste.visteGestioneColorificio.VistaInformazioniVernice import VistaInformazioniVernice
from viste.visteGestioneColorificio.VistaInserisciVernice import VistaInserisciVernice


class VistaStoricoVernici(QWidget):

    def __init__(self, parent=None):
        super(VistaStoricoVernici, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Storico vernici:')
        self.lista_vernici = QListWidget()
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        self.set_lista_vernici(GestoreColorificio.database_vernici)
        self.lista_vernici.itemActivated.connect(self.open_dettagli_vernice)
        self.button_inserisci_vernice = QPushButton('Inserisci vernice...')
        self.button_inserisci_vernice.clicked.connect(self.open_inserisci_vernice)
        self.button_aggiorna_storico = QPushButton('Aggiorna lo storico')
        self.button_aggiorna_storico.clicked.connect(self.aggiorna_storico)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.lista_vernici)
        self.v_layout.addWidget(self.button_inserisci_vernice)
        self.v_layout.addWidget(self.button_aggiorna_storico)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Storico vernici")
        self.setMinimumSize(700, 900)


    def open_inserisci_vernice(self):
        self.vista_inserisci_vernice = VistaInserisciVernice()
        self.vista_inserisci_vernice.show()

    def open_dettagli_vernice(self, item):
        vernice_dict = {}
        id_vernice = int(item.text().split(' ')[0])
        for vernice in GestoreColorificio.database_vernici:
            if vernice['_id'] == id_vernice:
                vernice_dict = vernice
                break
        self.vista_informazioni_vernice = VistaInformazioniVernice(vernice=vernice_dict)
        self.vista_informazioni_vernice.show()

    def set_lista_vernici(self, lista_vernici):
        self.lista_vernici.clear()
        if len(lista_vernici) != 0:
            for vernice in lista_vernici:
                self.lista_vernici.addItem(
                    f'{str(vernice["_id"])} | {str(vernice["descrizione"])} | Prezzo: {str(vernice["prezzo"])}')

    def aggiorna_storico(self):
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        self.set_lista_vernici(GestoreColorificio.database_vernici)