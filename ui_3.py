# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_3.ui'
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
        self.second_time = QtWidgets.QPushButton(Form)
        self.second_time.setGeometry(QtCore.QRect(0, 400, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.second_time.setFont(font)
        self.second_time.setObjectName("second_time")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 80, 361, 131))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(210, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.setObjectName("start")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "StopWatch"))
        self.second_time.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "00:00.00"))
        self.start.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
