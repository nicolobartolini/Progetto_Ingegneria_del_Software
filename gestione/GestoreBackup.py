import json

from gestione.GestoreClienti import GestoreClienti
from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreDocumenti import GestoreDocumenti
from gestione.GestoreMagazzino import GestoreMagazzino
from viste.VistaMessaggioGenerico import VistaMessaggioGenerico


class GestoreBackup:

    @staticmethod
    def effettua_backup():
        with open('backup/prodotti.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_prodotti(), f)
        with open('backup/basi.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_basi(), f)
        with open('backup/coloranti.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_coloranti(), f)
        with open('backup/vernici.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_vernici(), f)
        with open('backup/clienti.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_clienti(), f)
        with open('backup/documenti.json', 'w') as f:
            json.dump(GestoreBackup.get_dati_documenti(), f)
        VistaMessaggioGenerico(msg='Backup completato').show()

    @staticmethod
    def get_dati_prodotti():
        GestoreMagazzino.aggiorna_database_gestore_prodotti()
        return GestoreMagazzino.database_prodotti

    @staticmethod
    def get_dati_basi():
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        return GestoreColorificio.database_basi

    @staticmethod
    def get_dati_coloranti():
        GestoreColorificio.aggiorna_database_coloranti()
        return GestoreColorificio.collection_coloranti.find()

    @staticmethod
    def get_dati_vernici():
        GestoreColorificio.aggiorna_database_gestore_colorificio()
        return GestoreColorificio.database_vernici

    @staticmethod
    def get_dati_clienti():
        GestoreClienti.aggiorna_database_gestore_clienti()
        return GestoreClienti.database_clienti

    @staticmethod
    def get_dati_documenti():
        GestoreDocumenti.aggiorna_database_gestore_documenti()
        return GestoreDocumenti.database_documenti
