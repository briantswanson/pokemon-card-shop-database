# Brian Swanson & Nick Laustrup
# CS 340, Spring 2024
# Portfolio Project Flask Backend

# Citation for the following code:
# Date: 05/19/2024
# Copied from: CS 340 Flask Guide
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

"""
Questions:
1. The credentials don't seem to be working on db_connector... why?
2. How do we implement smaller app.py files (per the video)

"""

from flask import Flask, render_template, json
import os
import json
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/customers')
def customers():
    return "This is the customers route."

def customers():
    query = "SELECT * FROM customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = json.dumps(cursor.fetchall())
    return results


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True)