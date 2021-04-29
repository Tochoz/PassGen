import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QLineEdit, QDesktopWidget
from PyQt5 import QtCore, QtGui
import gen, base_relations


class RemindWindow(QWidget):
    h: int = 200
    w: int = 300
    coord = QtCore.QPoint()

    def __init__(self, width=300, height=80, coord=QtCore.QPoint()):
        super().__init__()

        self.h = height
        self.w = width
        self.coord = coord

        self.initUI()

    def initUI(self):
        self.move(self.coord.x() - self.w // 2, self.coord.y() - self.h // 2)
        self.setFixedSize(self.w, self.h)

        label = QLabel()
        label.setText("<b>Remind<b>")


class SaveWindow(QWidget):
    h: int = 200
    w: int = 300
    pas: str
    coord = QtCore.QPoint()

    def __init__(self, width=300, height=80, coord=QtCore.QPoint()):
        super().__init__()

        self.h = height
        self.w = width
        self.coord = coord

        self.initUI()

    def initUI(self):
        self.move(self.coord.x() - self.w // 2, self.coord.y() - self.h // 2)
        self.setFixedSize(self.w, self.h)

        self.setWindowTitle("Saving")

        l1 = QLabel("Enter the service (without spaces),\nwhat password refers to:")
        idlabel = QLabel(f"id: {str(base_relations.last_id() + 1).zfill(6)}")
        idlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignRight)
        self.resource = QLineEdit()
        btnsave = QPushButton("Apply")

        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()

        hLayout.addWidget(btnsave)
        hLayout.addWidget(idlabel)

        vLayout.addWidget(l1)
        vLayout.addWidget(self.resource)
        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)

        btnsave.clicked.connect(self.Apply_saving)

    def Apply_saving(self):
        if self.resource.text() != '':
            base_relations.add_pack([self.pas, self.resource.text()])
            QtCore.QCoreApplication.quit()


class CreateWindow(QWidget):
    h: int = 80
    w: int = 300
    coord = QtCore.QPoint()

    def __init__(self, width=300, height=80, coord=QtCore.QPoint()):
        super().__init__()

        self.h = height
        self.w = width
        self.coord = coord

        self.initUI()

    def initUI(self):
        self.move(self.coord.x() - self.w // 2, self.coord.y() - self.h // 2)
        self.setFixedSize(self.w, self.h)

        self.setWindowTitle("Generation menu")

        label = QLabel()
        label.setText('Press "Generate" to make new password\n '
                      'You also may save this password\ninto the base.')
        self.resultPSWRD = QLabel()
        self.resultPSWRD.setText("<i>Your generated password here...<i>")
        self.resultPSWRD.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        self.btnGenerate = QPushButton("Generate new")
        self.btnSave = QPushButton("Save")
        self.btnCopy = QPushButton("Copy")

        # Set frames to the right absolute position--------------
        main_horLayout = QHBoxLayout()
        locVLayout = QVBoxLayout()
        vbtnsLayout = QVBoxLayout()
        hbtnsLayout = QHBoxLayout()

        # Set right location-------------------------------------
        hbtnsLayout.addWidget(self.btnCopy)
        hbtnsLayout.addWidget(self.btnSave)

        locVLayout.addWidget(self.resultPSWRD)
        locVLayout.addLayout(vbtnsLayout)

        vbtnsLayout.addWidget(self.btnGenerate)
        vbtnsLayout.addLayout(hbtnsLayout)

        main_horLayout.addWidget(label)
        main_horLayout.addLayout(locVLayout)

        self.setLayout(main_horLayout)

        # --------------------------------------------------------
        self.btnGenerate.clicked.connect(self.Generation)
        self.btnCopy.clicked.connect(self.Copying)

    def Generation(self):
        self.resultPSWRD.setText(f"{gen.new_pass()}")

    def Copying(self):
        if self.resultPSWRD.text() != "<i>Your generated password here...<i>":
            cb = QtGui.QGuiApplication.clipboard()
            cb.clear(mode=QtGui.QClipboard.Clipboard)
            cb.setText(self.resultPSWRD.text(), mode=QtGui.QClipboard.Clipboard)


class IntroWindow(QWidget):
    w: int = 300
    h: int = 80

    def __init__(self, width=300, height=80):
        super().__init__()

        self.h = height
        self.w = width

        self.initUI()

    def initUI(self):
        screen = (QDesktopWidget().screenGeometry(-1).width(), QDesktopWidget().screenGeometry(-1).height())
        self.move(screen[0] // 2 - self.w // 2, screen[1] // 2 - self.h // 2)
        self.setFixedSize(self.w, self.h)

        self.setWindowTitle("Welcome")
        self.btn_remind = QPushButton("Remind me plz", self)
        self.btn_get_new = QPushButton("Get a new plz", self)

        self.label = QLabel(self)
        self.label.setText("What do you want?")
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignRight)

        # Set frames to the right absolute position--------------
        main_verticalLayout = QVBoxLayout()
        self.btnsLayout = QHBoxLayout()

        # Set component's locale---------------------------------
        self.btnsLayout.addWidget(self.btn_remind)
        self.btnsLayout.addWidget(self.btn_get_new)

        main_verticalLayout.addWidget(self.label)
        main_verticalLayout.addLayout(self.btnsLayout)

        self.setLayout(main_verticalLayout)
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dialog = IntroWindow(300, 80)
        pos = QtCore.QPoint(self.dialog.pos().x() + self.dialog.w // 2, self.dialog.pos().y() + self.dialog.h // 2)
        self.remindWindow = RemindWindow(400, 100, coord=pos)
        self.creationWindow = CreateWindow(400, 100, coord=pos)
        self.saveWindow = SaveWindow(250, 100, coord=pos)

        self.dialog.btn_remind.clicked.connect(self.show_remind)
        self.dialog.btn_get_new.clicked.connect(self.show_creation)
        self.creationWindow.btnSave.clicked.connect(self.show_saving)

    def show_remind(self):
        pos = QtCore.QPoint(self.dialog.pos().x() + self.dialog.w // 2,
                            self.dialog.pos().y() + self.dialog.h // 2)
        self.remindWindow.move(pos.x() - self.remindWindow.w // 2, pos.y() - self.remindWindow.h // 2)
        self.remindWindow.show()
        self.dialog.close()

    def show_creation(self):
        pos = QtCore.QPoint(self.dialog.pos().x() + self.dialog.w // 2,
                            self.dialog.pos().y() + self.dialog.h // 2)
        self.creationWindow.move(pos.x() - self.creationWindow.w // 2, pos.y() - self.creationWindow.h // 2)
        self.creationWindow.show()
        self.dialog.close()

    def show_saving(self):
        if self.creationWindow.resultPSWRD.text() != "<i>Your generated password here...<i>":
            self.saveWindow.pas = self.creationWindow.resultPSWRD.text()
            pos = QtCore.QPoint(self.creationWindow.pos().x() + self.creationWindow.w // 2,
                                self.creationWindow.pos().y() + self.creationWindow.h // 2)
            self.saveWindow.move(pos.x() - self.saveWindow.w // 2, pos.y() - self.saveWindow.h // 2)
            self.saveWindow.show()
            self.creationWindow.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
