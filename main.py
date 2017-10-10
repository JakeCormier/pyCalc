import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "<-":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)
            #print("clicked", v)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        grid = QGridLayout()
        results = QLineEdit()

        #creating the grid Layout
        buttons = ["AC", "√", "<-", "/",
                  7, 8, 9, "*",
                  4, 5, 6, "-",
                  1, 2, 3, "+",
                  0, ".", "="]

        grid.addWidget(results, 0, 0, 1, 4)

        row = 1
        column = 0

        for button in buttons:
            if column > 3:
                column = 0
                row += 1

            buttonObj = Button(button, results)
            if button == 0:
                grid.addWidget(buttonObj.b, row, column, 1, 2)
                column += 1
            else:
                grid.addWidget(buttonObj.b, row, column, 1, 1)
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
