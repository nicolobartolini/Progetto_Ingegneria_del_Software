import os
import pickle as pk

from Vernice import Vernice


class GestoreDocumenti:

    collection_documenti = None

    @staticmethod
    def aggiorna_storico():
        if os.path.isfile('dati/storico.pickle'):
            with open('dati/storico.pickle', 'rb') as f:
                GestoreVernici.storico_vernici = pk.load(f)

    @staticmethod
    def inserisci_vernice(vernice: Vernice):
        GestoreVernici.aggiorna_storico()
        GestoreVernici.storico_vernici[vernice.get_id()] = vernice
        with open('dati/storico.pickle', 'wb') as f:
            pk.dump(GestoreVernici.storico_vernici, f, pk.HIGHEST_PROTOCOL)

    @staticmethod
    def rimuovi_vernice(id: int):
        GestoreVernici.aggiorna_storico()
        del GestoreVernici.storico_vernici[id]
        with open('dati/storico.pickle', 'wb') as f:
            pk.dump(GestoreVernici.storico_vernici, f, pk.HIGHEST_PROTOCOL)

    @staticmethod
    def get_storico_vernici():
        GestoreVernici.aggiorna_storico()
        return GestoreVernici.storico_vernici
