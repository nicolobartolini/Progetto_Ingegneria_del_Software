import datetime

import qrcode as qr

from Dimensione import Dimensione
from Fornitore import Fornitore
from Ubicazione import Ubicazione


class Prodotto():

    def __init__(self, id: int, nome: str,  giacenza: int, prezzo: float, ubicazione: Ubicazione, dimensione: Dimensione, fornitore: Fornitore, note: str):
        self.id = id
        self.nome = nome
        self.data_immagazzinamento = datetime.datetime.now()
        self.giacenza = giacenza
        self.prezzo = prezzo
        self.ubicazione = ubicazione
        self.dimensione = dimensione
        self.fornitore = fornitore
        self.note = note

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_data_immagazzinamento(self) -> datetime:
        return self.data_immagazzinamento

    def set_data_immagazzinamento(self, data_immagazzinamento: datetime):
        self.data_immagazzinamento = data_immagazzinamento

    def get_giacenza(self) -> int:
        return self.giacenza

    def set_giacenza(self, giacenza: int):
        self.giacenza = giacenza

    def get_prezzo(self) -> float:
        return self.prezzo

    def set_prezzo(self, prezzo: float):
        self.prezzo = prezzo

    def get_id(self) -> int:
        return self.id

    def get_note(self) -> str:
        return self.note

    def set_note(self, note: str):
        self.note = note

    def get_ubicazione(self) -> Ubicazione:
        return self.ubicazione

    def set_ubicazione(self, ubicazione: Ubicazione):
        self.ubicazione = ubicazione

    def get_dimensione(self) -> Dimensione:
        return self.dimensione

    def set_dimensione(self, dimensione: Dimensione):
        self.dimensione = dimensione

    def get_fornitore(self) -> Fornitore:
        return self.fornitore

    def set_fornitore(self, fornitore: Fornitore):
        self.fornitore = fornitore

    def creaQR(self):
        return qr.make(str(self.ubicazione))