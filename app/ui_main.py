# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Jul  6 21:06:01 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Pictor(object):
    def setupUi(self, Pictor):
        Pictor.setObjectName("Pictor")
        Pictor.resize(716, 531)
        self.centralwidget = QtGui.QWidget(Pictor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browser = QtGui.QWidget(self.centralwidget)
        self.browser.setMaximumSize(QtCore.QSize(300, 16777215))
        self.browser.setObjectName("browser")
        self.verticalLayout = QtGui.QVBoxLayout(self.browser)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtGui.QWidget(self.browser)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_picture = QtGui.QPushButton(self.widget_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("statics/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_picture.setIcon(icon)
        self.add_picture.setObjectName("add_picture")
        self.horizontalLayout_2.addWidget(self.add_picture)
        self.add_folder = QtGui.QPushButton(self.widget_3)
        self.add_folder.setIcon(icon)
        self.add_folder.setObjectName("add_folder")
        self.horizontalLayout_2.addWidget(self.add_folder)
        self.verticalLayout.addWidget(self.widget_3)
        self.treeView = QtGui.QTreeView(self.browser)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout.addWidget(self.browser)
        self.images = QtGui.QWidget(self.centralwidget)
        self.images.setMinimumSize(QtCore.QSize(400, 0))
        self.images.setObjectName("images")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.images)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.images)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.images)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.images)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        Pictor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Pictor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 25))
        self.menubar.setObjectName("menubar")
        Pictor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Pictor)
        self.statusbar.setObjectName("statusbar")
        Pictor.setStatusBar(self.statusbar)

        self.retranslateUi(Pictor)
        QtCore.QMetaObject.connectSlotsByName(Pictor)

    def retranslateUi(self, Pictor):
        Pictor.setWindowTitle(QtGui.QApplication.translate("Pictor", "Pictor", None, QtGui.QApplication.UnicodeUTF8))
        self.add_picture.setText(QtGui.QApplication.translate("Pictor", "Picture", None, QtGui.QApplication.UnicodeUTF8))
        self.add_folder.setText(QtGui.QApplication.translate("Pictor", "Folder", None, QtGui.QApplication.UnicodeUTF8))

