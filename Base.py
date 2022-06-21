from Fornitore import Fornitore


class Base:

    def __init__(self, id: int, nome: str, giacenza: int, prezzo_al_litro: float, volume: float, fornitore: Fornitore):
        self.id = id
        self.giacenza = giacenza
        self.nome = nome
        self.prezzo_al_litro = prezzo_al_litro
        self.volume = volume
        self.fornitore = fornitore

    def get_id(self) -> int:
        return self.id

    def get_giacenza(self) -> int:
        return self.giacenza

    def set_giacenza(self, giacenza: int):
        self.giacenza = giacenza

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_prezzo_al_litro(self) -> float:
        return self.prezzo_al_litro

    def set_prezzo_al_litro(self, prezzo_al_litro: float):
        self.prezzo_al_litro = prezzo_al_litro

    def get_volume(self) -> float:
        return self.volume

    def set_volume(self, volume: float):
        self.volume = volume

    def get_fornitore(self) -> Fornitore:
        return self.fornitore
    