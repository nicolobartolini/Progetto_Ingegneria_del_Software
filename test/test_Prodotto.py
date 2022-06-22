import os
from unittest import TestCase

from magazzino.Prodotto import Prodotto
from magazzino.Dimensione import Dimensione
from magazzino.Ubicazione import Ubicazione
from generali.Fornitore import Fornitore


class TestProdotto(TestCase):
    def setUp(self):
        self.prodotto = Prodotto(3, 'prodotto prova', 6, 3.99, Ubicazione(2, 1, 13), Dimensione(10, 10, 10, 10), Fornitore('fornitore di prova', 13131313), 'note di prova')

    def test_crea_qr(self):
        qr = self.prodotto.creaQR()
        qr.save('qr_test.png')
        self.assertTrue(os.path.isfile('qr_test.png'))
