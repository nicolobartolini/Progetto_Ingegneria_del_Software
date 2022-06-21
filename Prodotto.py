import datetime


class Prodotto():

    def __init__(self, nome: str,  giacenza: int, id: int, note: str, ubicazione: Ubicazione, dimensione: Dimensione, fornitore: Fornitore):
        self.nome = nome
        self.data_immagazzinamento = datetime.datetime.now()
        self.giacenza = giacenza
        self.id = id
        self.note = note
        self.ubicazione = ubicazione
        self.dimensione = dimensione
        self.fornitore = fornitore

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