import webbrowser

def say_discoverpackages(self):
    print("Discover Packages")


def say_takemetopypi(self):
    print("Take me to pypi")
    # Specify the URL you want to open
    url = 'https://www.pypi.org'

    # Open the URL in the default web browser
    webbrowser.open(url)
