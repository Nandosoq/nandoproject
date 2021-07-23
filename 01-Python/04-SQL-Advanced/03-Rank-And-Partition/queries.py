# pylint:disable=C0111,C0103

def order_rank_per_customer(db):

    query = '''
    SELECT
	o.OrderID, o.CustomerID, o.OrderDate,
	RANK() OVER(
	PARTITION BY o.CustomerID
	ORDER BY o.OrderDate
	) AS OrderRank
    FROM Orders o
    '''

    db.execute(query)
    return db.fetchall()


def order_cumulative_amount_per_customer(db):
    query = '''
    SELECT DISTINCT od.OrderID, o.CustomerID, o.OrderDate,
    SUM(od.UnitPrice*od.Quantity) OVER (
    PARTITION BY o.CustomerID
    ORDER BY o.OrderDate
    ) AS OrderCumulativeAmount
    FROM OrderDetails od
    INNER JOIN Orders o ON od.OrderID = o.OrderID
    '''

    db.execute(query)
    return db.fetchall()
