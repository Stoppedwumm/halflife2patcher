def GUIThread(data, lock):
    import os
    import PyQt6.QtWidgets as qtw
    import PyQt6.QtGui as qtg
    import PyQt6.QtCore as qtc
    # Installer window where you select a drive, and install
    class Window(qtw.QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Half Life 2 Patcher")
            # Set the size of the window
            self.setFixedSize(400, 200)
            self.layout = qtw.QVBoxLayout()
            self.setLayout(self.layout)

            self.label = qtw.QLabel("Half Life 2 Patcher")
            # Make text bigger
            self.label.setFont(qtg.QFont("Arial", 20))
            self.layout.addWidget(self.label)
            self.warning = qtw.QLabel("As of 2024, you need to enable in the properties of Half Life 2 the beta 'steam_legacy - Pre-20th Anniversary Build'.")
            # Make line breaks
            self.warning.setWordWrap(True)
            self.layout.addWidget(self.warning)
            self.dialog = qtw.QFileDialog(self)
            self.layout.addWidget(self.dialog)
            self.install = qtw.QPushButton("Install")
            self.layout.addWidget(self.install)
            # When button is pressed, print Hello World
            def Install():
                """
                When the install button is pressed, prompt the user to select a directory with a file dialog.
                The starting directory is the first existing directory of:
                ~/Library/Application Support/Steam/steamapps/
                ~/.steam/steam/steamapps/common/Half-Life 2
                Sets data["path"] to the selected directory and data["install"] to True.
                """
                with lock:
                    res = "~"
                    if os.path.isdir(os.path.expanduser("~/Library/Application Support/Steam/steamapps/common")):
                        
                        res = os.path.expanduser("~/Library/Application Support/Steam/steamapps/common")
                    elif os.path.isdir(os.path.expanduser("~/.steam/steam/steamapps/common/")):
                        res = os.path.expanduser("~/.steam/steam/steamapps/common/")
                    print(res)
                    data["path"] = self.dialog.getExistingDirectory(None, "Select HL2 install location", res)
                    data["install"] = True
                    print(data["path"])
            self.install.clicked.connect(Install)
        
            self.show()

    app = qtw.QApplication([])
    window = Window()
    app.exec()

if __name__ == "__main__":
    import threading
    GUIThread({}, threading.Lock())