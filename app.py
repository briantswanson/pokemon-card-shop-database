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
    Needs to be connecting to classmysql and not classwork
    Make sure you are connected to mysql first!!! solved.
2. How do we implement smaller app.py files (per the video)

"""

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

# Configuration

app = Flask(__name__)

mysql = MySQL(app)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_swanbria"
app.config["MYSQL_PASSWORD"] = "IKWjiilHUyLz"
app.config["MYSQL_DB"] = "cs340_swanbria"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


# db_connection = db.connect_to_database()

# Routes 

# redirect page to Customers
@app.route("/")
def home():
    return redirect("/customers")

@app.route('/customers', methods=["POST","GET"])
def customers():

    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Customer"):
            # grab user form inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            # address is null-able

            if address == "":
                # mySQL query to insert a new person into Customers with our form inputs
                query = "INSERT INTO Customers (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone))
                mysql.connection.commit()
            
            # no null inputs

            else:
                query = "INSERT INTO Customers (firstName, lastName, email, phone, address) VALUES (%s, %s,%s,%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, address))
                mysql.connection.commit()

            # redirect back to Customers page
            return redirect("/customers")

    if request.method == "GET":
        # mySQL query to grab all the people in Customers
        query = "SELECT Customers.customerID, firstName, lastName, email, phone, address"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("customers.j2", data=data)

@app.route("/delete_customers/<int:customerID>")
def delete_customers(customerID):
    # mySQL query to delete the customer with our passed customerID
    query = "DELETE FROM Customers WHERE customerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customerID,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/customers")

@app.route("/edit_customers/<int:customerID>", methods=["POST", "GET"])
def edit_customers(customerID):
    if request.method == "GET":
        # mySQL query to grab the info of the customer with our passed customerID
        query = "SELECT * FROM Customers WHERE customerID = %s" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_customers.j2", data=data)
    
    if request.method == "POST":
        # fire off if user clicks the 'Edit Customer' button
        if request.form.get("Edit_Customer"):
            # grab user form inputs
            customerID = request.form["customerID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            address = request.form["address"]

            # account for null address
            if (address == "" or address == "None"):
                # mySQL query to update the attributes of customer with our passed customerID value
                query = "UPDATE Customers SET Customers.firstName = %s, Customers.lastName = %s, Customers.email = %s, Customers.phone = %s, Customers.address = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, customerID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Customers SET Customers.firstName = %s, Customers.lastName = %s, Customers.email = %s, Customers.phone = %s, Customers.address = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, customerID))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/customers")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True)