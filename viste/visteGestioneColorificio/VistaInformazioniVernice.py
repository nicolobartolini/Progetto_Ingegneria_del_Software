from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneColorificio.VistaRimuoviVernice import VistaRimuoviVernice


class VistaInformazioniVernice(QWidget):

    def __init__(self, parent=None):
        super(VistaInformazioniVernice, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel('ID')
        self.label_descrizione = QLabel('DESCRIZIONE')
        self.label_base = QLabel('BASE')
        self.label_quantita_rosso = QLabel('Q. ROSSO')
        self.label_quantita_blu = QLabel('Q. BLU')
        self.label_quantita_giallo = QLabel('Q. GIALLO')
        self.label_prezzo = QLabel('PREZZO')
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Descrizione:', self.label_descrizione)
        self.f_layout.addRow('Base:', self.label_base)
        self.f_layout.addRow('Quantità rosso:', self.label_quantita_rosso)
        self.f_layout.addRow('Quantità blu:', self.label_quantita_blu)
        self.f_layout.addRow('Quantità giallo:', self.label_quantita_giallo)
        self.f_layout.addRow('Prezzo:', self.label_prezzo)
        self.button_elimina_prodotto = QPushButton('Rimuovi vernice...')
        self.button_elimina_prodotto.clicked.connect(self.open_rimuovi_vernice)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_elimina_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli vernice")
        self.setMinimumSize(QSize(250, 200))
        self.setMaximumHeight(200)

    def open_rimuovi_vernice(self):
        self.vista_rimuovi_vernice = VistaRimuoviVernice()
        self.vista_rimuovi_vernice.show()