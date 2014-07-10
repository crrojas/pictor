#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from PySide import QtCore, QtGui
import core
import processing
from ui_main import Ui_Pictor


class Pictor(QtGui.QMainWindow):

    def __init__(self, parent):
        super(Pictor, self).__init__()
        self.ui = Ui_Pictor()
        self.ui.setupUi(self)
        self.ui.thumbnails = list()
        self.signals()
        self.init_app()

    def signals(self):
        self.ui.add_picture.clicked.connect(self.open_file)
        self.ui.add_folder.clicked.connect(self.open_folder)

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

    def open_file(self):
        file_name = QtGui.QFileDialog.getOpenFileName(
            self, self.tr("Select a photo"),
            os.path.expanduser("~"), self.tr(
                "Image Files ({0})".format(core.formats())))
        if len(file_name[0]) > 0:  # Se ha seleccionado un archivo
            self.add_picture(file_name[0])

    def open_folder(self):
        folder_name = QtGui.QFileDialog.getExistingDirectory(self)
        self.add_folder(folder_name)

    def add_picture(self, path, parent=None):
        name_ext = os.path.basename(path)
        name, ext = os.path.splitext(name_ext)
        child = QtGui.QStandardItem(name)
        child.type_file = "picture"
        thumb = QtGui.QPixmap(processing.thumbnail(path))
        icon = QtGui.QIcon(thumb)
        self.ui.thumbnails.append(icon)
        child.setIcon(icon)
        if parent is None:
            model = self.ui.treeView.model()
            model.appendRow(child)
        else:
            parent.appendRow(child)

    def add_folder(self, path, parent=None):
        name = os.path.basename(path)
        child = QtGui.QStandardItem(name)
        child.type_file = "folder"
        child.setIcon(QtGui.QIcon("statics/icons/folder.png"))
        if parent is None:
            model = self.ui.treeView.model()
            model.appendRow(child)
        else:
            parent.appendRow(child)
        self.append_childs(path, child)

    def append_childs(self, folder_path, node):
        for arch in os.listdir(folder_path):
            path_arch = os.path.join(folder_path, arch)
            if os.path.isfile(path_arch):
                if processing.is_image(path_arch):
                    self.add_picture(path_arch, node)
            elif os.path.isdir(path_arch):
                self.add_folder(path_arch, node)
            else:
                pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pictor = Pictor(app)
    QtCore.QCoreApplication.setApplicationName("Pictor")
    pictor.show()
    code = app.exec_()
    sys.exit(code)
