from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running!"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cur = conn.cursor()

        cur.execute("SELECT version();")
        version = cur.fetchone()

        conn.close()

        return f"Connected to SQLlite: {version[0]}"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)