from PyQt6 import QtWidgets
import subprocess

class SoftwareUpdates:
    def __init__(self,parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Software Updates
        self.parent.pushButton_softwareupdates.clicked.connect(self.say_software_updates)
        self.parent.pushButton_softwareupdates.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(3))


        self.parent.pushButton_back3.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))
        self.parent.pushButton_back3.clicked.connect(self.button_back_click)

        self.parent.pushButton_updateall.clicked.connect(self.button_updateall_click)



    def say_software_updates(self):
        print("Software Updates")
        try:
            # Run the pip list command
            result = subprocess.run(['pip3', 'list'], capture_output=True, text=True, check=True)
            packages = result.stdout.splitlines()
            # Print the output
            index = 0
            while index < len(packages):
                self.parent.listWidget_updatepippackages.addItem(packages[index])
                index = index + 1
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to list packages: {e}") 


    def button_back_click(self):
        # Clear all items from the QListWidget
        self.parent.listWidget_updatepippackages.clear()

    def button_updateall_click(self):
        print("Update all packages")
        # Get the list of installed packages
        result = subprocess.run(['pip3', 'freeze'], capture_output=True, text=True, check=True)

        # Split the output into lines
        packages = result.stdout.splitlines()

        # Upgrade each package
        for package in packages:
            package_name = package.split('==')[0]  # Get the package name without the version
            subprocess.run(['pip3', 'install', '--upgrade', package_name], check=True)