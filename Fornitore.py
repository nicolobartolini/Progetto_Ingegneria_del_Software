class Fornitore:

    def __init__(self, marchionimo: str, partitaIVA: int):
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

