import sys

from PyQt5.QtWidgets import QApplication
from pymongo import MongoClient

from gestione.GestoreClienti import GestoreClienti
from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreDocumenti import GestoreDocumenti
from gestione.GestoreMagazzino import GestoreMagazzino
from viste.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_login = VistaLogin()
    client = MongoClient(
        "mongodb+srv://nick:1234@cluster0.y6icf.mongodb.net/?retryWrites=true&w=majority")
    db = client['progetto']
    GestoreMagazzino.collection_prodotti = db['prodotti']
    GestoreColorificio.collection_coloranti = db['coloranti']
    GestoreColorificio.collection_basi = db['basi']
    GestoreColorificio.collection_vernici = db['vernici']
    GestoreClienti.collection_clienti = db['clienti']
    GestoreDocumenti.collection_documenti = db['documenti']
    GestoreMagazzino.aggiorna_database_gestore_prodotti()
    GestoreColorificio.aggiorna_database_gestore_colorificio()
    GestoreColorificio.aggiorna_giacenza_coloranti()
    vista_login.show()
    sys.exit(app.exec())

