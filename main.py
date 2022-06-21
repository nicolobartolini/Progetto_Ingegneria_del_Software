import sys

from PyQt5.QtWidgets import QApplication

from viste.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_home = VistaLogin()
    vista_home.show()
    sys.exit(app.exec())
