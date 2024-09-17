from flask import Flask, jsonify
import sqlite3
import requests

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def list_tables():
    try:
        conn = get_db_connection()
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row['name'] for row in cursor.fetchall()]
        conn.close()
        return jsonify(tables)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data', methods=['GET'])
def show_data():
    try:
        conn = get_db_connection()
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row['name'] for row in cursor.fetchall() if row['name'] != 'sqlite_sequence']
        data = {}
        for table in tables:
            try:
                column_info = conn.execute(f"PRAGMA table_info({table})").fetchall()
                columns = [col['name'] for col in column_info]
                
                rows = conn.execute(f"SELECT * FROM {table}").fetchall()
                data[table] = [dict(zip(columns, row)) for row in rows]
            except Exception as e:
                data[table] = {'error': str(e)}
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/external', methods=['GET'])
def external_api():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import db_init
    db_init.init_db()
    app.run(host='0.0.0.0', port=80, debug=True)
