from Cliente import Cliente


class ClienteAzienda(Cliente):

    def __init__(self, id: int, indirizzo_email: str, telefono: str, id_documenti: list[int], marchionimo: str, partitaIVA: int):
        super().__init__(id, indirizzo_email, telefono, id_documenti)
        self.marchionimo = marchionimo
        self.partitaIVA = partitaIVA

    def get_marchionimo(self) -> str:
        return self.marchionimo

    def set_marchionimo(self, marchionimo: str):
        self.marchionimo = marchionimo

    def get_partitaIVA(self) -> int:
        return self.partitaIVA

    def set_partitaIVA(self, partitaIVA: int):
        self.partitaIVA = partitaIVA
