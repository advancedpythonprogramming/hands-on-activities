from PyQt4 import QtCore, QtGui
import datetime
import pickle
import os


class Cliente:
    def __init__(self, name, id, spent):
        self.name = name
        self.ID = id
        self.accumulated_spent = spent

    def __getstate__(self):
        new = self.__dict__.copy()
        new.update({'last_purchase': str(datetime.datetime)})
        return new

    def __setstate__(self, state):
        self.__dict__ = state

    def update_spent(self, spent):
        self.accumulated_spent += spent


class Cashier(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Cashier, self).__init__(parent)

        self.button_box = QtGui.QDialogButtonBox(self)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.client_label = QtGui.QLabel('client name', self)
        self.client_text = QtGui.QLineEdit(self)
        self.id_label = QtGui.QLabel('ID', self)
        self.id_text = QtGui.QLineEdit(self)
        self.spent_label = QtGui.QLabel('spent', self)
        self.spent_text = QtGui.QLineEdit(self)

        self.vertical_layout = QtGui.QVBoxLayout(self)
        self.vertical_layout.addWidget(self.client_label)
        self.vertical_layout.addWidget(self.client_text)
        self.vertical_layout.addWidget(self.id_label)
        self.vertical_layout.addWidget(self.id_text)
        self.vertical_layout.addWidget(self.spent_label)
        self.vertical_layout.addWidget(self.spent_text)
        self.vertical_layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.serialize_client)
        self.button_box.rejected.connect(self.close)

    def serialize_client(self):
        ###
        # To complete
        ###

        self.client_text.setText('')
        self.id_text.setText('')
        self.spent_text.setText('')


class Admin(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)

        self.file_button = QtGui.QPushButton('TOP')
        self.file_button.clicked.connect(self.create_file)

        self.cancel_button = QtGui.QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.close)

        self.horizontal_layout = QtGui.QVBoxLayout(self)
        self.horizontal_layout.addWidget(self.file_button)
        self.horizontal_layout.addWidget(self.cancel_button)

    def create_file(self):
        ###
        # To complete
        ###
        pass


class Input(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Input, self).__init__(parent)

        self.user_name_text = QtGui.QLineEdit(self)

        self.push_button_window = QtGui.QPushButton(self)
        self.push_button_window.setText('Log in')
        self.push_button_window.clicked.connect(
            self.on_push_button_clicked)

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.user_name_text)
        self.layout.addWidget(self.push_button_window)

    @QtCore.pyqtSlot()
    def on_push_button_clicked(self):
        #####
        # To complete
        ###
        pass


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Log-in WM')

    main = Input()
    main.show()

    sys.exit(app.exec_())
