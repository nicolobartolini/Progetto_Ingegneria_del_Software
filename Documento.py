import Prodotto


class Documento:

    def __init__(self, id: int, pagamento: float, tipo_documento: str, prodotti: list[Prodotto], vernici: list[Vernice], cliente: Cliente):
        self.data_emissione = datetime.datetime.now()
        self.id = id
        self.pagamento = pagamento # bisogna fare metodo che lo calcola in automatico
        self.tipo_documento = tipo_documento
        self.prodotti = prodotti
        self.vernici = vernici
        self.cliente = cliente

    def get_data_emissione(self) -> datetime:
        return self.data_emissione

    def get_tipo_documento(self) -> str:
        return self.tipo_documento

    def get_prodotti(self) -> list:
        return self.prodotti

    def set_prodotti(self, prodotti: list):
        self.prodotti = prodotti

    def get_vernici(self) -> list:
        return self.vernici

    def set_vernici(self, vernici: list):
        self.vernici = vernici

    def get_cliente(self) -> Cliente:
        return self.cliente
    