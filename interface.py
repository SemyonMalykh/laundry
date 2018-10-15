from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import datetime
import configparser

class Order():
    def __init__(self, id_order = None, date = datetime.date.today(), date_rendition = None, status = 0, cost = None,
            is_payed = False, date_pay = None, id_customer = None, id_laundry = 1):
        self.id_order = id_order
        self.date = date
        self.date_rendition = date_rendition
        self.status = status
        self.cost = cost
        self.is_payed = is_payed
        self.date_pay = date_pay
        self.id_customer = id_customer
        self.id_laundry = id_laundry

    def getPrintedOrder(self):
        customer_full_name = get_name_by_id(self.id_customer)
        customer_first_name = customer_full_name[0]
        customer_second_name = customer_full_name[1]
        customer_phone_number = get_customer_phone_by_id(self.id_customer)
        printed_order = ("Номер: " + str(self.id_order) + "\nДата: "+ str(self.date) + "\nДата выдачи: " + str(self.date_rendition)
              + "\nСтатус: " + str(self.status)+ "\nСтоимость: " + str(self.cost) +"\nОплачен: " + str(self.is_payed) + "\nДата оплаты: " +
              str(self.date_pay) + "\nИмя покупателя: " + customer_first_name + "\nФамилия покупателя: " + customer_second_name +
              "\nТелефон покупателя:" + str(customer_phone_number) + "\nНомер прачечной: " + str(self.id_loundry))
        print(printed_order)
        return(printed_order)

    def getShortPrintedOrder(self):
        customer_full_name = get_name_by_id(self.id_customer)
        customer = customer_full_name[0] + ' ' + customer_full_name[1]
        payed = "Нет"
        if (self.is_payed):
            payed = "Да"
        printed_order = ("№ " + str(self.id_order) + " Дата: " + str(self.date)  + " Покупатель: " + customer +
                         " Стоимость: " + str(self.cost) + " Оплачен: " + payed)
        #print(printed_order)
        return (printed_order)

def get_name_by_id(customer_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT  First_Name_Customer, Second_Name_Customer FROM customer WHERE ID_Customer = " + \
                str(customer_id)
       # print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
           # print(row)
            return(row)
    finally:
         cursor.close()
         conn.close()

def get_customer_phone_by_id(customer_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT  Phone_Customer FROM customer WHERE ID_Customer = " + \
                str(customer_id)
       # print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            return(row[0])

    finally:
         cursor.close()
         conn.close()

def get_id_by_name(customer_first_name, customer_second_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        #print(customer_first_name, customer_second_name)
        query = "SELECT ID_Customer FROM customer WHERE First_Name_Customer = '" +  customer_first_name + "' " \
                "AND Second_Name_Customer = '" + customer_second_name + "'"
       # print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            #print(row)
            return(row)[0]
    finally:
         cursor.close()
         conn.close()

def add_new_customer(fist_name_customer, second_name_customer, phone_customer):
    query = "INSERT INTO customer(First_Name_Customer, Second_Name_Customer, Phone_Customer) VALUES (%s,%s, %s)"
    args = (fist_name_customer, second_name_customer, phone_customer)
    if (phone_customer == ""):
        phone_customer = "Не указан"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        #print(customer_first_name, customer_second_name)
        query = "SELECT Id_Customer FROM Customer WHERE Id_Customer =(SELECT max(Id_Customer) FROM Customer)"
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            return(row)[0]
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def get_opened_orders():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT * FROM lorder WHERE Status = '0'"
        cursor.execute(query)
        row = cursor.fetchone()
        opened_orders = []
        while row is not None:
            temp_order = Order()
            temp_order.id_order = row[0]
            temp_order.date = row[1]
            temp_order.date_rendition = row[2]
            temp_order.status = row[3]
            temp_order.cost = row[4]
            temp_order.is_payed = bool(row[5])
            temp_order.date_pay = row[6]
            temp_order.id_customer = row[7]
            temp_order.id_loundry = row[8]
            opened_orders.append(temp_order)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return (opened_orders)

def get_closed_orders():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT * FROM lorder WHERE Status = '1'"
        cursor.execute(query)
        row = cursor.fetchone()
        opened_orders = []
        while row is not None:
            temp_order = Order()
            temp_order.id_order = row[0]
            temp_order.date = row[1]
            temp_order.date_rendition = row[2]
            temp_order.status = row[3]
            temp_order.cost = row[4]
            temp_order.is_payed = bool(row[5])
            temp_order.date_pay = row[6]
            temp_order.id_customer = row[7]
            temp_order.id_loundry = row[8]
            opened_orders.append(temp_order)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return (opened_orders)

def get_order_by_id(order_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT * FROM lorder WHERE ID_Order = '" + str(order_id) + "'"
        cursor.execute(query)
        row = cursor.fetchone()
        temp_order = Order()
        temp_order.id_order = row[0]
        temp_order.date = row[1]
        temp_order.date_rendition = row[2]
        temp_order.status = row[3]
        temp_order.cost = row[4]
        temp_order.is_payed = bool(row[5])
        temp_order.date_pay = row[6]
        temp_order.id_customer = row[7]
        temp_order.id_loundry = row[8]
        row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return (temp_order)

def add_new_order(order):
    query = "INSERT INTO lorder(Date_Order, Cost, Is_Payed, Date_Pay ,ID_Customer, ID_Laundry) VALUES(%s,%s, %s, %s ,%s, %s)"
    args = (order.date, order.cost, order.is_payed, order.date_pay, order.id_customer, order.id_laundry)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # print(customer_first_name, customer_second_name)
        query = "SELECT ID_Order FROM lorder WHERE ID_Order =(SELECT max(ID_Order) FROM lorder)"
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            return (row)[0]
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def update_order(order):
    query = "UPDATE lorder SET Date_Order = %s, Date_Rendition = %s, Status = %s, " \
            "Cost = %s, Is_Payed = %s, Date_Pay = %s WHERE Id_Order = %s"
    args = (order.date, order.date_rendition, order.status, order.cost, order.is_payed,
            order.date_pay, order.id_order)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def check_login_password(first_name, second_name, pass_hash):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT Id_Employee FROM employee WHERE First_Name = %s AND Second_Name = %s AND Password = %s"
        args = (first_name, second_name, pass_hash)
        # print(query)
        cursor.execute(query, args)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            print(row[0])
            return (row[0])
    finally:
        cursor.close()
        conn.close()

def add_employee_order_action(order_id, employee_id):
    query = "INSERT INTO employee_to_order(ID_Order, ID_Employee) VALUES(%s,%s)"
    args = (order_id, employee_id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

