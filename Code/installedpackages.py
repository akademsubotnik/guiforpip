from PyQt6 import QtWidgets
import subprocess

class InstalledPackages:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Installed Packages
        self.parent.pushButton_installedpackages.clicked.connect(self.print_pippackages)
        self.parent.pushButton_installedpackages.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(2))
        self.parent.pushButton_back1.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))


    def say_installedpackages(self):
        print("Installed Packages")
        self.print_pippackages


    def print_pippackages(self):
        print("ECHOOOOOO")
        try:
            # Run the pip list command
            result = subprocess.run(['pip3', 'list'], capture_output=True, text=True, check=True)
            # Print the output
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to list packages: {e}") 

"""
(fstring)
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # Output: Hello, Alice!

"""