-- Brian Swanson & Nick Laustrup
-- Group 98
-- Portfolio Project Step 3 DMQ

# Citation for the following function: SQL DMQ
# Date: 5/5/2024
# Copied from /OR/ Adapted from /OR/ Based on 
# Starter Code on Canvas for DMQ queries
# Source URL: https://canvas.oregonstate.edu/courses/1958399/pages/exploration-database-application-design?module_item_id=24181845

-- READ customers
SELECT Customers.customerID, Customers.firstName, Customers.lastName, Customers.email, Customers.phone, Customers.address
FROM Customers;

-- READ employees
SELECT employeeID, firstName, lastName, email, phone, wage
FROM Employees;

-- READ products, inner join with productDetails
SELECT productID, name, price, type, inStock, productDetailsID
FROM Products
INNER JOIN productDetails
ON products.productDetailsID = ProductDetails.productDetailsID;

-- READ transactions
SELECT transactionID, customerID, employeeID, productID, name, price
FROM Transactions
INNER JOIN Transactions_has_Products
ON Transactions.transactionID = Transactions_has_Products.transactionID
INNER JOIN Products
ON Transactions_has_Products.productID = Products.productID;

-- get all product data
SELECT productDetailID, type FROM ProductDetails;

-- CREATE a new product
INSERT INTO ProductDetails (type, name)
VALUES (productTypeInput, productNameInput);
INSERT INTO Products (price, inStock, productDetailsID)
	-- user enters price, we put a "1" for in-stock, and then the productDetailsID is pulled from the ProductDetails table based on the type.
VALUES (priceInput, "1",
	(SELECT productDetailsID from ProductDetails WHERE type = productTypeInput)
);

-- CREATE a new Customer
INSERT INTO Customers (firstName, lastName, email, phone, address)
VALUES (firstNameInput, lastNameInput, emailInput, phoneInput, addressInput);


-- CREATE a new Employee
INSERT INTO Employees (firstName, lastName, email, phone, wage)
VALUES (firstNameInput, lastNameInput, emailInput, phoneInput, wageInput);

-- CREATE a new Transaction
	-- get all Customer IDs and Names to populate the dropdown
	SELECT customerID, firstName, lastName FROM Customers;

	-- get all Employee IDs and Names to populate the dropdown
	SELECT employeeID, firstName, lastName FROM Employees;

	-- add a transaction
INSERT INTO Transactions (customerID, employeeID)
VALUES (
	(SELECT customerID FROM Customers WHERE firstName = firstNameInput AND lastName = lastNameInput),
    (SELECT employeeID FROM Employees WHERE firstName = firstNameInput AND lastName = lastNameInput)
);

-- Delete an Employee
DELETE FROM Employees WHERE id = employeeIdInput;

-- Update a Customer
SELECT customerID, firstName, lastName, email, phone, address
FROM Customers
WHERE customerID = customerIdInput;

UPDATE Customers
	SET firstName = firstNameInput, lastName = lastNameInput, email = emailInput, phone = phoneInput, address = addressInput
    WHERE customerID = customerIdInput;

-- SEARCH command for Customers using lastName
SELECT Customers.customerID, Customers.firstName, Customers.lastName, Customers.email, Customers.phone, Customers.address
FROM Customers WHERE (Customers.lastName = :userSearch)};
