from PyQt4 import QtGui, uic
from sys import argv, exit
from random import randint

form_classes = uic.loadUiType('AC18VisualGame.ui')

OPERATIONS = [('sum', '+'), ('subt', '-'), ('mult', '*'), ('div', '/')]
DIFFICULTY = 20


class Game(*form_classes):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        # Randomly generates this turn's numbers
        self.ledit_1.setText(str(randint(0, DIFFICULTY)))
        self.ledit_2.setText(str(randint(0, DIFFICULTY)))

        # Event connection
        self.btn_new.clicked.connect(self.btn_newGame_clicked)
        self.btn_result.clicked.connect(self.btn_result_clicked)

        # Connecting QRadioButtons by their names
        for oper in OPERATIONS:
            getattr(self, 'rbtn_' + \
                    oper[0]).toggled.connect(self.btn_newGame_clicked)

        # This variable makes so that te user cant press the Result
        # button continuously and is forced to press the New Game button
        self.next = True

    def btn_newGame_clicked(self):
        self.next = True
        self.ledit_result.setText('')

        for oper in OPERATIONS:
            if getattr(self, 'rbtn_' + oper[0]).isChecked():
                self.label_op.setText(oper[1])

        a = randint(0, DIFFICULTY)
        b = randint(0, DIFFICULTY)

        # Divisions must be integers and numbers must be positive
        if oper[0] == 'div' and (b == 0 or b > a or a % b != 0):
            b = randint(1, DIFFICULTY)
            c = randint(0, DIFFICULTY)
            a = c * b

        elif oper[0] == 'subt' and b > a:
            a, b = b, a

        self.ledit_1.setText(str(a))
        self.ledit_2.setText(str(b))

    def btn_result_clicked(self):
        try:
            if not self.next:
                raise Warning('You must start a new game.')

            # Getting data from the interfaze
            a = int(self.ledit_1.text())
            b = int(self.ledit_2.text())

            operation = self.label_op.text()
            input = self.ledit_result.text()

            # check the existance of input
            if not input:
                raise ValueError('You must enter a number.')

            # check that the input is numerical
            if not input.isdigit():
                raise TypeError('Your answer must be a number.')

            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                result = a // b

            # Answer is verified
            if result == int(input):
                message = 'Correct!!'
            else:
                message = 'Incorrect :-(\n{0} {1} {2} = {3}'.format( \
                    a, operation, b, result)

        except Warning as err:
            QtGui.QMessageBox.about(self, ' ', '{}'.format(err))
        except TypeError as err:
            QtGui.QMessageBox.about(self, ' ', '{}'.format(err))
        except ValueError as err:
            QtGui.QMessageBox.about(self, ' ', '{}'.format(err))
        else:
            # Generates a message box to display the message
            QtGui.QMessageBox.about(self, ' ', message)
            self.next = False


if __name__ == '__main__':
    app = QtGui.QApplication(argv)
    MiJuego = Game()
    MiJuego.show()
    exit(app.exec_())
