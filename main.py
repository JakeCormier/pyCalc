import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        grid = QGridLayout()
        results = QLineEdit()

        #creating the grid Layout
        buttons = ["AC", "C", "CE", "/",
                  7, 8, 9, "*",
                  1, 2, 3, "+",
                  0, ".", "="]

        row = 1
        column = 0

        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if column > 3:
                column = 0
                row += 1
            if button == 0:
                grid.addWidget(QPushButton(str(button)), row, column, 1, 2)
                column += 1
            else:
                grid.addWidget(QPushButton(str(button)), row, column, 1, 1)
            column += 1



        '''button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Last Button")

        grid.addWidget(button1, 0, 0, 1, 1)
        #row number column number row column
        grid.addWidget(button2, 0, 1, 1, 1)
        grid.addWidget(button3, 0, 2, 1, 1)
        grid.addWidget(button4, 1, 0, 1, 3)'''
        self.setLayout(grid)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())
