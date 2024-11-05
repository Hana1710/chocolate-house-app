import sqlite3
from flask import Flask, request, jsonify, g
from sqlite3 import Error

app = Flask(__name__)
DATABASE = 'chocolate_house.db'

def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # To allow dict-like access
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Closes the database connection at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Initializes the database with tables from the schema file."""
    try:
        with app.app_context():
            db = get_db()
            with app.open_resource('schema.sql', mode='r') as f:
                db.executescript(f.read())
    except Error as e:
        print(f"Error initializing database: {e}")

# CRUD Operations for Seasonal Flavors
@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    db = get_db()
    cursor = db.cursor()
    
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input, 'name' is required"}), 400

        try:
            cursor.execute("INSERT INTO SeasonalFlavors (name) VALUES (?)", (data['name'],))
            db.commit()
            return jsonify({"message": "Flavor added successfully"}), 201
        except Error as e:
            db.rollback()
            return jsonify({"error": f"An error occurred: {e}"}), 500

    elif request.method == 'GET':
        cursor.execute("SELECT * FROM SeasonalFlavors")
        flavors = [dict(row) for row in cursor.fetchall()]
        return jsonify(flavors), 200

# Retrieve, Update, and Delete a specific flavor
@app.route('/flavors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_flavor(id):
    db = get_db()
    cursor = db.cursor()
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM SeasonalFlavors WHERE id = ?", (id,))
        flavor = cursor.fetchone()
        if flavor:
            return jsonify(dict(flavor)), 200
        else:
            return jsonify({"error": "Flavor not found"}), 404

    elif request.method == 'PUT':
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input, 'name' is required"}), 400

        try:
            cursor.execute("UPDATE SeasonalFlavors SET name = ? WHERE id = ?", (data['name'], id))
            db.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Flavor not found"}), 404
            return jsonify({"message": "Flavor updated successfully"}), 200
        except Error as e:
            db.rollback()
            return jsonify({"error": f"An error occurred: {e}"}), 500

    elif request.method == 'DELETE':
        try:
            cursor.execute("DELETE FROM SeasonalFlavors WHERE id = ?", (id,))
            db.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Flavor not found"}), 404
            return jsonify({"message": "Flavor deleted successfully"}), 200
        except Error as e:
            db.rollback()
            return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

from flask import render_template

@app.route('/')
def home():
    return app.send_static_file('index.html')
