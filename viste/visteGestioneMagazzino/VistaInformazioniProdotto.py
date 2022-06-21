from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from viste.visteGestioneMagazzino.VistaEliminaProdotto import VistaEliminaProdotto
from viste.visteGestioneMagazzino.VistaModificaProdotto import VistaModificaProdotto
from viste.visteGestioneMagazzino.VistaQRCode import VistaQRCode


class VistaInformazioniProdotto(QWidget):

    def __init__(self, parent=None):
        super(VistaInformazioniProdotto, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_ID = QLabel('ID')
        self.label_nome = QLabel('NOME')
        self.label_prezzo = QLabel('PREZZO')
        self.label_giacenza = QLabel('GIACENZA')
        self.label_data_immagazzinamento = QLabel('DATA IMMAGAZZINAMENTO')
        self.label_numero_scaffale = QLabel('N. SCAFFALE')
        self.label_livello = QLabel('LIVELLO')
        self.label_posizione = QLabel('POSIZIONE')
        self.label_lunghezza = QLabel('LUNGHEZZA')
        self.label_larghezza = QLabel('LARGHEZZA')
        self.label_profondita = QLabel('PROFONDITÀ')
        self.label_peso = QLabel('PESO')
        self.label_note = QLabel('NOTE')
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
        self.button_creaQR.clicked.connect(self.open_QR)
        self.button_modifica_prodotto = QPushButton('Modifica prodotto...')
        self.button_modifica_prodotto.clicked.connect(self.open_modifica_prodotto)
        self.button_elimina_prodotto = QPushButton('Elimina prodotto...')
        self.button_elimina_prodotto.clicked.connect(self.open_elimina_prodotto)
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_creaQR)
        self.v_layout.addWidget(self.button_modifica_prodotto)
        self.v_layout.addWidget(self.button_elimina_prodotto)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli prodotto")
        self.setMinimumSize(QSize(300, 350))
        self.setMaximumHeight(350)

    def open_QR(self):
        self.vista_qr = VistaQRCode()
        self.vista_qr.show()

    def open_modifica_prodotto(self):
        self.vista_modifica_prodotto = VistaModificaProdotto()
        self.vista_modifica_prodotto.show()

    def open_elimina_prodotto(self):
        self.vista_elimina_prodotto = VistaEliminaProdotto()
        self.vista_elimina_prodotto.show()