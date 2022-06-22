from unittest import TestCase

from magazzino.Ubicazione import Ubicazione


class TestUbicazione(TestCase):
    def test_str_ubicazione(self):
        ubicazione = Ubicazione(3, 1, 24)
        stringa_ubicazione_per_QR = 'Scaffale 3, livello 1, posizione 24'
        self.assertEquals(stringa_ubicazione_per_QR, str(ubicazione))
