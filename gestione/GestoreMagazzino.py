import os
import pickle as pk

from Prodotto import Prodotto


class GestoreMagazzino:

    database_prodotti = {}

    @staticmethod
    def aggiorna_database_prodotti():
        if os.path.isfile('dati/prodotti.pickle'):
            with open('dati/prodotti.pickle', 'rb') as f:
                GestoreMagazzino.database_prodotti = pk.load(f)

    @staticmethod
    def aggiungi_prodotto(prodotto: Prodotto):
        GestoreMagazzino.aggiorna_database_prodotti()
        GestoreMagazzino.database_prodotti[prodotto.get_id()] = prodotto
        with open('dati/prodotti.pickle', 'wb') as f:
            pk.dump(GestoreMagazzino.database_prodotti, f, pk.HIGHEST_PROTOCOL)

    @staticmethod
    def elimina_prodotto(id: int):
        GestoreMagazzino.aggiorna_database_prodotti()
        del GestoreMagazzino.database_prodotti[id]
        with open('dati/prodotti.pickle', 'wb') as f:
            pk.dump(GestoreMagazzino.database_prodotti, f, pk.HIGHEST_PROTOCOL)

    @staticmethod
    def get_lista_prodotti():
        GestoreMagazzino.aggiorna_database_prodotti()
        return GestoreMagazzino.database_prodotti

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
        prodotto = GestoreMagazzino.database_prodotti[id]
        qr = prodotto.crea_QR()
        return qr

    @staticmethod
    def modifica_prodotto(id_vecchio_prodotto: int, nuovo_prodotto: Prodotto):
        pass

