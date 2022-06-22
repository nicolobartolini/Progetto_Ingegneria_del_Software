from unittest import TestCase

from gestione.GestoreMagazzino import GestoreMagazzino
from magazzino.Prodotto import Prodotto


class TestGestoreMagazzino(TestCase):
    def test_get_oggetto_da_dict(self):
        prodotto_dict = {
            '_id': 1,
            'nome': 'prodotto di prova',
            'giacenza': 5,
            'prezzo': 3.99,
            'ubicazione': {
                'numero_scaffale': 3,
                'livello': 2,
                'posizione': 15
            },
            'dimensione': {
                'lunghezza': 10.0,
                'larghezza': 10.0,
                'profondita': 10.0,
                'peso': 10.0,
            },
            'fornitore': {
                'marchionimo': 'fornitore di prova',
                'partitaIVA': 123456789
            },
            'note': 'note di prova'
        }
        self.assertIsInstance(GestoreMagazzino.get_oggetto_da_dict(prodotto_dict), Prodotto)
