# This is a simple calculator app built with PyQt5

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout # Arrange buttons
from PyQt5.QtWidgets import QLineEdit # Display
from PyQt5.QtWidgets import QPushButton # Buttons
from PyQt5.QtWidgets import QVBoxLayout # General layout

# Set up GUI
class CalcUI(QMainWindow):
    def __init__(self):
        # Initialiser
        super().__init__()
        # Main window properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)
        # Set central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create display and buttons
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        # Create display widget
        self.display = QLineEdit()
        # Set display properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text : position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create buttons and add them to grid layout
        for btext, pos in buttons.items():
            self.buttons[btext] = QPushButton(btext)
            self.buttons[btext].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btext], pos[0], pos[1])
        # Add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)

        def setDisplayText(self, text):
            self.display.setText()
            self.display.setFocus()
        
        def getDisplayText(self):
            return self.display.text()
        
        def clearDisplay(self):
            self.setDisplayText('')


# Client
def main():
    # Create app
    calc = QApplication(sys.argv)
    # Show GUI UI
    view = CalcUI()
    view.show()
    # Execute
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()
