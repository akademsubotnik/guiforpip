class SoftwareUpdates:
    def __init__(self,parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Software Updates
        self.parent.pushButton_softwareupdates.clicked.connect(self.say_software_updates)
        self.parent.pushButton_softwareupdates.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(3))
        self.parent.pushButton_back3.clicked.connect(lambda: self.parent.stackedWidget.setCurrentIndex(0))

    def say_software_updates(self):
        print("Software Updates")