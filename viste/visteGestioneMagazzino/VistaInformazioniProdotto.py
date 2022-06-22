from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneMagazzino.VistaEliminaProdotto import VistaEliminaProdotto
from viste.visteGestioneMagazzino.VistaModificaProdotto import VistaModificaProdotto
from viste.visteGestioneMagazzino.VistaQRCode import VistaQRCode


class VistaInformazioniProdotto(QWidget):

    def __init__(self, parent=None, prodotto: dict = None):
        super(VistaInformazioniProdotto, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel(str(prodotto['_id']))
        self.label_nome = QLabel(str(prodotto['nome']))
        self.label_prezzo = QLabel(str(prodotto['prezzo']))
        self.label_giacenza = QLabel(str(prodotto['giacenza']))
        self.label_data_immagazzinamento = QLabel(str(prodotto['data_immagazzinamento']))
        self.label_numero_scaffale = QLabel(str(prodotto['ubicazione']['numero_scaffale']))
        self.label_livello = QLabel(str(prodotto['ubicazione']['livello']))
        self.label_posizione = QLabel(str(prodotto['ubicazione']['posizione']))
        self.label_lunghezza = QLabel(str(prodotto['dimensione']['lunghezza']))
        self.label_larghezza = QLabel(str(prodotto['dimensione']['larghezza']))
        self.label_profondita = QLabel(str(prodotto['dimensione']['profondita']))
        self.label_peso = QLabel(str(prodotto['dimensione']['peso']))
        self.label_note = QLabel(str(prodotto['note']))
        self.f_layout.addRow('ID:', self.label_ID)
        self.f_layout.addRow('Nome:', self.label_nome)
        self.f_layout.addRow('Prezzo:', self.label_prezzo)
        self.f_layout.addRow('Giacenza:', self.label_giacenza)
        self.f_layout.addRow('Data immagazzinamento:', self.label_data_immagazzinamento)
        self.f_layout.addRow('N. scaffale:', self.label_numero_scaffale)
        self.f_layout.addRow('Livello:', self.label_livello)
        self.f_layout.addRow('Posizione:', self.label_posizione)
        self.f_layout.addRow('Lunghezza:', self.label_lunghezza)
        self.f_layout.addRow('Larghezza:', self.label_larghezza)
        self.f_layout.addRow('Profondità:', self.label_profondita)
        self.f_layout.addRow('Peso:', self.label_peso)
        self.f_layout.addRow('Note:', self.label_note)
        self.button_creaQR = QPushButton('Crea QR code ubicazione...')
        self.button_creaQR.clicked.connect(lambda: self.open_QR(prodotto['_id']))
        self.button_modifica_prodotto = QPushButton('Modifica prodotto...')
        self.button_modifica_prodotto.clicked.connect(lambda: self.open_modifica_prodotto(prodotto['_id']))
        self.button_elimina_prodotto = QPushButton('Elimina prodotto...')
        self.button_elimina_prodotto.clicked.connect(lambda: self.open_elimina_prodotto(prodotto['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_creaQR)
        self.v_layout.addWidget(self.button_modifica_prodotto)
        self.v_layout.addWidget(self.button_elimina_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli prodotto")
        self.setMinimumSize(QSize(300, 350))
        self.setMaximumHeight(350)

    def open_QR(self, id: int):
        self.vista_qr = VistaQRCode(id=id)
        self.vista_qr.show()

    def open_modifica_prodotto(self, id: int):
        self.vista_modifica_prodotto = VistaModificaProdotto(id=id)
        self.vista_modifica_prodotto.show()

    def open_elimina_prodotto(self, id: int):
        self.vista_elimina_prodotto = VistaEliminaProdotto(id=id)
        self.vista_elimina_prodotto.show()
        self.close()
