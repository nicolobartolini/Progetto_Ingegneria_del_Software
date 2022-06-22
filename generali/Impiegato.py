class Impiegato:

    def __init__(self, nome: str, cognome: str, nome_utente: str, password: str, ruolo: str):
        self.nome = nome
        self.cognome = cognome
        self.nome_utente = nome_utente
        self.password = password
        self.ruolo = ruolo

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_cognome(self) -> str:
        return self.cognome

    def set_cognome(self, cognome: str):
        self.cognome = cognome

    def get_nome_utente(self) -> str:
        return self.nome_utente

    def set_nome_utente(self, nome_utente: str):
        self.nome_utente = nome_utente

    def get_password(self) -> str:
        return self.password

    def set_password(self, password: str):
        self.password = password

    def get_ruolo(self) -> str:
        return self.ruolo

    def set_ruolo(self, ruolo: str):
        self.ruolo = ruolo
