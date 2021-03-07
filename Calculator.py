# This is a simple calculator app built with PyQt5

import sys
from functools import partial
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
            self.buttons[btext].setFixedSize(45, 40)
            buttonsLayout.addWidget(self.buttons[btext], pos[0], pos[1])
        # Add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.setDisplayText('')

# This control class connects GUI and model
class CalcControl:
    def __init__(self, model, view):
        # Initialiser
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()
    
    def _calculateResult(self):
        res = self._evaluate(exp=self._view.displayText())
        self._view.setDisplayText(res)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == "Error":
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp # Combine expressions
        self._view.setDisplayText(expression) # Set new display

    def _connectSignals(self):
        for btext, but in self._view.buttons.items():
            if btext not in {'=', 'C'}:
                but.clicked.connect(partial(self._buildExpression,btext))
        
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)

def evaluateExpression(exp):
    try:
        res = str(eval(exp, {}, {}))
    except Exception:
        res = "Error"

    return res

# Client
def main():
    # Create app
    calc = QApplication(sys.argv)
    # Show GUI UI
    view = CalcUI()
    view.show()
    # Create model and controller
    model = evaluateExpression
    CalcControl(model=model, view=view)
    # Execute
    sys.exit(calc.exec_())

if __name__ == '__main__':
    main()
