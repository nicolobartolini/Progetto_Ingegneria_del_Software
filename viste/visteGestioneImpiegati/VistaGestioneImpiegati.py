from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreImpiegati import GestoreImpiegati
from viste.visteGestioneColorificio.VistaInformazioniVernice import VistaInformazioniVernice
from viste.visteGestioneColorificio.VistaInserisciVernice import VistaInserisciVernice
from viste.visteGestioneImpiegati.VistaInformazioniImpiegato import VistaInformazioniImpiegato
from viste.visteGestioneImpiegati.VistaInserisciImpiegato import VistaInserisciImpiegato


class VistaGestioneImpiegati(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneImpiegati, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Lista impiegati:')
        self.lista_impiegati = QListWidget()
        GestoreImpiegati.aggiorna_database_gestore_impiegati()
        self.set_lista_impiegati(GestoreImpiegati.database_impiegati)
        self.lista_impiegati.itemActivated.connect(self.open_dettagli_impiegato)
        self.button_inserisci_vernice = QPushButton('Aggiungi utente...')
        self.button_inserisci_vernice.clicked.connect(self.open_inserisci_impiegato)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.lista_impiegati)
        self.v_layout.addWidget(self.button_inserisci_vernice)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione impiegati")
        self.setMinimumSize(700, 900)

    def open_inserisci_impiegato(self):
        self.vista_inserisci_impiegato = VistaInserisciImpiegato()
        self.vista_inserisci_impiegato.show()

    def open_dettagli_impiegato(self, item):
        impiegato_dict = {}
        nome_utente_impiegato = str(item.text().split(' ')[0])
        for impiegato in GestoreImpiegati.database_impiegati:
            if impiegato['_id'] == nome_utente_impiegato:
                impiegato_dict = impiegato
                break
        self.vista_informazioni_impiegato = VistaInformazioniImpiegato(impiegato=impiegato_dict)
        self.vista_informazioni_impiegato.show()

    def set_lista_impiegati(self, lista_impiegati):
        self.lista_impiegati.clear()
        if len(lista_impiegati) != 0:
            for impiegato in lista_impiegati:
                self.lista_impiegati.addItem(
                    f'{str(impiegato["_id"])} | {impiegato["nome"]} {impiegato["cognome"]} | {str(impiegato["ruolo"])}')
