from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, \
    QListWidget, QProgressBar, QFormLayout

from gestione.GestoreColorificio import GestoreColorificio
from viste.visteGestioneColorificio.VistaInformazioniBase import VistaInformazioniBase
from viste.visteGestioneColorificio.VistaInserisciBase import VistaInserisciBase
from viste.visteGestioneColorificio.VistaModificaGiacenzaColoranti import VistaModificaGiacenzaColoranti


class VistaScorteColorificio(QWidget):

    def __init__(self, parent=None):
        super(VistaScorteColorificio, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.label = QLabel('Ricerca:')
        self.barra_ricerca = QLineEdit()
        self.button_cerca = QPushButton('Cerca/Aggiorna')
        self.button_cerca.clicked.connect(self.ricerca_lista_basi)
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.barra_ricerca)
        self.h_layout.addWidget(self.button_cerca)
        self.lista_basi = QListWidget()
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        self.set_lista_basi(GestoreColorificio.database_basi)
        self.lista_basi.itemActivated.connect(self.open_informazioni_base)
        self.button_inserisci_base = QPushButton('Inserisci base...')
        self.button_inserisci_base.clicked.connect(self.open_inserisci_base)
        self.f_layout = QFormLayout()
        self.quantita_rosso = QProgressBar()
        self.quantita_blu = QProgressBar()
        self.quantita_giallo = QProgressBar()
        self.quantita_rosso.setMaximum(10000)
        self.quantita_blu.setMaximum(10000)
        self.quantita_giallo.setMaximum(10000)
        valore_rosso = GestoreColorificio.colorante_rosso.get_giacenza_litri() * 100
        valore_blu = GestoreColorificio.colorante_blu.get_giacenza_litri() * 100
        valore_giallo = GestoreColorificio.colorante_giallo.get_giacenza_litri() * 100
        self.quantita_rosso.setValue(int(valore_rosso))
        self.quantita_rosso.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #DC143C;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.quantita_blu.setValue(int(valore_blu))
        self.quantita_blu.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #1E90FF;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.quantita_giallo.setValue(int(valore_giallo))
        self.quantita_giallo.setStyleSheet("""
                                          QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            text-align: center
                                          }
                                          QProgressBar::chunk {
                                            background-color: #FFD700;
                                            width: 10px;
                                            margin: 1px;
                                          }
                                          """)
        self.f_layout.addRow('Giacenza rosso:', self.quantita_rosso)
        self.f_layout.addRow('Giacenza blu:', self.quantita_blu)
        self.f_layout.addRow('Giacenza giallo:', self.quantita_giallo)
        self.button_modifica_giacenza_coloranti = QPushButton('Modifica giacenza coloranti...')
        self.button_modifica_giacenza_coloranti.clicked.connect(self.open_modifica_giacenza_coloranti)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.lista_basi)
        self.v_layout.addWidget(self.button_inserisci_base)
        self.v_layout.addWidget(QLabel('Giacenza coloranti su 100.0 L massimi per ognuno:'))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_modifica_giacenza_coloranti)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Scorte Colorificio")
        self.setMinimumSize(700, 900)

    def open_inserisci_base(self):
        self.vista_inserisci_base = VistaInserisciBase()
        self.vista_inserisci_base.show()

    def open_informazioni_base(self, item):
        base_dict = {}
        id_base = int(item.text().split(' ')[0])
        for base in GestoreColorificio.database_basi:
            if base['_id'] == id_base:
                base_dict = base
                break
        self.vista_informazioni_prodotto = VistaInformazioniBase(base=base_dict)
        self.vista_informazioni_prodotto.show()

    def open_modifica_giacenza_coloranti(self):
        self.vista_modifica_giacenza_coloranti = VistaModificaGiacenzaColoranti()
        self.vista_modifica_giacenza_coloranti.show()

    def set_lista_basi(self, lista_basi):
        self.lista_basi.clear()
        if len(lista_basi) != 0:
            for base in lista_basi:
                self.lista_basi.addItem(
                    f'{str(base["_id"])} | {str(base["nome"])} | Giacenza: {str(base["giacenza"])} | Prezzo/L: {str(base["prezzo_al_litro"])} | Volume (L): {str(base["volume"])}')

    def ricerca_lista_basi(self):
        parametro = self.barra_ricerca.text()
        lista_basi = GestoreColorificio.ricerca_basi(parametro)
        self.set_lista_basi(lista_basi)
