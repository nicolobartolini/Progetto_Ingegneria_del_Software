from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFormLayout, QComboBox, QListWidget

from Documento import Documento
from Vernice import Vernice
from gestione.GestoreClienti import GestoreClienti
from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreDocumenti import GestoreDocumenti
from gestione.GestoreMagazzino import GestoreMagazzino


class VistaCreaFattura(QWidget):

    def __init__(self, parent=None):
        super(VistaCreaFattura, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_cliente = QComboBox()
        self.set_cbox_clienti()
        self.prodotti = QComboBox()
        self.set_cbox_prodotti()
        self.button_aggiungi_prodotto = QPushButton('Aggiungi prodotto')
        self.button_aggiungi_prodotto.clicked.connect(self.aggiungi_prodotto_a_lista)
        self.lista_prodotti = QListWidget()
        self.vernici = QComboBox()
        self.set_cbox_vernici()
        self.button_aggiungi_vernice = QPushButton('Aggiungi vernice')
        self.button_aggiungi_vernice.clicked.connect(self.aggiungi_vernice_a_lista)
        self.lista_vernici = QListWidget()
        self.f_layout.addRow('Cliente:', self.input_cliente)
        self.f_layout.addRow(self.prodotti, self.button_aggiungi_prodotto)
        self.f_layout.addRow('Prodotti:', self.lista_prodotti)
        self.f_layout.addRow(self.vernici, self.button_aggiungi_vernice)
        self.f_layout.addRow('Vernici:', self.lista_vernici)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(self.crea_fattura)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Creazione fattura")
        self.setMinimumSize(QSize(250, 500))
        self.setMaximumHeight(800)

    def set_cbox_clienti(self):
        GestoreClienti.aggiorna_database_gestore_clienti()
        for cliente in GestoreClienti.database_clienti:
            if cliente['tipo'] == 'persona':
                self.input_cliente.addItem(f'{cliente["_id"]} | {cliente["nome"]} {cliente["cognome"]}')
            elif cliente['tipo'] == 'azienda':
                self.input_cliente.addItem(f'{cliente["_id"]} | {cliente["marchionimo"]}')

    def set_cbox_prodotti(self):
        GestoreMagazzino.aggiorna_database_gestore_prodotti()
        self.prodotti.clear()
        for prodotto in GestoreMagazzino.database_prodotti:
            if prodotto['giacenza'] > 0:
                self.prodotti.addItem(
                    f'{prodotto["_id"]} | {prodotto["nome"]} | Giacenza: {prodotto["giacenza"]} | {prodotto["prezzo"]} €')

    def set_cbox_vernici(self):
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        self.vernici.clear()
        for vernice in GestoreColorificio.database_vernici:
            self.vernici.addItem(f'{vernice["_id"]} | {vernice["descrizione"]} | {vernice["prezzo"]} €')

    def aggiungi_prodotto_a_lista(self):
        prodotto_da_aggiungere = self.prodotti.currentText()
        id_prodotto_da_aggiungere = int(prodotto_da_aggiungere.split(' ')[0])
        self.lista_prodotti.addItem(prodotto_da_aggiungere)
        GestoreMagazzino.diminuisci_giacenza_prodotto(id_prodotto_da_aggiungere, 1)
        self.set_cbox_prodotti()

    def aggiungi_vernice_a_lista(self):
        vernice_da_aggiungere = self.vernici.currentText()
        id_vernice_da_aggiungere = int(vernice_da_aggiungere.split(' ')[0])
        self.lista_vernici.addItem(vernice_da_aggiungere)
        nuova_vernice_dict = GestoreColorificio.collection_vernici.find_one({'_id': id_vernice_da_aggiungere})
        nuova_vernice = Vernice(GestoreColorificio.get_prossimo_id_vernice(), nuova_vernice_dict['descrizione'],
                                nuova_vernice_dict['id_base'], nuova_vernice_dict['quantita_rosso'],
                                nuova_vernice_dict['quantita_blu'], nuova_vernice_dict['quantita_giallo'])
        GestoreColorificio.aggiungi_vernice(nuova_vernice)
        self.set_cbox_vernici()

    def crea_fattura(self):
        id_cliente = int(self.input_cliente.currentText().split(' ')[0])
        id_prodotti = []
        for i in range(self.lista_prodotti.count()):
            id_prodotti.append(int(self.lista_prodotti.item(i).text().split(' ')[0]))
        id_vernici = []
        for i in range(self.lista_vernici.count()):
            id_vernici.append(int(self.lista_vernici.item(i).text().split(' ')[0]))
        documento = Documento(GestoreDocumenti.get_prossimo_id_documento(), 'fattura', id_prodotti, id_vernici,
                              id_cliente)
        GestoreDocumenti.aggiungi_documento(documento)
        self.close()
