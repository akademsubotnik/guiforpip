from PyQt6 import QtWidgets
import subprocess

class InstalledPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        
        # Installed Packages
        #Button - Installed Packages
        self.parent.pushButton_installedpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(2))
        self.parent.pushButton_installedpackages.clicked.connect(self.print_pippackages)
        #Button - Back
        self.parent.pushButton_back1.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))        
        self.parent.pushButton_back1.clicked.connect(self.back_button_click)


    def back_button_click(self):
        # Clear all items from the QListWidget
        self.parent.listWidget_installedpippackages.clear()


    def say_installedpackages(self):
        print("Installed Packages")
        self.print_pippackages


    def print_pippackages(self):
        try:
            # Run the pip list command
            result = subprocess.run(['pip3', 'list'], capture_output=True, text=True, check=True)
            packages = result.stdout.splitlines()
            # Print the output
            index = 0
            while index < len(packages):
                self.parent.listWidget_installedpippackages.addItem(packages[index])
                index = index + 1
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to list packages: {e}") 