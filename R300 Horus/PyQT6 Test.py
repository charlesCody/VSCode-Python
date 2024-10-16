from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        
        self.toolbar = QToolBar("My main toolbar")
        self.addToolBar(self.toolbar)
        
        buttonAction = QAction("BUTTON", self)
        buttonAction.setStatusTip("This is a button")
        buttonAction.triggered.connect(self.buttonClicked)
        buttonAction.setCheckable(True)
        self.toolbar.addAction(buttonAction)
        
        self.setStatusBar(QStatusBar(self))
    def buttonClicked(self, s):
        print("click", s)
    
app = QApplication(sys.argv)
window = mainWindow()
window.show()

app.exec()