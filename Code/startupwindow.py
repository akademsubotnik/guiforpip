import sys
import subprocess
from PyQt6 import QtWidgets, uic
import Code.discoverpackages as discpackages #from Code.discoverpackages import say_discoverpackages, say_takemetopypi
import Code.installedpackages as instpackages #from Code.installedpackages import say_installedpackages, print_pippackages
from Code.softwareupdates import SoftwareUpdates #import Code.softwareupdates as swu #from Code.softwareupdates import say_softwareupdates

#Main/StartUp Window
class startupwindow(QtWidgets.QDialog):
    def __init__(self):
        super(startupwindow, self).__init__()
        # Load the UI file
        uic.loadUi('GUI/pipuistartupwindow.ui', self)

        # Set up the different functionalities
        self.discover_packages = DiscoverPackages(self)
        self.installed_packages = InstalledPackages(self)
        self.software_updates = SoftwareUpdates(self)
        
class DiscoverPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Discover Packages
        self.parent.pushButton_discoverpackages.clicked.connect(discpackages.say_discoverpackages)
        self.parent.pushButton_discoverpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(1))
        self.parent.pushButton_back2.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))
        # If "Take me to PyPI" button is pressed, open PyPI website
        self.parent.pushButton_pypi.clicked.connect(discpackages.say_takemetopypi)


class InstalledPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Installed Packages
        self.parent.pushButton_installedpackages.clicked.connect(instpackages.say_installedpackages)
        self.parent.pushButton_installedpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(2))
        self.parent.pushButton_back1.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))
