from colorificio.Base import Base
from colorificio.Colorante import Colorante
from generali.Fornitore import Fornitore


class GestoreColorificio:
    collection_coloranti = None
    collection_basi = None
    collection_vernici = None
    database_basi = []
    database_vernici = []

    prezzo_al_litro_coloranti = 7.5  # VEDIAMO
    colorante_rosso = None
    colorante_blu = None
    colorante_giallo = None

    @staticmethod
    def aggiorna_database_gestore_colorificio():
        GestoreColorificio.database_basi = list(GestoreColorificio.collection_basi.find())
        GestoreColorificio.database_vernici = list(GestoreColorificio.collection_vernici.find())

    @staticmethod
    def get_prossimo_id_base():
        if len(GestoreColorificio.database_basi) != 0:
            GestoreColorificio.aggiorna_database_gestore_colorificio()
            return GestoreColorificio.database_basi[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def get_prossimo_id_vernice():
        if len(GestoreColorificio.database_vernici) != 0:
            GestoreColorificio.aggiorna_database_gestore_colorificio()
            return GestoreColorificio.database_vernici[-1]['_id'] + 1
        else:
            return 1

    @staticmethod
    def aggiungi_base(base: Base):
        GestoreColorificio.collection_basi.insert_one({
            '_id': base.get_id(),
            'nome': base.get_nome(),
            'giacenza': base.get_giacenza(),
            'prezzo_al_litro': base.get_prezzo_al_litro(),
            'volume': base.get_volume(),
            'fornitore': {'marchionimo': base.get_fornitore().get_marchionimo(),
                          'partitaIVA': base.get_fornitore().get_partitaIVA()},
        })
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def aggiungi_vernice(vernice):
        GestoreColorificio.collection_vernici.insert_one({
            '_id': vernice.get_id(),
            'descrizione': vernice.get_descrizione(),
            'id_base': vernice.get_id_base(),
            'quantita_rosso': vernice.get_quantita_rosso(),
            'quantita_blu': vernice.get_quantita_blu(),
            'quantita_giallo': vernice.get_quantita_giallo(),
            'prezzo': vernice.get_prezzo()
        })
        GestoreColorificio.diminuisci_giacenza_base(vernice.get_id_base(), 1)
        GestoreColorificio.diminuisci_giacenza_colorante('rosso', vernice.get_quantita_rosso())
        GestoreColorificio.diminuisci_giacenza_colorante('blu', vernice.get_quantita_blu())
        GestoreColorificio.diminuisci_giacenza_colorante('giallo', vernice.get_quantita_giallo())
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def elimina_base(id: int):
        GestoreColorificio.collection_basi.delete_one({'_id': id})
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def rimuovi_vernice(id: int):
        GestoreColorificio.collection_vernici.delete_one({'_id': id})
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def diminuisci_giacenza_base(id: int, quantita: int):
        GestoreColorificio.collection_basi.update_one({'_id': id},
                                                      {'$inc': {'giacenza': -1 * quantita}})
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def modifica_base(id_vecchia_base: int, nuova_base: Base):
        GestoreColorificio.collection_basi.update_one({'_id': id_vecchia_base},
                                                      {'$set': {
                                                          'nome': nuova_base.get_nome(),
                                                          'giacenza': nuova_base.get_giacenza(),
                                                          'prezzo_al_litro': nuova_base.get_prezzo_al_litro(),
                                                          'volume': nuova_base.get_volume(),
                                                          'fornitore': {
                                                              'marchionimo': nuova_base.get_fornitore().get_marchionimo(),
                                                              'partitaIVA': nuova_base.get_fornitore().get_partitaIVA()},
                                                      }})
        GestoreColorificio.aggiorna_database_gestore_colorificio()

    @staticmethod
    def get_oggetto_da_dict(base_dict: dict):
        fornitore = Fornitore(base_dict['fornitore']['marchionimo'], base_dict['fornitore']['partitaIVA'])
        return Base(base_dict['_id'], base_dict['nome'], base_dict['giacenza'], base_dict['prezzo_al_litro'],
                    base_dict['volume'], fornitore)

    @staticmethod
    def ricerca_basi(parametro):
        risultato_ricerca = sorted(list(
            GestoreColorificio.collection_basi.find({'nome': {'$regex': f".*{parametro}.*", '$options': 'i'}})),
            key=lambda prodotto: prodotto['nome'], reverse=False)
        return risultato_ricerca

    @staticmethod
    def aggiorna_giacenza_coloranti():
        GestoreColorificio.colorante_rosso = Colorante('rosso', GestoreColorificio.collection_coloranti.find_one(
            {'colore': 'rosso'})['giacenza'])
        GestoreColorificio.colorante_blu = Colorante('blu', GestoreColorificio.collection_coloranti.find_one(
            {'colore': 'blu'})['giacenza'])
        GestoreColorificio.colorante_giallo = Colorante('giallo', GestoreColorificio.collection_coloranti.find_one(
            {'colore': 'giallo'})['giacenza'])

    @staticmethod
    def aggiorna_database_coloranti():
        GestoreColorificio.collection_coloranti.update_one({'colore': 'rosso'}, {
            '$set': {'giacenza': GestoreColorificio.colorante_rosso.get_giacenza_litri()}})
        GestoreColorificio.collection_coloranti.update_one({'colore': 'blu'}, {
            '$set': {'giacenza': GestoreColorificio.colorante_blu.get_giacenza_litri()}})
        GestoreColorificio.collection_coloranti.update_one({'colore': 'giallo'}, {
            '$set': {'giacenza': GestoreColorificio.colorante_giallo.get_giacenza_litri()}})

    @staticmethod
    def diminuisci_giacenza_colorante(colore, quantita):
        if colore == 'rosso':
            GestoreColorificio.colorante_rosso.set_giacenza_litri(
                GestoreColorificio.colorante_rosso.get_giacenza_litri() - quantita)
        elif colore == 'blu':
            GestoreColorificio.colorante_blu.set_giacenza_litri(
                GestoreColorificio.colorante_blu.get_giacenza_litri() - quantita)
        elif colore == 'giallo':
            GestoreColorificio.colorante_giallo.set_giacenza_litri(
                GestoreColorificio.colorante_giallo.get_giacenza_litri() - quantita)
        GestoreColorificio.aggiorna_database_coloranti()
