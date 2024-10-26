import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': '',  # No password
    'host': 'localhost',
    'port': '3306',
    'database': 'payment_system'
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Successfully connected to the database.")
except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
