import os
import pickle as pk

from Documento import Documento
from Vernice import Vernice
from gestione.GestoreClienti import GestoreClienti


class GestoreDocumenti:

    collection_documenti = None
    database_documenti = []

    @staticmethod
    def aggiorna_database_gestore_documenti():
        GestoreDocumenti.database_documenti = list(GestoreDocumenti.collection_documenti.find())

    @staticmethod
    def get_prossimo_id_documento():
        if len(GestoreDocumenti.database_documenti) != 0:
            GestoreDocumenti.aggiorna_database_gestore_documenti()
            return GestoreDocumenti.database_documenti[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_documento(documento: Documento):
        GestoreDocumenti.collection_documenti.insert_one({
            '_id': int(documento.get_id()),
            'tipo': str(documento.get_tipo_documento()),
            'nome': f'{documento.get_tipo_documento().capitalize()} {documento.get_id()}',
            'pagamento': str(documento.get_pagamento()),
            'id_prodotti': documento.get_id_prodotti(),
            'id_vernici': documento.get_id_vernici(),
            'id_cliente': documento.get_id_cliente()
        })
        GestoreClienti.aggiungi_documento_a_cliente(documento.get_id_cliente(), documento.get_id())

    @staticmethod
    def elimina_documento(id: int):
        GestoreDocumenti.collection_documenti.delete_one({'_id': id})
        GestoreDocumenti.aggiorna_database_gestore_documenti()

    @staticmethod
    def get_oggetto_da_dict(documento_dict: dict):
        return Documento(documento_dict['_id'], documento_dict['tipo'], documento_dict['id_prodotti'], documento_dict['id_vernici'], documento_dict['id_cliente'])
