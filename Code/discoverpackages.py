from PyQt6 import QtWidgets
import webbrowser

class DiscoverPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Discover Packages
        self.parent.pushButton_discoverpackages.clicked.connect(self.say_discover_packages)
        self.parent.pushButton_discoverpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(1))
        self.parent.pushButton_back2.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))
        # If "Take me to PyPI" button is pressed, open PyPI website
        self.parent.pushButton_pypi.clicked.connect(self.say_takemetopypi)

    def say_discover_packages(self):
        print("Discover Packages")

    def say_takemetopypi(self):
        print("Take me to pypi")
        # Specify the URL you want to open
        url = 'https://pypi.org'
        # Open the URL in the default web browser
        webbrowser.open(url)