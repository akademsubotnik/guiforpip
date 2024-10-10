import sys
import subprocess
from PyQt6 import QtWidgets, uic
from Code.discoverpackages import say_discoverpackages
from Code.softwareupdates import say_softwareupdates


def say_installedpackages():
    print("Installed Packages")
    print_pippackages()


def print_pippackages():
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