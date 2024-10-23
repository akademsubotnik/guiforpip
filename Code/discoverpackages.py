from PyQt6 import QtWidgets
import webbrowser
import wget
import subprocess

class DiscoverPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Discover Packages
        self.parent.pushButton_discoverpackages.clicked.connect(self.say_discover_packages)
        self.parent.pushButton_discoverpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(1))
        #Back Button
        self.parent.pushButton_back2.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))
        self.parent.pushButton_back2.clicked.connect(self.back_button_click)


        self.parent.pushButton_pypi.clicked.connect(self.say_takemetopypi)
        self.parent.pushButton_packagesearch.clicked.connect(self.say_getvaluefromtextline)



    def say_discover_packages(self):
        print("Discover Packages")

    def say_takemetopypi(self):
        print("Take me to pypi")
        # Specify the URL you want to open
        url = 'https://pypi.org'
        # Open the URL in the default web browser
        webbrowser.open(url)

    def back_button_click(self):
        # Clear all items from the QListWidget
        self.parent.listWidget_foundpackages.clear()

    
    def say_getvaluefromtextline(self):
        print("Get value from text line")
        search_term = self.parent.lineEdit_pacakgesearch.text()
        url = 'https://pypi.org/simple/'

        command = f"wget -q -O - {url} | grep -i '{search_term}' | grep -oP '>(.*?)<' | sed 's/[><]//g' " 
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        # Print the output to on list widget
        try:
            # Run the pip list command
            packages = result.stdout.splitlines()
            if len(packages) > 50:
                size = 50
            else:
                size = len(packages)
            # Print the output
            index = 0
            while index < size:
                self.parent.listWidget_foundpackages.addItem(packages[index])
                index = index + 1
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to list packages: {e}") 
        

        #use the following to search for pacakges, where babel is the package being searched for
        #wget -qO- https://pypi.org/simple/ | grep -i 'babel' | grep -oP '>(.*?)<' | sed 's/[><]//g'