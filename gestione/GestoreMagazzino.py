import os
import pickle as pk

from Dimensione import Dimensione
from Fornitore import Fornitore
from Prodotto import Prodotto
from Ubicazione import Ubicazione


class GestoreMagazzino:

    collection_prodotti = None
    database_prodotti = []

    @staticmethod
    def aggiorna_database_prodotti():
        GestoreMagazzino.database_prodotti = list(GestoreMagazzino.collection_prodotti.find())

    @staticmethod
    def get_prossimo_id_prodotto():
        if len(GestoreMagazzino.database_prodotti) != 0:
            GestoreMagazzino.aggiorna_database_prodotti()
            return GestoreMagazzino.database_prodotti[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_prodotto(prodotto: Prodotto):
        GestoreMagazzino.collection_prodotti.insert_one({
            '_id': prodotto.get_id(),
            'nome': prodotto.get_nome(),
            'giacenza': prodotto.get_giacenza(),
            'prezzo': prodotto.get_prezzo(),
            'data_immagazzinamento': prodotto.get_data_immagazzinamento(),
            'ubicazione': {'numero_scaffale': prodotto.get_ubicazione().get_numero_scaffale(),
                           'livello': prodotto.get_ubicazione().get_livello(),
                           'posizione': prodotto.get_ubicazione().get_posizione()},
            'dimensione': {'lunghezza': prodotto.get_dimensione().get_lunghezza(),
                           'larghezza': prodotto.get_dimensione().get_larghezza(),
                           'profondita': prodotto.get_dimensione().get_profondita(),
                           'peso': prodotto.get_dimensione().get_peso()},
            'fornitore': {'marchionimo': prodotto.get_fornitore().get_marchionimo(),
                          'partitaIVA': prodotto.get_fornitore().get_partitaIVA()},
            'note': prodotto.get_note()
        })
        GestoreMagazzino.aggiorna_database_prodotti()

    @staticmethod
    def elimina_prodotto(id: int):
        GestoreMagazzino.aggiorna_database_prodotti()
        del GestoreMagazzino.database_prodotti[id]
        with open('dati/prodotti.pickle', 'wb') as f:
            pk.dump(GestoreMagazzino.database_prodotti, f, pk.HIGHEST_PROTOCOL)

    @staticmethod
    def aumenta_giacenza_prodotto(id: int, quantita: int):
        GestoreMagazzino.aggiorna_database_prodotti()
        prodotto = GestoreMagazzino.database_prodotti[id]
        prodotto.set_giacenza(prodotto.get_giacenza() + quantita)
        GestoreMagazzino.aggiungi_prodotto(prodotto)
        GestoreMagazzino.aggiorna_database_prodotti()

    @staticmethod
    def diminuisci_giacenza_prodotto(id: int, quantita: int):
        GestoreMagazzino.aggiorna_database_prodotti()
        prodotto = GestoreMagazzino.database_prodotti[id]
        prodotto.set_giacenza(prodotto.get_giacenza() - quantita)
        GestoreMagazzino.aggiungi_prodotto(prodotto)
        GestoreMagazzino.aggiorna_database_prodotti()

    @staticmethod
    def get_QR_prodotto(id: int):
        GestoreMagazzino.aggiorna_database_prodotti()
        prodotto_dict = {}
        for prodotto in GestoreMagazzino.database_prodotti:
            if prodotto['_id'] == id:
                prodotto_dict = prodotto
                break
        prodotto = GestoreMagazzino.get_oggetto_da_dict(prodotto_dict)
        return prodotto.creaQR()

    @staticmethod
    def modifica_prodotto(id_vecchio_prodotto: int, nuovo_prodotto: Prodotto):
        pass

    @staticmethod
    def get_oggetto_da_dict(prodotto_dict: dict):
        ubicazione = Ubicazione(prodotto_dict['ubicazione']['numero_scaffale'], prodotto_dict['ubicazione']['livello'], prodotto_dict['ubicazione']['posizione'])
        dimensione = Dimensione(prodotto_dict['dimensione']['lunghezza'], prodotto_dict['dimensione']['larghezza'], prodotto_dict['dimensione']['profondita'], prodotto_dict['dimensione']['peso'])
        fornitore = Fornitore('Gianni srl', 154891205)
        return Prodotto(prodotto_dict['_id'], prodotto_dict['nome'], prodotto_dict['giacenza'], prodotto_dict['prezzo'], ubicazione, dimensione, fornitore, prodotto_dict['note'])