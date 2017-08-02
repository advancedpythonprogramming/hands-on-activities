import sys
from PyQt4 import QtGui


class TicTacToe(QtGui.QWidget):
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        self.turn = 'X'
        self.button_dict = {}
        self.rep = [[], [], []]
        self.plays = 0
        self.end = False
        for i in range(3):
            for j in range(3):
                button = QtGui.QPushButton(' ')
                button.setFixedSize(50, 50)
                grid.addWidget(button, i, j)
                self.button_dict[button] = (i, j)
                self.rep[i].append(0)
                button.clicked.connect(self.buttonClicked)

        self.label = QtGui.QLabel('Player {} turn'.format(self.turn))
        grid.addWidget(self.label, 4, 0, 1, 4)
        self.setWindowTitle('TicTacToe')
        self.show()

    def buttonClicked(self):
        if not self.end:
            sender = self.sender()
            pos = self.button_dict[sender]
            val = self.rep[pos[0]][pos[1]]
            ant = self.turn
            if val == 0:
                self.plays += 1
                if self.turn == 'X':
                    sender.setText('X')
                    self.turn = 'O'
                    self.rep[pos[0]][pos[1]] = 1
                else:
                    sender.setText('O')
                    self.turn = 'X'
                    self.rep[pos[0]][pos[1]] = -1

                self.label.setText('Player {} turn'.format(self.turn))

                if self.check_winner(ant):
                    self.label.setText('Player {} wins!'.format(ant))
                    self.end = True

                elif self.plays == 9:
                    self.label.setText('Tie')
                    self.end = True

    def check_winner(self, turn):
        jug = 1 if turn == 'X' else -1
        rep = self.rep
        transposed = list(zip(*rep))

        # rows and columns
        for i in range(3):
            if len(set(rep[i])) == 1 and rep[i][0] == jug:
                return True
            if len(set(transposed[i])) == 1 and transposed[i][0] == jug:
                return True

        # diagonals
        diag1 = [rep[i][i] for i in range(3)]
        diag2 = [rep[i][2 - i] for i in range(3)]

        if diag1[0] == jug and len(set(diag1)) == 1:
            return True

        if diag2[0] == jug and len(set(diag2)) == 1:
            return True


def main():
    app = QtGui.QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
