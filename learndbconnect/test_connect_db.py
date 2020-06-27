import mysql.connector

config = {"user": "root",
          "password": 'root',
          "host": 'localhost',
          "database": 'my_data'
          }

cnx = mysql.connector.connect(**config)

try:
    cursor = cnx.cursor()
    query = "INSERT INTO my_info (name,father_name,mother_name,school_name) VALUES (%s, %s, %s, %s)"
    val = ("Joshua", "John", "Josephine", "SJBHS")

    cursor.execute(query, val)
    cnx.commit()
    print(cursor.rowcount, "record inserted.")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    cnx.rollback()
finally:
    cnx.close()

