# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newOrderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewOrderDialog(object):
    def setupUi(self, NewOrderDialog):
        NewOrderDialog.setObjectName("NewOrderDialog")
        NewOrderDialog.resize(336, 314)
        self.first_name_label = QtWidgets.QLabel(NewOrderDialog)
        self.first_name_label.setGeometry(QtCore.QRect(40, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name_label.setFont(font)
        self.first_name_label.setObjectName("first_name_label")
        self.date_order_label = QtWidgets.QLabel(NewOrderDialog)
        self.date_order_label.setGeometry(QtCore.QRect(40, 60, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_order_label.setFont(font)
        self.date_order_label.setObjectName("date_order_label")
        self.cost_label = QtWidgets.QLabel(NewOrderDialog)
        self.cost_label.setGeometry(QtCore.QRect(40, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cost_label.setFont(font)
        self.cost_label.setObjectName("cost_label")
        self.is_payed_check_box = QtWidgets.QCheckBox(NewOrderDialog)
        self.is_payed_check_box.setGeometry(QtCore.QRect(140, 120, 16, 17))
        self.is_payed_check_box.setText("")
        self.is_payed_check_box.setObjectName("is_payed_check_box")
        self.phone_label = QtWidgets.QLabel(NewOrderDialog)
        self.phone_label.setGeometry(QtCore.QRect(40, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.first_name_edit = QtWidgets.QLineEdit(NewOrderDialog)
        self.first_name_edit.setGeometry(QtCore.QRect(140, 150, 151, 20))
        self.first_name_edit.setObjectName("first_name_edit")
        self.second_name_label = QtWidgets.QLabel(NewOrderDialog)
        self.second_name_label.setGeometry(QtCore.QRect(40, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.second_name_label.setFont(font)
        self.second_name_label.setObjectName("second_name_label")
        self.id_payd_label = QtWidgets.QLabel(NewOrderDialog)
        self.id_payd_label.setGeometry(QtCore.QRect(40, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_payd_label.setFont(font)
        self.id_payd_label.setObjectName("id_payd_label")
        self.cost_edit = QtWidgets.QLineEdit(NewOrderDialog)
        self.cost_edit.setGeometry(QtCore.QRect(140, 90, 151, 20))
        self.cost_edit.setObjectName("cost_edit")
        self.second_name_edit = QtWidgets.QLineEdit(NewOrderDialog)
        self.second_name_edit.setGeometry(QtCore.QRect(140, 180, 151, 20))
        self.second_name_edit.setObjectName("second_name_edit")
        self.date_order_label_2 = QtWidgets.QLabel(NewOrderDialog)
        self.date_order_label_2.setGeometry(QtCore.QRect(120, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_order_label_2.setFont(font)
        self.date_order_label_2.setObjectName("date_order_label_2")
        self.phone_number_edit = QtWidgets.QLineEdit(NewOrderDialog)
        self.phone_number_edit.setGeometry(QtCore.QRect(140, 210, 151, 20))
        self.phone_number_edit.setObjectName("phone_number_edit")
        self.verticalLayoutWidget = QtWidgets.QWidget(NewOrderDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 240, 251, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_push_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_push_button.setObjectName("save_push_button")
        self.verticalLayout.addWidget(self.save_push_button)
        self.cancel_push_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_push_button.setObjectName("cancel_push_button")
        self.verticalLayout.addWidget(self.cancel_push_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.day_spin_box = QtWidgets.QSpinBox(NewOrderDialog)
        self.day_spin_box.setGeometry(QtCore.QRect(140, 60, 42, 22))
        self.day_spin_box.setMinimum(1)
        self.day_spin_box.setMaximum(31)
        self.day_spin_box.setProperty("value", 31)
        self.day_spin_box.setObjectName("day_spin_box")
        self.month_spin_box = QtWidgets.QSpinBox(NewOrderDialog)
        self.month_spin_box.setGeometry(QtCore.QRect(190, 60, 42, 22))
        self.month_spin_box.setMaximum(12)
        self.month_spin_box.setSingleStep(1)
        self.month_spin_box.setProperty("value", 12)
        self.month_spin_box.setObjectName("month_spin_box")
        self.year_spin_box = QtWidgets.QSpinBox(NewOrderDialog)
        self.year_spin_box.setGeometry(QtCore.QRect(240, 60, 51, 22))
        self.year_spin_box.setMaximum(9999)
        self.year_spin_box.setProperty("value", 2018)
        self.year_spin_box.setObjectName("year_spin_box")

        self.retranslateUi(NewOrderDialog)
        QtCore.QMetaObject.connectSlotsByName(NewOrderDialog)

    def retranslateUi(self, NewOrderDialog):
        _translate = QtCore.QCoreApplication.translate
        NewOrderDialog.setWindowTitle(_translate("NewOrderDialog", "Dialog"))
        self.first_name_label.setText(_translate("NewOrderDialog", "Имя заказчика"))
        self.date_order_label.setText(_translate("NewOrderDialog", "Дата принятия"))
        self.cost_label.setText(_translate("NewOrderDialog", "Стоимость"))
        self.phone_label.setText(_translate("NewOrderDialog", "Телефон"))
        self.second_name_label.setText(_translate("NewOrderDialog", "Фамилия"))
        self.id_payd_label.setText(_translate("NewOrderDialog", "Оплачен"))
        self.date_order_label_2.setText(_translate("NewOrderDialog", "Новый заказ"))
        self.save_push_button.setText(_translate("NewOrderDialog", "Сохранить"))
        self.cancel_push_button.setText(_translate("NewOrderDialog", "Отменить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewOrderDialog = QtWidgets.QDialog()
    ui = Ui_NewOrderDialog()
    ui.setupUi(NewOrderDialog)
    NewOrderDialog.show()
    sys.exit(app.exec_())

