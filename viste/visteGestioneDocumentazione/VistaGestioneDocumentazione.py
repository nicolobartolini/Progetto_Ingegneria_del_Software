from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout

from gestione.GestoreClienti import GestoreClienti
from gestione.GestoreColorificio import GestoreColorificio
from gestione.GestoreDocumenti import GestoreDocumenti
from viste.visteGestioneColorificio.VistaInformazioniVernice import VistaInformazioniVernice
from viste.visteGestioneColorificio.VistaInserisciVernice import VistaInserisciVernice
from viste.visteGestioneDocumentazione.VistaCreaFattura import VistaCreaFattura
from viste.visteGestioneDocumentazione.VistaCreaPreventivo import VistaCreaPreventivo
from viste.visteGestioneDocumentazione.VistaInformazioniDocumento import VistaInformazioniDocumento


class VistaGestioneDocumentazione(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneDocumentazione, self).__init__(parent)
        self.v_layout = QVBoxLayout()
        self.lista_documenti = QListWidget()
        GestoreDocumenti.aggiorna_database_gestore_documenti()
        self.set_lista_documenti(GestoreDocumenti.database_documenti)
        self.lista_documenti.itemActivated.connect(self.open_dettagli_documento)
        self.button_crea_fattura = QPushButton('Crea fattura...')
        self.button_crea_fattura.clicked.connect(self.open_crea_fattura)
        self.button_crea_preventivo = QPushButton('Crea preventivo...')
        self.button_crea_preventivo.clicked.connect(self.open_crea_preventivo)
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button_crea_fattura)
        self.h_layout.addWidget(self.button_crea_preventivo)
        self.v_layout.addWidget(self.lista_documenti)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Documentazione")
        self.setMinimumSize(700, 900)


    def open_crea_fattura(self):
        self.vista_crea_fattura = VistaCreaFattura()
        self.vista_crea_fattura.show()

    def open_crea_preventivo(self):
        self.vista_crea_preventivo = VistaCreaPreventivo()
        self.vista_crea_preventivo.show()

    def open_dettagli_documento(self, item):
        documento_dict = {}
        id_documento = int(item.text().split(' ')[0])
        for documento in GestoreDocumenti.database_documenti:
            if documento['_id'] == id_documento:
                documento_dict = documento
                break
        self.vista_informazioni_documento = VistaInformazioniDocumento(documento=documento_dict)
        self.vista_informazioni_documento.show()

    def set_lista_documenti(self, lista_documenti):
        self.lista_documenti.clear()
        if len(lista_documenti) != 0:
            for documento in lista_documenti:
                cliente = GestoreClienti.collection_clienti.find_one({'_id': documento['id_cliente']})
                if cliente is not None:
                    if cliente['tipo'] == 'persona':
                        nome_cliente = f"{cliente['nome']} {cliente['cognome']}"
                    else:
                        nome_cliente = cliente['marchionimo']
                else:
                    continue
                self.lista_documenti.addItem(
                    f'{str(documento["_id"])} | {str(documento["nome"])} | Cliente: {nome_cliente} | Pagamento: {documento["pagamento"]}')
