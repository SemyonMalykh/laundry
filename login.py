# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(294, 296)
        self.submit_button = QtWidgets.QPushButton(LoginDialog)
        self.submit_button.setGeometry(QtCore.QRect(120, 240, 75, 23))
        self.submit_button.setObjectName("submit_button")
        self.name_label = QtWidgets.QLabel(LoginDialog)
        self.name_label.setGeometry(QtCore.QRect(40, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.password = QtWidgets.QLineEdit(LoginDialog)
        self.password.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.password.setText("")
        self.password.setObjectName("password")
        self.name_edit = QtWidgets.QLineEdit(LoginDialog)
        self.name_edit.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.name_edit.setText("")
        self.name_edit.setObjectName("name_edit")
        self.pass_label = QtWidgets.QLabel(LoginDialog)
        self.pass_label.setGeometry(QtCore.QRect(40, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.pls_login_label = QtWidgets.QLabel(LoginDialog)
        self.pls_login_label.setGeometry(QtCore.QRect(50, 10, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pls_login_label.setFont(font)
        self.pls_login_label.setObjectName("pls_login_label")
        self.error_message_label = QtWidgets.QLabel(LoginDialog)
        self.error_message_label.setGeometry(QtCore.QRect(40, 210, 211, 20))
        self.error_message_label.setText("")
        self.error_message_label.setObjectName("error_message_label")
        self.second_name_edit = QtWidgets.QLineEdit(LoginDialog)
        self.second_name_edit.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.second_name_edit.setText("")
        self.second_name_edit.setObjectName("second_name_edit")
        self.second_name_label = QtWidgets.QLabel(LoginDialog)
        self.second_name_label.setGeometry(QtCore.QRect(40, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.second_name_label.setFont(font)
        self.second_name_label.setObjectName("second_name_label")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog"))
        self.submit_button.setText(_translate("LoginDialog", "Войти"))
        self.name_label.setText(_translate("LoginDialog", "Имя"))
        self.pass_label.setText(_translate("LoginDialog", "Пароль"))
        self.pls_login_label.setText(_translate("LoginDialog", "Войдите в систему"))
        self.second_name_label.setText(_translate("LoginDialog", "Фамилия"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())

