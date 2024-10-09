import sys
import subprocess
from PyQt6 import QtWidgets, uic





#Main/StartUp Window
class startupwindow(QtWidgets.QDialog):
    def __init__(self):
        super(startupwindow, self).__init__()
        # Load the UI file
        uic.loadUi('pipuistartupwindow.ui', self)

        
        #Discover Packages
        #self.pushButton_discoverpackages.clicked.connect(self.say_discoverpackages)
        self.pushButton_discoverpackages.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_back2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))


        #Installed Packages
        #self.pushButton_installedpackages.clicked.connect(self.say_installedpackages)
        self.pushButton_installedpackages.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_back1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        #Software Updates
        #self.pushButton_softwareupdates.clicked.connect(self.say_softwareupdates)
        self.pushButton_softwareupdates.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_back3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))        



    def say_discoverpackages(self):
        print("Discover Packages")

    def say_softwareupdates(self):
        print("Software Updates")

    def say_installedpackages(self):
        print("Installed Packages")
        self.print_pippackages()

    def print_pippackages(self):
        # Run the pip list command
        result = subprocess.run(['pip3', 'list'], capture_output=True, text=True, check=True)
        # Print the output
        print(result.stdout)