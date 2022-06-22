from Cliente import Cliente
from ClienteAzienda import ClienteAzienda
from ClientePersona import ClientePersona
from Dimensione import Dimensione
from Fornitore import Fornitore
from Prodotto import Prodotto
from Ubicazione import Ubicazione


class GestoreClienti:
    collection_clienti = None
    database_clienti = []

    @staticmethod
    def aggiorna_database_gestore_clienti():
        GestoreClienti.database_clienti = list(GestoreClienti.collection_clienti.find())

    @staticmethod
    def get_prossimo_id_cliente():
        if len(GestoreClienti.database_clienti) != 0:
            GestoreClienti.aggiorna_database_gestore_clienti()
            return GestoreClienti.database_clienti[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_cliente_persona(cliente: ClientePersona):
        GestoreClienti.collection_clienti.insert_one({
            '_id': cliente.get_id(),
            'tipo': 'persona',
            'nome': cliente.get_nome(),
            'cognome': cliente.get_cognome(),
            'codice_fiscale': cliente.get_codice_fiscale(),
            'indirizzo_email': cliente.get_indirizzo_email(),
            'telefono': cliente.get_telefono(),
            'documenti': cliente.get_documenti()
        })
        GestoreClienti.aggiorna_database_gestore_clienti()

    @staticmethod
    def aggiungi_cliente_azienda(cliente: ClienteAzienda):
        GestoreClienti.collection_clienti.insert_one({
            '_id': cliente.get_id(),
            'tipo': 'azienda',
            'marchionimo': cliente.get_marchionimo(),
            'partitaIVA': cliente.get_partitaIVA(),
            'indirizzo_email': cliente.get_indirizzo_email(),
            'telefono': cliente.get_telefono(),
            'documenti': cliente.get_documenti()
        })
        GestoreClienti.aggiorna_database_gestore_clienti()

    @staticmethod
    def elimina_cliente(id: int):
        GestoreClienti.collection_clienti.delete_one({'_id': id})
        GestoreClienti.aggiorna_database_gestore_clienti()

    @staticmethod
    def modifica_cliente_persona(id_vecchio_cliente: int, nuovo_cliente: ClientePersona):
        GestoreClienti.collection_clienti.update_one({'_id': id_vecchio_cliente},
                                                     {'$set': {'nome': nuovo_cliente.get_nome(),
                                                               'cognome': nuovo_cliente.get_cognome(),
                                                               'codice_fiscale': nuovo_cliente.get_codice_fiscale(),
                                                               'indirizzo_email': nuovo_cliente.get_indirizzo_email(),
                                                               'telefono': nuovo_cliente.get_telefono(),
                                                               }})
        GestoreClienti.aggiorna_database_gestore_clienti()

    @staticmethod
    def modifica_cliente_azienda(id_vecchio_cliente: int, nuovo_cliente: ClienteAzienda):
        GestoreClienti.collection_clienti.update_one({'_id': id_vecchio_cliente},
                                                     {'$set': {'marchionimo': nuovo_cliente.get_marchionimo(),
                                                               'partitaIVA': nuovo_cliente.get_partitaIVA(),
                                                               'indirizzo_email': nuovo_cliente.get_indirizzo_email(),
                                                               'telefono': nuovo_cliente.get_telefono(),
                                                               }})
        GestoreClienti.aggiorna_database_gestore_clienti()

    @staticmethod
    def get_oggetto_da_dict(cliente_dict: dict):
        if cliente_dict['tipo'] == 'persona':
            return ClientePersona(cliente_dict['_id'], cliente_dict['indirizzo_email'], cliente_dict['telefono'],
                                  cliente_dict['id_documenti'], cliente_dict['codice_fiscale'], cliente_dict['cognome'],
                                  cliente_dict['nome'])
        elif cliente_dict['tipo'] == 'azienda':
            return ClienteAzienda(cliente_dict['_id'], cliente_dict['indirizzo_email'], cliente_dict['telefono'],
                                  cliente_dict['id_documenti'], cliente_dict['marchionimo'], cliente_dict['partitaIVA'])

    @staticmethod
    def ricerca_ordina_clienti(tipo, parametro):
        if tipo == 'cognome':
            risultato_persone = sorted(list(
                GestoreClienti.collection_clienti.find({tipo: {'$regex': f".*{parametro}.*", '$options': 'i'}})),
                key=lambda prodotto: prodotto[tipo], reverse=False)
            risultato_aziende = sorted(list(
                GestoreClienti.collection_clienti.find(
                    {'marchionimo': {'$regex': f".*{parametro}.*", '$options': 'i'}})),
                key=lambda prodotto: prodotto['marchionimo'], reverse=False)
            risultato = risultato_persone + risultato_aziende
            return risultato
        elif tipo == 'cf':
            risultato_persone = sorted(list(
                GestoreClienti.collection_clienti.find(
                    {'codice_fiscale': {'$regex': f".*{parametro}.*", '$options': 'i'}})),
                key=lambda prodotto: prodotto['codice_fiscale'], reverse=False)
            risultato_aziende = sorted(list(
                GestoreClienti.collection_clienti.find(
                    {'partitaIVA': parametro})),
                key=lambda prodotto: prodotto['partitaIVA'], reverse=False)
            risultato = risultato_persone + risultato_aziende
            return risultato
