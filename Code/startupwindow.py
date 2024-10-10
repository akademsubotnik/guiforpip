import sys
import subprocess
from PyQt6 import QtWidgets, uic
import Code.discoverpackages as discpackages #from Code.discoverpackages import say_discoverpackages, say_takemetopypi
import Code.installedpackages as instpackages #from Code.installedpackages import say_installedpackages, print_pippackages
import Code.softwareupdates as swu #from Code.softwareupdates import say_softwareupdates


#Main/StartUp Window
class startupwindow(QtWidgets.QDialog):
    def __init__(self):
        super(startupwindow, self).__init__()
        # Load the UI file
        uic.loadUi('GUI/pipuistartupwindow.ui', self)

        # Set up the different functionalities
        self.setup_discover_packages()
        self.setup_installed_packages()
        self.setup_software_updates()
        
    def setup_discover_packages(self):
        # Discover Packages
        self.pushButton_discoverpackages.clicked.connect(discpackages.say_discoverpackages)
        self.pushButton_discoverpackages.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_back2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        # If "Take me to PyPI" button is pressed, open PyPI website
        self.pushButton_pypi.clicked.connect(discpackages.say_takemetopypi)

    def setup_installed_packages(self):
        # Installed Packages
        self.pushButton_installedpackages.clicked.connect(instpackages.say_installedpackages)
        self.pushButton_installedpackages.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_back1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def setup_software_updates(self):
        # Software Updates
        self.pushButton_softwareupdates.clicked.connect(swu.say_softwareupdates)
        self.pushButton_softwareupdates.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_back3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

