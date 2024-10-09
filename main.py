import sys
import subprocess
from PyQt6 import QtWidgets, uic
import startupwindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = startupwindow.startupwindow()
    window.show()
    sys.exit(app.exec())