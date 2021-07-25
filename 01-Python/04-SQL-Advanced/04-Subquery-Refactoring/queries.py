# pylint:disable=C0111,C0103

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID
    query ='''
    WITH AmountTable AS (
    SELECT DISTINCT c.CustomerID,
    SUM (od.UnitPrice * od.Quantity) OVER(
    PARTITION BY o.OrderID
    ) AS OrderedAmount
    FROM Orders o
    JOIN Customers c ON c.CustomerID = o.CustomerID
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    ORDER BY c.CustomerID
    )
    SELECT DISTINCT CustomerID ,
    ROUND(AVG(OrderedAmount) OVER(
    PARTITION BY CustomerID
    ),2) AS AverageOrderedAmount
    FROM AmountTable
    '''
    db.execute(query)
    return db.fetchall()

def get_general_avg_order(db):
    # return the average amount spent per order
    query = '''
    WITH SumTable AS (
    SELECT DISTINCT
    sum (od.UnitPrice * od.Quantity) OVER(
    PARTITION BY o.OrderID
    ) AS sum_order
    FROM Orders o
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    )
    SELECT ROUND(AVG(sum_order),2) AS avg_order
    FROM SumTable
    '''
    db.execute(query)
    return db.fetchone()[0]


def best_customers(db):

    get_average_purchase(db)
    # return the customers who have an average purchase greater than the general average purchase
    pass  # YOUR CODE HERE

def top_ordered_product_per_customer(db):

    query = '''
 	WITH table_2 as
	(WITH AmountTable AS (
	SELECT c.CustomerID,
    od.ProductID,
	SUM(od.UnitPrice *od.Quantity) OVER (
    PARTITION BY od.ProductID, c.CustomerID
    ORDER BY c.CustomerID
    ) AS OrderedAmount
    FROM Orders o
    JOIN Customers c ON c.CustomerID = o.CustomerID
    JOIN OrderDetails od ON od.OrderID = o.OrderID
	ORDER BY c.CustomerID ASC, OrderedAmount DESC
	)
	SELECT *,
	ROW_NUMBER ()
    OVER(
    PARTITION BY AmountTable.CustomerID
    ORDER BY CustomerID) rk
	FROM AmountTable)
	SELECT CustomerID , ProductID, OrderedAmount
	FROM table_2
	WHERE rk=1
	ORDER BY OrderedAmount DESC
    '''
    db.execute(query)
    return db.fetchall()
    # return the list of the top ordered product by each customer based on the total ordered amount
    #pass  # YOUR CODE HERE

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    pass  # YOUR CODE HERE
