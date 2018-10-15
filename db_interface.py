

def get_name_by_id(customer_id):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = "SELECT  First_Name_Customer, Second_Name_Customer FROM customer WHERE ID_Customer = " + \
                str(customer_id)
        print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            print(row)
            return(row)[0]
    finally:
         cursor.close()
         conn.close()

get_name_by_id(1)

def get_id_by_name(customer_first_name, customer_second_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        print(customer_first_name, customer_second_name)
        query = "SELECT ID_Customer FROM customer WHERE First_Name_Customer = '" +  customer_first_name + "' " \
                "AND Second_Name_Customer = '" + customer_second_name + "'"
        print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            cursor.close()
            conn.close()
            print(row)
            return(row)[0]
    finally:
         cursor.close()
         conn.close()

def add_new_customer(fist_name_customer, second_name_customer, phone_customer):
    query = "INSERT INTO customer(First_Name_Customer, Second_Name_Customer, Phone_Customer) VALUES (%s,%s, %s)"
    args = (fist_name_customer, second_name_customer, phone_customer)

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


def add_new_order(cost, id_customer, date = datetime.date.today(), is_payed = False, id_laundry = 1):
    query = "INSERT INTO lorder(Date_Order, Cost, Is_Payed, Date_Pay ,ID_Customer, ID_Laundry) VALUES(%s,%s, %s, %s ,%s, %s)"
    if (is_payed):
        pay_date = date
    else:
        pay_date = None

    args = (date, cost, is_payed, pay_date, id_customer, id_laundry)

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
