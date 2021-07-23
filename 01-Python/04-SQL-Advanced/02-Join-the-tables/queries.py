# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = '''
        SELECT o.OrderID, c.ContactName , e.FirstName
        FROM Orders o
        JOIN Customers c ON c.CustomerID = o.CustomerID
        JOIN Employees e ON e.EmployeeID = o.EmployeeID
        ORDER BY o.OrderID ASC
    '''
    db.execute(query)
    return db.fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''

    query = '''
        SELECT DISTINCT c.ContactName ,
	    SUM(od.UnitPrice * od.Quantity) OVER (
        PARTITION BY c.CustomerID
        ) AS spent_per_customer
        FROM Orders o
        JOIN Customers c ON c.CustomerID = o.CustomerID
        JOIN OrderDetails od ON od.OrderID = o.OrderID
        ORDER BY spent_per_customer ASC
    '''
    db.execute(query)
    return db.fetchall()


def best_employee(db):
    query = '''
    SELECT DISTINCT e.FirstName, e.LastName,
	SUM(od.UnitPrice * od.Quantity) OVER (
    PARTITION BY e.EmployeeID
    ) AS best_employee
    FROM Orders o
    INNER JOIN Employees e ON e.EmployeeID =o.EmployeeID
    INNER JOIN OrderDetails od ON od.OrderID = o.OrderID
    ORDER BY best_employee DESC
    '''

    db.execute(query)
    return db.fetchall()[0]

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = '''
    SELECT DISTINCT c.ContactName,
    COUNT(o.OrderID) OVER (
    PARTITION BY c.CustomerID
    ) AS number_of_orders
    FROM Customers c
    LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
    ORDER BY number_of_orders ASC
    '''
    db.execute(query)
    return db.fetchall()
