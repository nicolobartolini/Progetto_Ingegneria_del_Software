from generali.Fornitore import Fornitore


class GestoreFornitori:
    collection_fornitori = None
    database_fornitori = []

    @staticmethod
    def aggiorna_database_gestore_fornitori():
        GestoreFornitori.database_fornitori = list(GestoreFornitori.collection_fornitori.find())

    @staticmethod
    def get_prossimo_id_fornitore():
        if len(GestoreFornitori.database_fornitori) != 0:
            GestoreFornitori.aggiorna_database_gestore_fornitori()
            return GestoreFornitori.database_fornitori[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_fornitore(fornitore: Fornitore):
        GestoreFornitori.collection_fornitori.insert_one({
            '_id': int(GestoreFornitori.get_prossimo_id_fornitore()),
            'marchionimo': fornitore.get_marchionimo(),
            'partitaIVA': int(fornitore.get_partitaIVA())
        })
        GestoreFornitori.aggiorna_database_gestore_fornitori()

    @staticmethod
    def rimuovi_fornitore(marchionimo: str):
        GestoreFornitori.collection_fornitori.delete_one({'marchionimo': str(marchionimo)})
        GestoreFornitori.aggiorna_database_gestore_fornitori()
