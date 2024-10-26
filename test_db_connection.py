import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': '',  # No password
    'host': 'localhost',
    'port': '3306',
    'database': 'payment_system'
}

print("Starting database connection test...")  # Debugging statement

try:
    print("Attempting to connect to the database...")  # Debugging statement
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Successfully connected to the database.")
        db_info = connection.get_server_info()
        print("Server version:", db_info)
except Error as e:
    print("Error while connecting to MySQL:", e)
except Exception as ex:
    print("An unexpected error occurred:", ex)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")
    else:
        print("No connection to close.")
