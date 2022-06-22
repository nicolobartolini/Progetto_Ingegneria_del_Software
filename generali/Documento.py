import datetime

from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreMagazzino import GestoreMagazzino


class Documento:

    def __init__(self, id: int, tipo_documento: str, id_prodotti: list[int], id_vernici: list[int], id_cliente):
        self.data_emissione = datetime.datetime.now()
        self.id = id
        self.tipo_documento = tipo_documento
        self.id_prodotti = id_prodotti
        self.id_vernici = id_vernici
        self.id_cliente = id_cliente
        self.pagamento = self.calcola_pagamento()

    def get_id(self) -> int:
        return self.id

    def get_data_emissione(self) -> datetime:
        return self.data_emissione

    def get_tipo_documento(self) -> str:
        return self.tipo_documento

    def get_pagamento(self) -> float:
        return self.pagamento

    def get_id_prodotti(self) -> list:
        return self.id_prodotti

    def set_id_prodotti(self, id_prodotti: list):
        self.id_prodotti = id_prodotti

    def get_id_vernici(self) -> list:
        return self.id_vernici

    def set_id_vernici(self, id_vernici: list):
        self.id_vernici = id_vernici

    def get_id_cliente(self) -> int:
        return self.id_cliente

    def calcola_pagamento(self):
        pagamento_prodotti = 0.0
        print(len(self.id_prodotti))
        if len(self.id_prodotti) != 0:
            for id_prodotto in self.id_prodotti:
                prodotto = GestoreMagazzino.collection_prodotti.find_one({'_id': id_prodotto})
                if prodotto is not None:
                    prezzo = prodotto['prezzo']
                else:
                    prezzo = 0.0
                pagamento_prodotti += prezzo
        pagamento_vernici = 0.0
        if len(self.id_vernici) != 0:
            for id_vernice in self.id_vernici:
                vernice = GestoreColorificio.collection_vernici.find_one({'_id': id_vernice})
                if vernice is not None:
                    prezzo = vernice['prezzo']
                else:
                    prezzo = 0.0
                pagamento_vernici += prezzo
        return pagamento_prodotti + pagamento_vernici
