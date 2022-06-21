class Ubicazione():

    def __init__(self, livello: int, numero_scaffale: int, posizione: int):
        self.livello = livello
        self.numero_scaffale = numero_scaffale
        self.posizione = posizione

    def get_livello(self) -> int:
        return self.livello

    def set_livello(self, livello: int):
        self.livello = livello

    def get_numero_scaffale(self) -> int:
        return self.numero_scaffale

    def set_numero_scaffale(self, numero_scaffale: int):
        self.numero_scaffale = numero_scaffale

    def get_posizione(self) -> int:
        return self.posizione

    def set_posizione(self, posizione: int):
        self.posizione = posizione
