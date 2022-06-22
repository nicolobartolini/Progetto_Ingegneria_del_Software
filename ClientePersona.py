from Cliente import Cliente


class ClientePersona(Cliente):

    def __init__(self, id: int, indirizzo_email: str, telefono: str, id_documenti: list[int], codice_fiscale: str,
                 cognome: str, nome: str):
        super().__init__(id, indirizzo_email, telefono, id_documenti)
        self.codice_fiscale = codice_fiscale
        self.cognome = cognome
        self.nome = nome

    def get_codice_fiscale(self) -> str:
        return self.codice_fiscale

    def get_cognome(self) -> str:
        return self.cognome

    def set_cognome(self, cognome: str):
        self.cognome = cognome

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome
