from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/")
def insert():
    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(50))")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ("Anish",))
    
    db.commit()
    cursor.close()
    db.close()
    
    return "Data Inserted Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
