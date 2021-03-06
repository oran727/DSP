# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtMultimedia import QSound


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(490, 380, 121, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 462, 121, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 380, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 420, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 460, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 510, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 540, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 510, 72, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 540, 72, 15))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 510, 91, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 540, 91, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(640, 510, 101, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(640, 540, 101, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(409, 83, 256, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(760, 60, 171, 19))
        self.checkBox_6.setObjectName("checkBox_6")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(750, 80, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 261, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.sound = QSound('noise/sound_Hnoise.wav', self)  # 1
        self.play_btn = QPushButton('pushButton', self)
        self.play_btn.clicked.connect(self.sound.play)  # 2

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 360, 241, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 421, 121, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(420, 60, 126, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setCheckable(True)
        self.fileOpenAction.setChecked(True)
        self.fileOpenAction.setEnabled(True)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.flieCloseAction = QtWidgets.QAction(MainWindow)
        self.flieCloseAction.setObjectName("flieCloseAction")
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.flieCloseAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.listWidget_2)
        MainWindow.setTabOrder(self.listWidget_2, self.checkBox_6)
        MainWindow.setTabOrder(self.checkBox_6, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.checkBox_4)
        MainWindow.setTabOrder(self.checkBox_4, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.checkBox_5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "Gpass"))
        self.label_3.setText(_translate("MainWindow", "Gstop"))
        self.label_4.setText(_translate("MainWindow", "fst1"))
        self.label_5.setText(_translate("MainWindow", "fst2"))
        self.label_6.setText(_translate("MainWindow", "fp1"))
        self.label_7.setText(_translate("MainWindow", "fp2"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "????????????I???"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "????????????II???"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "?????????"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox_6.setText(_translate("MainWindow", "??????FIR?????????"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "?????????"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "?????????"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "?????????"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "???????????????"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "?????????"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "????????????????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "???????????????????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "??????????????????"))
        self.checkBox.setText(_translate("MainWindow", "????????????"))
        self.checkBox_4.setText(_translate("MainWindow", "????????????"))
        self.checkBox_2.setText(_translate("MainWindow", "????????????"))
        self.checkBox_3.setText(_translate("MainWindow", "????????????"))
        self.checkBox_5.setText(_translate("MainWindow", "??????IIR?????????"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.fileOpenAction.setText(_translate("MainWindow", "??????????????????"))
        self.fileOpenAction.setToolTip(_translate("MainWindow", "??????"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.flieCloseAction.setText(_translate("MainWindow", "??????"))
        self.flieCloseAction.setToolTip(_translate("MainWindow", "??????"))
        self.flieCloseAction.setShortcut(_translate("MainWindow", "Alt+C"))




