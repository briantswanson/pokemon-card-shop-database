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
    # return redirect("/customers")
    return render_template('index.html')

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
        query = "SELECT Customers.customerID, firstName, lastName, email, phone, address FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("customers.html", data=data, header="Customers", id_type="customerID")

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

        return render_template("edit_customers.html", data=data, header="Customers", id_type="customerID")
    
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
                cur.execute(query, (firstName, lastName, email, phone, address, customerID))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/customers")

# Employees
@app.route('/employees', methods=["POST","GET"])
def employees():

    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Employee"):
            # grab user form inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            wage = request.form["wage"]

            # wage is null-able

            if wage == "":
                # mySQL query to insert a new person into Employees with our form inputs
                query = "INSERT INTO Employees (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone))
                mysql.connection.commit()
            
            # no null inputs

            else:
                query = "INSERT INTO Employees (firstName, lastName, email, phone, wage) VALUES (%s, %s,%s,%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, wage))
                mysql.connection.commit()

            # redirect back to Employees page
            return redirect("/employees")

    if request.method == "GET":
        # mySQL query to grab all the people in Employees
        query = "SELECT Employees.employeeID, firstName, lastName, email, phone, wage FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("employees.html", data=data, header="Employees", id_type="employeeID")

@app.route("/delete_employees/<int:employeeID>")
def delete_employees(employeeID):
    # mySQL query to delete the employee with our passed employeeID
    query = "DELETE FROM Employees WHERE employeeID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employeeID,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/employees")

@app.route("/edit_employees/<int:employeeID>", methods=["POST", "GET"])
def edit_employees(employeeID):
    if request.method == "GET":
        # mySQL query to grab the info of the employee with our passed employeeID
        query = "SELECT * FROM Employees WHERE employeeID = %s" % (employeeID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_employees.html", data=data, header="Employees")
    
    if request.method == "POST":
        # fire off if user clicks the 'Edit Employee' button
        if request.form.get("Edit_Employee"):
            # grab user form inputs
            employeeID = request.form["employeeID"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phone = request.form["phone"]
            wage = request.form["wage"]

            # account for null wage
            if (wage == "" or wage == "None"):
                # mySQL query to update the attributes of employee with our passed employeeID value
                query = "UPDATE Employees SET Employees.firstName = %s, Employees.lastName = %s, Employees.email = %s, Employees.phone = %s, Employees.wage = NULL WHERE Employees.employeeID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, employeeID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Employees SET Employees.firstName = %s, Employees.lastName = %s, Employees.email = %s, Employees.phone = %s, Employees.wage = %s WHERE Employees.employeeID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (firstName, lastName, email, phone, wage, employeeID))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/employees")
        
        
# Products
@app.route('/products', methods=["POST","GET"])
def products():

    if request.method == "POST":
        # fire off if user presses the Add Product button
        if request.form.get("Add_Product"):
            # grab user form inputs
            
            ####  PRODUCTS ####
            inStock = request.form["inStock"]
            price = request.form["price"]
            
            ####  PRODUCTDETAILS  ####
            type = request.form["type"]
            name = request.form["name"]
            
            ####  PRODUCTDETAILS  ####
            query = "INSERT INTO ProductDetails (name, type) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, type))
            mysql.connection.commit()
            
            ####  PRODUCTS ####
            query = "INSERT INTO Products (price, inStock, productDetailsID) VALUES (%s, %s, (SELECT productDetailsID FROM ProductDetails WHERE ProductDetails.name = %s LIMIT 1))"
            cur = mysql.connection.cursor()
            cur.execute(query, (price, inStock, name))
            mysql.connection.commit()
        

            # redirect back to Products page
            return redirect("/products")

    if request.method == "GET":
        # mySQL query to grab all the people in Products
        query = "SELECT productID, price, inStock, type, name, Products.productDetailsID FROM Products JOIN ProductDetails ON Products.productDetailsID = ProductDetails.productDetailsID"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("products.html", data=data, header="Products", id_type="productID")

@app.route("/delete_products/<int:productID>")
def delete_products(productID):
    # mySQL query to delete the product with our passed productID
    query = "DELETE FROM Products WHERE productID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (productID,))
    mysql.connection.commit()

    # redirect back to product page
    return redirect("/products")

@app.route("/edit_products/<int:productID>", methods=["POST", "GET"])
def edit_products(productID):
    if request.method == "GET":
        # mySQL query to grab the info of the product with our passed productID
        query = """
        SELECT productID, price, inStock, Products.productDetailsID, type, name FROM Products 
        JOIN ProductDetails 
        ON Products.productDetailsID = ProductDetails.productDetailsID 
        WHERE productID = %s
        """
        cur = mysql.connection.cursor()
        cur.execute(query, (productID,))
        data = cur.fetchall()

        return render_template("edit_products.html", data=data, header="Products", id_type="productID")
    
    if request.method == "POST":
        # fire off if user presses the Add Product button
        if request.form.get("Edit_Product"):
            # grab user form inputs
            
            ####  PRODUCTS ####
            inStock = request.form["inStock"]
            price = request.form["price"]
            
            ####  PRODUCTDETAILS  ####
            type = request.form["type"]
            name = request.form["name"]
            productDetailsID = request.form["productDetailsID"]


            #     # mySQL query to update the attributes of product with our passed productID value
            # query = "UPDATE Products SET Products.firstName = %s, Products.lastName = %s, Products.email = %s, Products.phone = %s, Products.wage = NULL WHERE Products.productID = %s"
            # cur = mysql.connection.cursor()
            # cur.execute(query, (firstName, lastName, productID))
            # mysql.connection.commit()


            ####  PRODUCTDETAILS  ####
            query = """
            UPDATE ProductDetails
            SET ProductDetails.name = %s, ProductDetails.type = %s 
            WHERE ProductDetails.productDetailsID = %s
            """
            cur = mysql.connection.cursor()
            cur.execute(query, (name, type, productDetailsID))
            mysql.connection.commit()
            
            ####  PRODUCTS ####
            query = """
            UPDATE Products 
            SET Products.price = %s, Products.inStock = %s
            WHERE Products.productID = %s
            """
            cur = mysql.connection.cursor()
            cur.execute(query, (price, inStock, productID))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/products")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1425))
    app.run(port=port, debug=True)