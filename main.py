import sys

from PyQt5.QtWidgets import QApplication

from gestione.GestoreMagazzino import GestoreMagazzino
from viste.VistaLogin import VistaLogin

from pymongo import MongoClient

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_login = VistaLogin()
    client = MongoClient(
        "mongodb+srv://nick:1234@cluster0.y6icf.mongodb.net/?retryWrites=true&w=majority")
    db = client['progetto']
    GestoreMagazzino.collection_prodotti = db['prodotti']
    print(GestoreMagazzino.database_prodotti)
    GestoreMagazzino.aggiorna_database_prodotti()
    print(GestoreMagazzino.database_prodotti)
    vista_login.show()
    sys.exit(app.exec())

