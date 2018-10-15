import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDate, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QDialog, QDateEdit, QListView, QAbstractItemView
from mainWindow import Ui_MainWindow
from login import Ui_LoginDialog
from newOrderDialog import Ui_NewOrderDialog
from editOrderDialog import Ui_OrderEditDialog
from OrderDialog import Ui_OrderDialog
from interface import get_id_by_name, add_new_customer, add_new_order, get_opened_orders, get_closed_orders, add_employee_order_action
from interface import  Order, get_order_by_id, get_name_by_id, get_customer_phone_by_id, update_order, check_login_password
import datetime
from hashlib import md5


is_logged = False
logged_id = None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.new_order_button.clicked.connect(self.logCheck)
        self.refresh_push_button.clicked.connect(self.updateWindow)
        self.setWindowTitle("Прачечная")
        text = ''
        self.model_opened_list = QtGui.QStandardItemModel(self.opened_orders_list_view)
        self.model_closed_list = QtGui.QStandardItemModel(self.opened_orders_list_view)
        self.updateWindow()
        self.opened_orders_list_view.doubleClicked.connect(self.orderDialog)
        self.closed_orders_list_view.doubleClicked.connect(self.orderDialog)

    def updateOpenedListModel(self):
        self.model_opened_list = QtGui.QStandardItemModel(self.opened_orders_list_view)
        for order in get_opened_orders():
            text = ">> " + order.getShortPrintedOrder()
            item = QtGui.QStandardItem(text)
            self.model_opened_list.appendRow(item)
        self.opened_orders_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.opened_orders_list_view.setModel(self.model_opened_list)

    def updateClosedListModel(self):
        self.model_closed_list = QtGui.QStandardItemModel(self.opened_orders_list_view)
        for order in get_closed_orders():
            text = ">> " + order.getShortPrintedOrder()
            item = QtGui.QStandardItem(text)  # create an item with a caption
            self.model_closed_list.appendRow(item)  # Add the item to the model
        # Apply the model to the list view
        self.closed_orders_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.closed_orders_list_view.setModel(self.model_closed_list)

    def updateWindow(self):
        self.updateOpenedListModel()
        self.updateClosedListModel()

    def logCheck(self):
        print(is_logged)
        if (not is_logged):
            updateDialog = Login()
            updateDialog.exec_()
        else:
            print("Logged in")
            updateDialog = NewOrder()
            updateDialog.exec()
            self.updateOpenedListModel()

    def orderDialog(self):
        if (not is_logged):
            updateDialog = Login()
            updateDialog.exec_()
        else:
            print("Bada bum - bada bang!")
            if (self.opened_orders_list_view.selectionModel().hasSelection()):
                print("Has selection: ")
                selectedRow = (self.opened_orders_list_view.selectionModel().selectedRows())
                row = self.model_opened_list.item(selectedRow[0].row()).text()
                print(row)
            if(self.closed_orders_list_view.selectionModel().hasSelection()):
                selectedRow = (self.closed_orders_list_view.selectionModel().selectedRows())
                row = self.model_closed_list.item(selectedRow[0].row()).text()
            updateDialog = OrderDialog(row)
            updateDialog.exec()
            self.updateWindow()


class OrderDialog(QDialog, Ui_OrderDialog):
    def __init__(self, shortOrder):
        QDialog.__init__(self)
        self.setupUi(self)
        self.order_id = int(shortOrder.split()[2])
        self.setWindowTitle("Заказ номер " + str(self.order_id))
        print(self.order_id)
        order = get_order_by_id(self.order_id)
        self.temp_label.setText(order.getPrintedOrder())
        self.edit_push_button.clicked.connect(self.edit)

    def edit(self):
        self.hide()
        updateDialog = EditOrder(self.order_id)
        updateDialog.exec()


