import Base
from gestione.GestoreColorificio import GestoreColorificio


class Vernice:
    
    def __init__(self, id: int, descrizione: str, base: Base, quantita_rosso: float, quantita_blu: float, quantita_giallo: float):
        self.id = id
        self.descrizione = descrizione
        self.base = base
        self.quantita_rosso = quantita_rosso
        self.quantita_blu = quantita_blu
        self.quantita_giallo = quantita_giallo
        self.prezzo = self.calcola_prezzo()

    def get_id(self) -> int:
        return self.id

    def get_descrizione(self) -> str:
        return self.descrizione

    def set_descrizione(self, descrizione: str):
        self.descrizione = descrizione

    def get_quantita_rosso(self) -> float:
        return self.quantita_rosso

    def get_quantita_blu(self) -> float:
        return self.quantita_blu

    def get_quantita_giallo(self) -> float:
        return self.quantita_giallo

    def get_prezzo(self) -> float:
        return self.prezzo

    def calcola_prezzo(self):
        return self.base.get_prezzo_al_litro() * self.base.get_volume() + (self.quantita_blu + self.quantita_giallo + self.quantita_rosso) * GestoreColorificio.get_prezzo_al_litro_coloranti()
