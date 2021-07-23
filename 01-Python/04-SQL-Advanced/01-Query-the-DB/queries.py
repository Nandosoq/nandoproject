# pylint:disable=C0111,C0103

def query_orders(db):
    query ='''
        SELECT *
        FROM  Orders o
        ORDER BY OrderID ASC
    '''
    db.execute(query)
    return db.fetchall()


def get_orders_range(db, date_from, date_to):
    query = '''
        SELECT *
        FROM  Orders o
        WHERE OrderDate > ? AND OrderDate < ?
    '''
    db.execute(query, (date_from, date_to))
    #db.execute(query)
    return db.fetchall()

    # return a list of orders displaying all columns with OrderDate between date_from and date_to


def get_waiting_time(db):

    query = '''
        SELECT *, (julianday(o.ShippedDate) - julianday(o.OrderDate))  AS TimeDelta
        FROM  Orders o
        ORDER BY TimeDelta ASC
    '''
    db.execute(query)
    return db.fetchall()

    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    #pass  # YOUR CODE HERE
