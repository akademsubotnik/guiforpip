import sys
import subprocess
from PyQt6 import QtWidgets, uic
from Code.discoverpackages import DiscoverPackages #import Code.discoverpackages as discpackages #from Code.discoverpackages import say_discoverpackages, say_takemetopypi
from Code.installedpackages import InstalledPackages #import Code.installedpackages as instpackages #from Code.installedpackages import say_installedpackages, print_pippackages
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
