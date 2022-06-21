class Ubicazione():

    def __init__(self, numero_scaffale: int, livello: int, posizione: int):
        self.numero_scaffale = numero_scaffale
        self.livello = livello
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

    def __str__(self):
        return f'Scaffale {self.numero_scaffale}, livello {self.livello}, posizione {self.posizione}'
