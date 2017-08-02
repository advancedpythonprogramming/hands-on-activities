import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self, chat, name, signal):
        super(Example, self).__init__()
        self.chat = chat
        self.signal = signal
        self.name = name
        self.init_UI()

    def init_UI(self):
        self.signal.connect(self.set_photo)
        self.size = 400

        button = QtGui.QPushButton('Upload photo')
        button.setFixedSize(150, 50)
        button.clicked.connect(self.button_clicked)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)

        self.label = QtGui.QLabel(' ')
        self.label.setFixedSize(self.size, self.size)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(QtCore.QRectF(self.rect()).topLeft(),
                                         QtCore.QRectF(self.rect()).topRight())
        gradient.setColorAt(0, QtCore.Qt.green)
        gradient.setColorAt(0.5, QtCore.Qt.darkGreen)
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(gradient))
        self.setPalette(palette)

        self.setGeometry(0, 0, self.size, self.size)
        self.center_on_screen()
        self.setWindowTitle(self.name)
        self.show()

    def button_clicked(self):
        self.chat.path = QtGui.QFileDialog.getOpenFileName(self)
        if not self.chat.path == '':
            self.chat.pressed = True

    def center_on_screen(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - self.size / 2,
                  (resolution.height() / 2) - self.size / 2)

    def set_photo(self):
        self.myPixmap = QtGui.QPixmap(self.chat.get_path())
        self.label.setPixmap(self.myPixmap)
        self.label.setScaledContents(True)


class Chat(QtCore.QObject):
    signal = QtCore.pyqtSignal()

    def __init__(self, name):
        super(Chat, self).__init__()
        self.path = ''
        self.name = name
        self.pressed = False

    def init_UI(self):
        self.run()

    def run(self):
        app = QtGui.QApplication(sys.argv)
        self.ex = Example(self, self.name, self.signal)
        sys.exit(app.exec_())

    def get_path(self):
        return self.path

    def update_image(self, path):
        self.path = path
        self.signal.emit()

    def upload_pressed(self):
        if self.pressed:
            self.pressed = False
            return True
        return False
