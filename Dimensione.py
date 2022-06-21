class Dimensione():

    def __init__(self, lunghezza: float, larghezza: float, profondita: float, peso: float):
        self.larghezza = larghezza
        self.lunghezza = lunghezza
        self.profondita = profondita
        self.peso = peso

    def get_larghezza(self) -> float:
        return self.larghezza

    def set_larghezza(self, larghezza: float):
        self.larghezza = larghezza

    def get_lunghezza(self) -> float:
        return self.lunghezza

    def set_lunghezza(self, lunghezza: float):
        self.lunghezza = lunghezza

    def get_profondita(self) -> float:
        return self.profondita

    def set_profondita(self, profondita: float):
        self.profondita = profondita

    def get_peso(self) -> float:
        return self.peso

    def set_peso(self, peso: float):
        self.peso = peso
