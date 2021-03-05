# This is a simple calculator app built with PyQt5

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

# Set up GUI
class CalcUI(QMainWindow):
    def __init__(self):
        # Initialiser
        super().__init__()
        # Main window
        self.setWindowTitle('Calculator')
        self.setFixedSize(500, 500)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

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
