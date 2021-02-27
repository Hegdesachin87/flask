import psycopg2
from psycopg2 import Error


def select_data(table):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="psql",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ems")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("select * from {};".format(table))
        # Fetch result
        record = cursor.fetchall()
        return record
    except:
        throw("Error while selecting data ")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_data(emp_id, name, email, phone, address, metadata):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="psql",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ems")

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        table_insert_query = "INSERT INTO employee(emp_id, name, email, phone, address, metadata)\
        VALUES('"+emp_id+"', '"+name+"', '"+email+"', '"+phone+"', '"+address+"', '"+metadata+"')"
        print(table_insert_query)
        cursor.execute(table_insert_query)
        connection.commit()

    except:
        throw("Error while inserting data to emp_details")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def update_data(update_content, update_content_value, id):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="psql",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ems")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        print("UPDATE employee set {}={} where emp_id={}".format(
            update_content, update_content_value, id))
        cursor.execute(
            "UPDATE employee set {}='{}' where emp_id={}".format(update_content, update_content_value, id))
        connection.commit()
    except:
        throw("Error while updating data")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def delete_data(delete_id):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="psql",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ems")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(
            "DELETE from employee where emp_id={}".format(delete_id))
        connection.commit()

    except:
        throw("Error while connecting to PostgreSQL")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def order_by(table, column, order):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="psql",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ems")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        x = cursor.execute(
            "Select * FROM {} ORDER BY {} {}".format(table, column, order))
        connection.commit()
        record = cursor.fetchall()
        return record
    except:
        throw("Error while connecting to PostgreSQL")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
