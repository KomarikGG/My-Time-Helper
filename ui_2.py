# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 472)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(160, 270, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(-12)
        self.spinBox.setMaximum(12)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.time_country = QtWidgets.QPushButton(Form)
        self.time_country.setGeometry(QtCore.QRect(0, 400, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.time_country.setFont(font)
        self.time_country.setObjectName("time_country")
        self.number = QtWidgets.QLabel(Form)
        self.number.setGeometry(QtCore.QRect(70, 30, 341, 201))
        self.number.setStyleSheet("border: 5px solid;\n"
"border-radius: 25px;\n"
"font-size: 70px;\n"
"text-align: center;")
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setObjectName("number")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "World Time"))
        self.time_country.setText(_translate("Form", "Back"))
        self.number.setText(_translate("Form", "19:46"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
