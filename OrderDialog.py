# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        OrderDialog.setObjectName("OrderDialog")
        OrderDialog.resize(394, 303)
        self.temp_label = QtWidgets.QLabel(OrderDialog)
        self.temp_label.setGeometry(QtCore.QRect(20, 10, 321, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.temp_label.setFont(font)
        self.temp_label.setObjectName("temp_label")
        self.edit_push_button = QtWidgets.QPushButton(OrderDialog)
        self.edit_push_button.setGeometry(QtCore.QRect(130, 250, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_push_button.setFont(font)
        self.edit_push_button.setObjectName("edit_push_button")

        self.retranslateUi(OrderDialog)
        QtCore.QMetaObject.connectSlotsByName(OrderDialog)

    def retranslateUi(self, OrderDialog):
        _translate = QtCore.QCoreApplication.translate
        OrderDialog.setWindowTitle(_translate("OrderDialog", "Dialog"))
        self.temp_label.setText(_translate("OrderDialog", "Номер:"))
        self.edit_push_button.setText(_translate("OrderDialog", "Редактировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderDialog = QtWidgets.QDialog()
    ui = Ui_OrderDialog()
    ui.setupUi(OrderDialog)
    OrderDialog.show()
    sys.exit(app.exec_())

