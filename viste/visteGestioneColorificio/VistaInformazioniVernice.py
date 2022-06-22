from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from gestione.GestoreColorificio import GestoreColorificio
from viste.visteGestioneColorificio.VistaRimuoviVernice import VistaRimuoviVernice


class VistaInformazioniVernice(QWidget):

    def __init__(self, parent=None, vernice: dict = None):
        super(VistaInformazioniVernice, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel(str(vernice['_id']))
        self.label_descrizione = QLabel(str(vernice['descrizione']))
        base = GestoreColorificio.collection_basi.find_one({'_id': int(vernice['id_base'])})['nome']
        self.label_base = QLabel(str(base))
        self.label_quantita_rosso = QLabel(str(vernice['quantita_rosso']))
        self.label_quantita_blu = QLabel(str(vernice['quantita_blu']))
        self.label_quantita_giallo = QLabel(str(vernice['quantita_giallo']))
        self.label_prezzo = QLabel(str(vernice['prezzo']))
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Descrizione:', self.label_descrizione)
        self.f_layout.addRow('Base:', self.label_base)
        self.f_layout.addRow('Quantità rosso:', self.label_quantita_rosso)
        self.f_layout.addRow('Quantità blu:', self.label_quantita_blu)
        self.f_layout.addRow('Quantità giallo:', self.label_quantita_giallo)
        self.f_layout.addRow('Prezzo:', self.label_prezzo)
        self.button_elimina_prodotto = QPushButton('Rimuovi vernice...')
        self.button_elimina_prodotto.clicked.connect(lambda: self.open_rimuovi_vernice(vernice['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_elimina_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli vernice")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def open_rimuovi_vernice(self, id: int):
        self.vista_rimuovi_vernice = VistaRimuoviVernice(id=id)
        self.vista_rimuovi_vernice.show()
        self.close()
