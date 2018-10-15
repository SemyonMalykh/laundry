# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 609)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orders_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.orders_widget.setGeometry(QtCore.QRect(10, 50, 781, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orders_widget.sizePolicy().hasHeightForWidth())
        self.orders_widget.setSizePolicy(sizePolicy)
        self.orders_widget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.orders_widget.setObjectName("orders_widget")
        self.closed_orders_tab = QtWidgets.QWidget()
        self.closed_orders_tab.setObjectName("closed_orders_tab")
        self.closed_orders_list_view = QtWidgets.QListView(self.closed_orders_tab)
        self.closed_orders_list_view.setGeometry(QtCore.QRect(0, 0, 771, 481))
        self.closed_orders_list_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closed_orders_list_view.setObjectName("closed_orders_list_view")
        self.orders_widget.addTab(self.closed_orders_tab, "")
        self.opened_orders_tab = QtWidgets.QWidget()
        self.opened_orders_tab.setObjectName("opened_orders_tab")
        self.opened_orders_list_view = QtWidgets.QListView(self.opened_orders_tab)
        self.opened_orders_list_view.setGeometry(QtCore.QRect(0, 0, 771, 481))
        self.opened_orders_list_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.opened_orders_list_view.setObjectName("opened_orders_list_view")
        self.orders_widget.addTab(self.opened_orders_tab, "")
        self.new_order_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_order_button.setGeometry(QtCore.QRect(10, 10, 779, 23))
        self.new_order_button.setObjectName("new_order_button")
        self.refresh_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_push_button.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.refresh_push_button.setObjectName("refresh_push_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_login = QtWidgets.QAction(MainWindow)
        self.action_login.setObjectName("action_login")

        self.retranslateUi(MainWindow)
        self.orders_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orders_widget.setTabText(self.orders_widget.indexOf(self.closed_orders_tab), _translate("MainWindow", "Закрытые заказы"))
        self.orders_widget.setTabText(self.orders_widget.indexOf(self.opened_orders_tab), _translate("MainWindow", "Открытые заказы"))
        self.new_order_button.setText(_translate("MainWindow", "Новый заказ"))
        self.refresh_push_button.setText(_translate("MainWindow", "Обновить"))
        self.action_login.setText(_translate("MainWindow", "Login"))
        self.action_login.setShortcut(_translate("MainWindow", "Ctrl+L"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

