from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTextEdit, \
    QDoubleSpinBox, QSpinBox

from Dimensione import Dimensione
from Fornitore import Fornitore
from Prodotto import Prodotto
from Ubicazione import Ubicazione
from gestione.GestoreMagazzino import GestoreMagazzino
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class VistaModificaProdotto(QWidget):

    def __init__(self, parent=None, id=1):
        super(VistaModificaProdotto, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.input_nome = QLineEdit()
        self.input_prezzo = QDoubleSpinBox()
        self.input_prezzo.setMaximum(10000.0)
        self.input_giacenza = QSpinBox()
        self.input_giacenza.setMinimum(-1000)
        self.input_giacenza.setMaximum(1000)
        self.input_numero_scaffale = QSpinBox()
        self.input_numero_scaffale.setMinimum(1)
        self.input_numero_scaffale.setMaximum(15)
        self.input_livello = QSpinBox()
        self.input_livello.setMinimum(1)
        self.input_livello.setMaximum(2)
        self.input_posizione = QSpinBox()
        self.input_posizione.setMinimum(1)
        self.input_posizione.setMaximum(25)
        self.input_lunghezza = QDoubleSpinBox()
        self.input_lunghezza.setMaximum(1000.0)
        self.input_larghezza = QDoubleSpinBox()
        self.input_larghezza.setMaximum(1000.0)
        self.input_profondita = QDoubleSpinBox()
        self.input_profondita.setMaximum(1000.0)
        self.input_peso = QDoubleSpinBox()
        self.input_peso.setMaximum(1000.0)
        self.input_note = QTextEdit()
        self.f_layout.addRow('Nome:', self.input_nome)
        self.f_layout.addRow('Prezzo:', self.input_prezzo)
        self.f_layout.addRow('Giacenza:', self.input_giacenza)
        self.f_layout.addRow('N. Scaffale:', self.input_numero_scaffale)
        self.f_layout.addRow('Livello:', self.input_livello)
        self.f_layout.addRow('Posizione:', self.input_posizione)
        self.f_layout.addRow('Lunghezza (cm):', self.input_lunghezza)
        self.f_layout.addRow('Larghezza (cm):', self.input_larghezza)
        self.f_layout.addRow('Profondità (cm):', self.input_profondita)
        self.f_layout.addRow('Peso (kg):', self.input_peso)
        self.f_layout.addRow('Note:', self.input_note)
        self.button_conferma = QPushButton('Conferma')
        self.button_conferma.clicked.connect(lambda: self.modifica_prodotto(id))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_conferma)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Modifica prodotto")
        self.setMinimumSize(QSize(400, 450))
        self.setMaximumHeight(450)

    def modifica_prodotto(self, id):
        nome = self.input_nome.text()
        prezzo = self.input_prezzo.value()
        giacenza = self.input_giacenza.value()
        numero_scaffale = self.input_numero_scaffale.value()
        livello = self.input_livello.value()
        posizione = self.input_posizione.value()
        ubicazione = Ubicazione(numero_scaffale, livello, posizione)
        lunghezza = self.input_lunghezza.value()
        larghezza = self.input_larghezza.value()
        profondita = self.input_profondita.value()
        peso = self.input_peso.value()
        dimensione = Dimensione(lunghezza, larghezza, profondita, peso)
        fornitore = Fornitore('Gianni srl', 131414132)
        note = self.input_note.toPlainText()
        nuovo_prodotto = Prodotto(GestoreMagazzino.get_prossimo_id_prodotto(), nome, giacenza, prezzo, ubicazione,
                                  dimensione, fornitore, note)
        GestoreMagazzino.modifica_prodotto(id, nuovo_prodotto)
        self.messaggio_conferma = VistaMessaggioGenerico(msg='Prodotto modificato con successo!')
        self.messaggio_conferma.show()
        self.close()
