import sys
import subprocess
from PyQt6 import QtWidgets, uic
import Code.startupwindow as startupwindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = startupwindow.startupwindow()
    window.show()
    sys.exit(app.exec())