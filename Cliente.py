class Cliente:

    def __init__(self, id: int, indirizzo_email: str, telefono: str, id_documenti: list[int]):
        self.id = id
        self.indirizzo_email = indirizzo_email
        self.telefono = telefono
        self.id_documenti = id_documenti

    def get_id(self) -> int:
        return self.id

    def get_indirizzo_email(self) -> str:
        return self.indirizzo_email

    def set_indirizzo_email(self, indirizzo_email: str):
        self.indirizzo_email = indirizzo_email

    def get_telefono(self) -> str:
        return self.telefono

    def set_telefono(self, telefono: str):
        self.telefono = telefono

    def get_documenti(self) -> list[int]:
        return self.id_documenti

    def set_documenti(self, documenti: list[int]):
        self.id_documenti = documenti
