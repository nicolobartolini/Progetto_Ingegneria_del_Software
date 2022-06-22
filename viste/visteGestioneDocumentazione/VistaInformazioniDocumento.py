from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton, QListWidget

from gestione.GestoreClienti import GestoreClienti
from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreMagazzino import GestoreMagazzino
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaInformazioniDocumento(QWidget):

    def __init__(self, parent=None, documento: dict = None):
        super(VistaInformazioniDocumento, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel(str(documento['_id']))
        self.label_nome = QLabel(str(documento['nome']))
        cliente = GestoreClienti.collection_clienti.find_one({'_id': int(documento['id_cliente'])})
        if cliente['tipo'] == 'persona':
            self.label_cliente = QLabel(str(f'{cliente["nome"]} {cliente["cognome"]}'))
        elif cliente['tipo'] == 'azienda':
            self.label_cliente = QLabel(str(cliente['marchionimo']))
        self.lista_prodotti = QListWidget()
        self.set_lista_prodotti(documento)
        self.lista_vernici = QListWidget()
        self.set_lista_vernici(documento)
        self.label_pagamento = QLabel(str(documento['pagamento']))
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Nome:', self.label_nome)
        self.f_layout.addRow('Prodotti:', self.lista_prodotti)
        self.f_layout.addRow('Vernici:', self.lista_vernici)
        self.f_layout.addRow('Pagamento:', self.label_pagamento)
        self.button_crea_PDF = QPushButton('Crea pdf...')
        self.button_crea_PDF.clicked.connect(lambda: self.crea_PDF(id=documento['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_crea_PDF)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli documento")
        self.setMinimumSize(QSize(350, 350))
        self.setMaximumHeight(500)

    def crea_PDF(self, id: int):
        self.vista_messaggio_non_siamo_riusciti_a_fare_pdf = VistaMessaggioGenerico(
            msg=f'Impossibile creare PDF per il documento {id}')
        self.vista_messaggio_non_siamo_riusciti_a_fare_pdf.show()
        self.close()

    def set_lista_prodotti(self, documento: dict):
        if len(documento['id_prodotti']) != 0:
            for id_prodotto in documento['id_prodotti']:
                prodotto = GestoreMagazzino.collection_prodotti.find_one({'_id': id_prodotto})
                self.lista_prodotti.addItem(f'{str(id_prodotto)} | {str(prodotto["nome"])}')
        else:
            self.lista_prodotti.addItem('Nessun prodotto nel documento')

    def set_lista_vernici(self, documento: dict):
        if len(documento['id_vernici']) != 0:
            for id_vernice in documento['id_vernici']:
                vernice = GestoreColorificio.collection_vernici.find_one({'_id': id_vernice})
                self.lista_vernici.addItem(f'{str(id_vernice)} | {str(vernice["descrizione"])}')
        else:
            self.lista_vernici.addItem('Nessuna vernice nel documento')
