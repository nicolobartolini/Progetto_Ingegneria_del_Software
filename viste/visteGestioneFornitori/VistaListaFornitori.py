from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreFornitori import GestoreFornitori
from viste.visteGestioneColorificio.VistaInformazioniVernice import VistaInformazioniVernice
from viste.visteGestioneColorificio.VistaInserisciVernice import VistaInserisciVernice
from viste.visteGestioneFornitori.VistaInserisciFornitore import VistaInserisciFornitore
from viste.visteGestioneFornitori.VistaRimuoviFornitore import VistaRimuoviFornitore


class VistaListaFornitori(QWidget):

    def __init__(self, parent=None):
        super(VistaListaFornitori, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.label = QLabel('Lista fornitori:')
        self.lista_fornitori = QListWidget()
        GestoreFornitori.aggiorna_database_gestore_fornitori()
        self.set_lista_fornitori(GestoreFornitori.database_fornitori)
        self.lista_fornitori.itemActivated.connect(self.open_rimuovi_fornitore)
        self.button_inserisci_fornitore = QPushButton('Inserisci fornitore...')
        self.button_inserisci_fornitore.clicked.connect(self.open_inserisci_fornitore)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.lista_fornitori)
        self.v_layout.addWidget(self.button_inserisci_fornitore)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Lista fornitori")
        self.setMinimumSize(700, 400)

    def set_lista_fornitori(self, lista_fornitori):
        self.lista_fornitori.clear()
        if len(lista_fornitori) != 0:
            for fornitore in lista_fornitori:
                self.lista_fornitori.addItem(
                    f'{fornitore["_id"]} | {str(fornitore["marchionimo"])} | {str(fornitore["partitaIVA"])}')

    def open_rimuovi_fornitore(self, item):
        marchionimo = item.text().split(' ')[2]
        self.vista_rimuovi_fornitore = VistaRimuoviFornitore(marchionimo=marchionimo)
        self.vista_rimuovi_fornitore.show()

    def open_inserisci_fornitore(self):
        self.vista_inserisci_fornitore = VistaInserisciFornitore()
        self.vista_inserisci_fornitore.show()