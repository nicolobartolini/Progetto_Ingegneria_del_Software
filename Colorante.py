class Colorante:

    def __init__(self, colore: str, giacenza_litri: float):
        self.colore = colore
        self.giacenza_litri = giacenza_litri

    def get_colore(self) -> str:
        return self.colore

    def set_colore(self, colore: str):
        self.colore = colore

    def get_giacenza_litri(self) -> float:
        return self.giacenza_litri

    def set_giacenza_litri(self, giacenza_litri: float):
        self.giacenza_litri = giacenza_litri
