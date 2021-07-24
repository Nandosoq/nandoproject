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
    pass  # YOUR CODE HERE

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    pass  # YOUR CODE HERE

def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer based on the total ordered amount
    pass  # YOUR CODE HERE

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    pass  # YOUR CODE HERE
