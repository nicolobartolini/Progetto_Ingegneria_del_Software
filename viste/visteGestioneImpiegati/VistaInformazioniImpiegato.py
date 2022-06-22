from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QPushButton

from gestione.GestoreColorificio import GestoreColorificio
from viste.visteGestioneColorificio.VistaRimuoviVernice import VistaRimuoviVernice
from viste.visteGestioneImpiegati.VistaModificaImpiegato import VistaModificaImpiegato
from viste.visteGestioneImpiegati.VistaRimuoviImpiegato import VistaRimuoviImpiegato


class VistaInformazioniImpiegato(QWidget):

    def __init__(self, parent=None, impiegato: dict = None):
        super(VistaInformazioniImpiegato, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.f_layout = QFormLayout()
        self.label_nome = QLabel(impiegato['nome'])
        self.label_cognome = QLabel(impiegato['cognome'])
        self.label_nome_utente = QLabel(impiegato['_id'])
        self.label_password = QLabel(impiegato['password'])
        self.label_ruolo = QLabel(impiegato['ruolo'])
        self.f_layout.addRow('Nome:', self.label_nome)
        self.f_layout.addRow('Cognome:', self.label_cognome)
        self.f_layout.addRow('Nome utente:', self.label_nome_utente)
        self.f_layout.addRow('Password:', self.label_password)
        self.f_layout.addRow('Ruolo:', self.label_ruolo)
        self.button_modifica_impiegato = QPushButton('Modifica utente...')
        self.button_modifica_impiegato.clicked.connect(lambda: self.open_modifica_impiegato(impiegato['_id']))
        self.button_elimina_impiegato = QPushButton('Rimuovi utente...')
        self.button_elimina_impiegato.clicked.connect(lambda: self.open_elimina_impiegato(impiegato['_id']))
        self.v_layout.addLayout(self.f_layout)
        self.v_layout.addWidget(self.button_modifica_impiegato)
        self.v_layout.addWidget(self.button_elimina_impiegato)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli impiegato")
        self.setMinimumSize(QSize(250, 175))
        self.setMaximumHeight(175)

    def open_modifica_impiegato(self, nome_utente: str):
        self.vista_modifica_impiegato = VistaModificaImpiegato(nome_utente=nome_utente)
        self.vista_modifica_impiegato.show()

    def open_elimina_impiegato(self, nome_utente: str):
        self.vista_rimuovi_impiegato = VistaRimuoviImpiegato(nome_utente=nome_utente)
        self.vista_rimuovi_impiegato.show()
        self.close()