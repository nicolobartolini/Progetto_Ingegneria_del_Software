from unittest import TestCase

from clientela.Cliente import Cliente


class TestCliente(TestCase):
    def setUp(self):
        self.cliente_senza_documenti = Cliente(3, 'prova@example.com', '123456789', [])
        self.cliente_con_documenti = Cliente(3, 'prova@example.com', '123456789', [4, 7])

    def test_lista_vuota(self):
        self.assertEqual(len(self.cliente_senza_documenti.get_id_documenti()), 0)

    def test_lista_non_vuota(self):
        self.assertEqual(len(self.cliente_con_documenti.get_id_documenti()), 2)
