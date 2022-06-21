from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QComboBox

from gestione.GestoreMagazzino import GestoreMagazzino
from viste.visteGestioneMagazzino.VistaInformazioniProdotto import VistaInformazioniProdotto
from viste.visteGestioneMagazzino.VistaInserisciProdotto import VistaInserisciProdotto


class VistaGestioneMagazzino(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneMagazzino, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label = QLabel('Ricerca:')
        self.barra_ricerca = QLineEdit()
        self.tipo_ricerca = QComboBox()
        self.tipo_ricerca.addItem('Ricerca per nome')
        self.tipo_ricerca.addItem('Ricerca per ID')
        self.tipo_ricerca.addItem('Ricerca per fornitore')
        self.button_cerca = QPushButton('Cerca')
        self.button_cerca.clicked.connect(lambda: self.ricerca_lista_prodotti('nome', False))
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.tipo_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.h_layout_2 = QHBoxLayout()
        self.label_scelta_ordinamento = QLabel('Ordinamento:')
        self.scelta_ordinamento_cbox = QComboBox()
        self.scelta_ordinamento_cbox.addItem('ID crescente')
        self.scelta_ordinamento_cbox.addItem('ID decrescente')
        self.scelta_ordinamento_cbox.addItem('Nome A-Z')
        self.scelta_ordinamento_cbox.addItem('Nome Z-A')
        self.scelta_ordinamento_cbox.addItem('Data crescente')
        self.scelta_ordinamento_cbox.addItem('Data decrescente')
        self.scelta_ordinamento_cbox.addItem('Prezzo crescente')
        self.scelta_ordinamento_cbox.addItem('Prezzo decrescente')
        self.button_cambia_ordinamento = QPushButton('OK')
        self.button_cambia_ordinamento.clicked.connect(self.ordina_lista_prodotti)
        self.h_layout_2.addWidget(self.label_scelta_ordinamento)
        self.h_layout_2.addWidget(self.scelta_ordinamento_cbox)
        self.h_layout_2.addWidget(self.button_cambia_ordinamento)  # DA RIVEDERE DISPOSIZIONE
        self.lista_prodotti = QListWidget()
        GestoreMagazzino.aggiorna_database_prodotti()
        self.set_lista_prodotti(GestoreMagazzino.database_prodotti)
        self.lista_prodotti.itemActivated.connect(self.open_informazioni_prodotto)
        self.button_inserisci_prodotto = QPushButton('Inserisci prodotto...')
        self.button_inserisci_prodotto.clicked.connect(self.open_inserisci_prodotto)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.h_layout_2)
        self.v_layout.addWidget(self.lista_prodotti)
        self.v_layout.addWidget(self.button_inserisci_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Magazzino")
        self.setMinimumSize(700, 900)


    def open_inserisci_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto()
        self.vista_inserisci_prodotto.show()

    def open_informazioni_prodotto(self, item):
        prodotto_dict = {}
        id_prodotto = int(item.text().split(' ')[0])
        for prodotto in GestoreMagazzino.database_prodotti:
            if prodotto['_id'] == id_prodotto:
                prodotto_dict = prodotto
                break
        self.vista_informazioni_prodotto = VistaInformazioniProdotto(prodotto=prodotto_dict)
        self.vista_informazioni_prodotto.show()

    def set_lista_prodotti(self, lista_prodotti):
        self.lista_prodotti.clear()
        if len(lista_prodotti) != 0:
            for prodotto in lista_prodotti:
                self.lista_prodotti.addItem(f'{str(prodotto["_id"])} | {str(prodotto["nome"])} | Giacenza: {str(prodotto["giacenza"])} | Prezzo: {str(prodotto["prezzo"])}')

    def ricerca_lista_prodotti(self, tipo_ordinamento, decrescente):
        parametro = self.barra_ricerca.text()
        lista_prodotti = []
        if self.tipo_ricerca.currentText() == 'Ricerca per nome':
            lista_prodotti = GestoreMagazzino.ricerca_ordina_prodotti('nome', parametro, tipo_ordinamento, decrescente)
        elif self.tipo_ricerca.currentText() == 'Ricerca per ID':
            lista_prodotti = GestoreMagazzino.ricerca_ordina_prodotti('_id', parametro, tipo_ordinamento, decrescente)
        elif self.tipo_ricerca.currentText() == 'Ricerca per fornitore':
            lista_prodotti = GestoreMagazzino.ricerca_ordina_prodotti('fornitore', parametro, tipo_ordinamento, decrescente)
        self.set_lista_prodotti(lista_prodotti)

    def ordina_lista_prodotti(self):
        tipo_ordinamento = 'nome'
        decrescente = False
        if self.scelta_ordinamento_cbox.currentText() == 'Nome A-Z':
            tipo_ordinamento = 'nome'
            decrescente = False
        elif self.scelta_ordinamento_cbox.currentText() == 'Nome Z-A':
            tipo_ordinamento = 'nome'
            decrescente = True
        elif self.scelta_ordinamento_cbox.currentText() == 'ID crescente':
            tipo_ordinamento = '_id'
            decrescente = False
        elif self.scelta_ordinamento_cbox.currentText() == 'ID decrescente':
            tipo_ordinamento = '_id'
            decrescente = True
        elif self.scelta_ordinamento_cbox.currentText() == 'Prezzo crescente':
            tipo_ordinamento = 'prezzo'
            decrescente = False
        elif self.scelta_ordinamento_cbox.currentText() == 'Prezzo decrescente':
            tipo_ordinamento = 'prezzo'
            decrescente = True
        elif self.scelta_ordinamento_cbox.currentText() == 'Data crescente':
            tipo_ordinamento = 'data_immagazzinamento'
            decrescente = False
        elif self.scelta_ordinamento_cbox.currentText() == 'Data decrescente':
            tipo_ordinamento = 'data_immagazzinamento'
            decrescente = True
        self.ricerca_lista_prodotti(tipo_ordinamento, decrescente)