import sys
from PySide import QtCore, QtGui
from ui_main import Ui_Pictor


class Pictor(QtGui.QMainWindow):

    def __init__(self, parent):
        super(Pictor, self).__init__()
        self.ui = Ui_Pictor()
        self.ui.setupUi(self)
        self.signals()
        self.init_app()

    def signals(self):
        self.ui.add_picture.clicked.connect(self.add_picture)

    def init_app(self):
        self.browser()

    def browser(self, path=None):
        # if path is None:
        model = QtGui.QStandardItemModel()
        # model.setRootPath(QtCore.QDir.currentPath())
        self.ui.treeView.setModel(model)
        # self.ui.treeView.hideColumn(1)  # Size
        # self.ui.treeView.hideColumn(2)  # Type
        # self.ui.treeView.hideColumn(3)  # Date

    def add_picture(self):
        model = self.ui.treeView.model()
        child1 = QtGui.QStandardItem('Picture 1')
        child1.setIcon(QtGui.QIcon("statics/icons/picture.png"))
        model.appendRow(child1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pictor = Pictor(app)
    QtCore.QCoreApplication.setApplicationName("Pictor")
    pictor.show()
    code = app.exec_()
    sys.exit(code)