class EditOrder(QDialog, Ui_OrderEditDialog):
    def __init__(self, order_id):
        QDialog.__init__(self)
        self.setupUi(self)
        self.cancel_push_button.clicked.connect(self.close)
        self.save_push_button.clicked.connect(self.validation)
        self.order = get_order_by_id(order_id)
        self.id_edit.setText(str(self.order.id_order))
        self.day_order_spin_box.setValue(self.order.date.day)
        self.month_order_spin_box.setValue(self.order.date.month)
        self.year_order_spin_box.setValue(self.order.date.year)
        if (self.order.date_rendition is None):
            self.day_rendition_spin_box.setValue(0)
            self.month_rendition_spin_box.setValue(0)
            self.year_rendition_spin_box.setValue(0)
        else:
            self.day_rendition_spin_box.setValue(self.order.date_rendition.day)
            self.month_rendition_spin_box.setValue(self.order.date_rendition.month)
            self.year_rendition_spin_box.setValue(self.order.date_rendition.year)
        self.status_spin_box.setValue(self.order.status)
        self.cost_edit.setText(str(self.order.cost))
        if (self.order.is_payed):
            self.is_payed_check_box.setChecked(True)
        else:
            self.is_payed_check_box.setChecked(False)
        if (not self.order.date_pay is None):
            self.day_pay_spin_box.setValue(self.order.date_pay.day)
            self.month_pay_spin_box.setValue(self.order.date_pay.month)
            self.year_pay_spin_box.setValue(self.order.date_pay.year)
        else:
            self.day_pay_spin_box.setValue(0)
            self.month_pay_spin_box.setValue(0)
            self.year_pay_spin_box.setValue(0)
        customer_full_name = get_name_by_id(self.order.id_customer)
        self.first_name_edit.setText(customer_full_name[0])
        self.second_name_edit.setText(customer_full_name[1])
        phone = get_customer_phone_by_id(self.order.id_customer)
        if (not phone is None):
            self.phone_number_edit.setText(str(phone))
        else:
            self.phone_number_edit.setText("Не указан")

    def validation(self):
        valid = True
        self.year_rendition_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.month_rendition_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.day_rendition_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.year_pay_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.month_pay_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.day_pay_spin_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cost_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        date = datetime.date(self.year_order_spin_box.value(),
                             self.month_order_spin_box.value(),
                             self.day_order_spin_box.value())
        if ((not self.year_rendition_spin_box.value() == 0) and (not self.month_rendition_spin_box.value() == 0) and
                (not self.day_rendition_spin_box.value() == 0)):
            date_rendition = datetime.date(self.year_rendition_spin_box.value(),
                                                 self.month_rendition_spin_box.value(),
                                                 self.day_rendition_spin_box.value())
            if (date_rendition >= date):
                print("OK")
            else:
                print("Not OK")
                self.year_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.month_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.day_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                valid = False
        elif ((not self.year_rendition_spin_box.value() == 0) or (not self.month_rendition_spin_box.value() == 0) or
                (not self.day_rendition_spin_box.value() == 0)):
            print("Not OK")
            self.year_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.month_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.day_rendition_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            valid = False
        if ((not self.year_pay_spin_box.value() == 0) and (not self.month_pay_spin_box.value() == 0) and
                (not self.day_pay_spin_box.value() == 0)):
            date_pay = datetime.date(self.year_pay_spin_box.value(),
                                                 self.month_pay_spin_box.value(),
                                                 self.day_pay_spin_box.value())
            if (date_pay >= date):
                print("OK")
            else:
                print("Not OK")
                self.year_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.month_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.day_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
                valid = False
        elif ((not self.year_pay_spin_box.value() == 0) or (not self.month_pay_spin_box.value() == 0) or
                (not self.day_pay_spin_box.value() == 0)):
            print("Not OK")
            self.year_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.month_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.day_pay_spin_box.setStyleSheet("background-color: rgb(255, 0, 0);")
            valid = False
        if (not self.cost_edit.text().isdigit()):
            self.cost_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
            valid = False
        print(valid)
        if(valid):
            self.setOrder()

    def setOrder(self):
        order = Order()
        order.id_order = int(self.id_edit.text())
        order.date = datetime.date(self.year_order_spin_box.value(),
                                    self.month_order_spin_box.value(),
                                    self.day_order_spin_box.value())
        if(not self.year_rendition_spin_box.value() == 0):
            order.date_rendition = datetime.date(self.year_rendition_spin_box.value(),
                                                  self.month_rendition_spin_box.value(),
                                                  self.day_rendition_spin_box.value())
        else:
            order.date_rendition = None
        order.status = self.status_spin_box.value()
        order.cost = int(self.cost_edit.text())
        order.is_payed = bool(self.is_payed_check_box.isChecked())
        if (not self.year_pay_spin_box.value() == 0):
            order.date_pay = datetime.date(self.year_pay_spin_box.value(),
                                           self.month_pay_spin_box.value(),
                                           self.day_pay_spin_box.value())
        else:
            order.date_pay = None
        print(self.year_pay_spin_box.value())
        order.id_customer = self.order.id_customer
        update_order(order)
        global logged_id
        add_employee_order_action(order.id_order, logged_id)
        self.hide()


class Login(QDialog, Ui_LoginDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.submit_button.clicked.connect(self.PrintNameAndPass)
        self.setWindowTitle("Индектификация")

    def PrintNameAndPass(self):
        global is_logged
        global logged_id
        name = self.name_edit.text()
        second_name = self.second_name_edit.text()
        print(name)
        password = md5(self.password.text().encode()).hexdigest()
        print(password)
        id = check_login_password(name, second_name, password)
        if (bool(id)):
            is_logged = True
            logged_id = id
            self.hide()
        else:
            self.error_message_label.setStyleSheet("color: rgb(255, 0, 0);")
            self.error_message_label.setText("Неверное имя пользователя или пароль")


class NewOrder(QDialog, Ui_NewOrderDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.save_push_button.clicked.connect(self.validation)
        self.cancel_push_button.clicked.connect(self.close)
        today = datetime.date.today()
        self.year_spin_box.setValue(today.year)
        self.month_spin_box.setValue(today.month)
        self.day_spin_box.setValue(today.day)

    def validation(self):
        if (not ((self.first_name_edit.text() == "") or (self.second_name_edit.text() == "") or
                (self.cost_edit.text() == "") or (not self.cost_edit.text().isdigit()))):
            self.insertNewOrder()
        else:
            if (self.first_name_edit.text() == ""):
                self.first_name_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.first_name_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            if (self.second_name_edit.text() == ""):
                self.second_name_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.second_name_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
            if(self.cost_edit.text() == "" or (not self.cost_edit.text().isdigit())):
                self.cost_edit.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.cost_edit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def insertNewOrder(self):
        #global logged_id
        new_order = Order()
        new_order.date = datetime.datetime(int(self.year_spin_box.text()), int(self.month_spin_box.text()),
          int(self.day_spin_box.text()))
        new_order.cost = int(self.cost_edit.text())
        new_order.is_payed = bool(self.is_payed_check_box.checkState())
        new_order.id_customer = get_id_by_name(self.first_name_edit.text(), self.second_name_edit.text())
        if(new_order.id_customer is None):
            new_order.id_customer = add_new_customer(self.first_name_edit.text(), self.second_name_edit.text(),
                                                     self.phone_number_edit.text())
        order_id = add_new_order(new_order)
        add_employee_order_action(order_id, logged_id)
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
