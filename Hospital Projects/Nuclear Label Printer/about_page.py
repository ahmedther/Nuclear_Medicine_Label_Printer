# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_page(object):
    def setupUi(self, about_page):
        about_page.setObjectName("about_page")
        about_page.resize(586, 455)
        self.about_page_button = QtWidgets.QPushButton(about_page)
        self.about_page_button.setGeometry(QtCore.QRect(-10, -10, 623, 241))
        self.about_page_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imageResources/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.about_page_button.setIcon(icon)
        self.about_page_button.setIconSize(QtCore.QSize(611, 301))
        self.about_page_button.setObjectName("about_page_button")
        self.label_line_one = QtWidgets.QLabel(about_page)
        self.label_line_one.setGeometry(QtCore.QRect(-10, 240, 611, 24))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_line_one.setFont(font)
        self.label_line_one.setScaledContents(True)
        self.label_line_one.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line_one.setObjectName("label_line_one")
        self.label_line_one_2 = QtWidgets.QLabel(about_page)
        self.label_line_one_2.setGeometry(QtCore.QRect(0, 290, 611, 24))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_line_one_2.setFont(font)
        self.label_line_one_2.setScaledContents(True)
        self.label_line_one_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line_one_2.setObjectName("label_line_one_2")
        self.label_line_one_3 = QtWidgets.QLabel(about_page)
        self.label_line_one_3.setGeometry(QtCore.QRect(0, 320, 611, 24))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_line_one_3.setFont(font)
        self.label_line_one_3.setScaledContents(True)
        self.label_line_one_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line_one_3.setObjectName("label_line_one_3")
        self.label_line_one_4 = QtWidgets.QLabel(about_page)
        self.label_line_one_4.setGeometry(QtCore.QRect(0, 430, 611, 24))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_line_one_4.setFont(font)
        self.label_line_one_4.setScaledContents(True)
        self.label_line_one_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line_one_4.setObjectName("label_line_one_4")
        self.label_line_one_5 = QtWidgets.QLabel(about_page)
        self.label_line_one_5.setGeometry(QtCore.QRect(-10, 370, 611, 24))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_line_one_5.setFont(font)
        self.label_line_one_5.setScaledContents(True)
        self.label_line_one_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line_one_5.setObjectName("label_line_one_5")

        self.retranslateUi(about_page)
        QtCore.QMetaObject.connectSlotsByName(about_page)

    def retranslateUi(self, about_page):
        _translate = QtCore.QCoreApplication.translate
        about_page.setWindowTitle(_translate("about_page", "Dialog"))
        about_page.setWindowIcon(QtGui.QIcon('imageResources/logo.ico'))
        self.label_line_one.setText(_translate("about_page", "This Application is a property of Kokilaben Hospital"))
        self.label_line_one_2.setText(_translate("about_page", "Distribution of this Application outside of the"))
        self.label_line_one_3.setText(_translate("about_page", "hospital premises is strictly prohibited."))
        self.label_line_one_4.setText(_translate("about_page", "This programme was built and intended to be used by Nuclear Staff Only!!!"))
        self.label_line_one_5.setText(_translate("about_page", "Version 1.0"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     about_page = QtWidgets.QDialog()
#     ui = Ui_about_page()
#     ui.setupUi(about_page)
#     about_page.show()
#     sys.exit(app.exec_())