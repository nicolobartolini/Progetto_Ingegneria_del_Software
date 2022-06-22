from Documento import Documento
from Impiegato import Impiegato


class GestoreImpiegati:
    collection_impiegati = None
    database_impiegati = []

    @staticmethod
    def aggiorna_database_gestore_impiegati():
        GestoreImpiegati.database_impiegati = list(GestoreImpiegati.collection_impiegati.find())

    @staticmethod
    def get_prossimo_id_documento():
        if len(GestoreImpiegati.collection_impiegati) != 0:
            GestoreImpiegati.aggiorna_database_gestore_impiegati()
            return GestoreImpiegati.collection_impiegati[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_impiegato(impiegato: Impiegato):
        GestoreImpiegati.collection_impiegati.insert_one({
            '_id': str(impiegato.get_nome_utente()),
            'nome': str(impiegato.get_nome()),
            'cognome': str(impiegato.get_cognome()),
            'password': str(impiegato.get_password()),
            'ruolo': str(impiegato.get_ruolo())
        })

    @staticmethod
    def elimina_impiegato(nome_utente: str):
        GestoreImpiegati.collection_impiegati.delete_one({'_id': nome_utente})
        GestoreImpiegati.aggiorna_database_gestore_impiegati()

    @staticmethod
    def get_oggetto_da_dict(documento_dict: dict):
        return Documento(documento_dict['_id'], documento_dict['tipo'], documento_dict['id_prodotti'],
                         documento_dict['id_vernici'], documento_dict['id_cliente'])

    @staticmethod
    def modifica_impiegato(nome_utente, nuovo_impiegato):
        GestoreImpiegati.collection_impiegati.update_one({'_id': str(nome_utente)},
                                                         {'$set': {'_id': nuovo_impiegato.get_nome_utente(),
                                                                   'nome': nuovo_impiegato.get_nome(),
                                                                   'cognome': nuovo_impiegato.get_cognome(),
                                                                   'password': nuovo_impiegato.get_password(),
                                                                   'ruolo': nuovo_impiegato.get_ruolo()}})
        GestoreImpiegati.aggiorna_database_gestore_impiegati()
