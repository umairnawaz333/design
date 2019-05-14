# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchase.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 434)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(550, 380))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.purchase_treeWidget = QtWidgets.QTreeWidget(self.frame_2)
        self.purchase_treeWidget.setObjectName("purchase_treeWidget")
        self.purchase_treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.purchase_treeWidget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 2, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.add_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_pushButton.setObjectName("add_pushButton")
        self.gridLayout_2.addWidget(self.add_pushButton, 0, 0, 1, 1)
        self.remove_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.remove_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.gridLayout_2.addWidget(self.remove_pushButton, 1, 0, 1, 1)
        self.update_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.update_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_pushButton.setObjectName("update_pushButton")
        self.gridLayout_2.addWidget(self.update_pushButton, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.submit_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.submit_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.gridLayout_3.addWidget(self.submit_pushButton, 0, 0, 1, 1)
        self.Cancel_purchase_Button = QtWidgets.QPushButton(self.frame_4)
        self.Cancel_purchase_Button.setObjectName("Cancel_purchase_Button")
        self.gridLayout_3.addWidget(self.Cancel_purchase_Button, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_pushButton.setText(_translate("Dialog", "ADD"))
        self.remove_pushButton.setText(_translate("Dialog", "Remove"))
        self.update_pushButton.setText(_translate("Dialog", "update"))
        self.submit_pushButton.setText(_translate("Dialog", "Submit"))
        self.Cancel_purchase_Button.setText(_translate("Dialog", "Cancel"))

