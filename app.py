from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="himanshi@2004",
        database="ipl_project"
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/matches')
def matches():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches LIMIT 10")
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return render_template('matches.html', matches=data, columns=columns)

@app.route('/deliveries')
def deliveries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deliveries LIMIT 10")
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return render_template('deliveries.html', deliveries=data, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)