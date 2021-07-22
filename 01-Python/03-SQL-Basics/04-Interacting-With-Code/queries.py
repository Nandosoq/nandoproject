# pylint: disable=missing-docstring, C0103

def directors_count(db):
    query = 'SELECT count(*) FROM directors d'
    db.execute(query)
    rows = db.fetchone()
    return rows[0]

def directors_list(db):
    query = 'SELECT name FROM directors d ORDER BY name ASC'
    db.execute(query)
    rows = db.fetchall()
    list_direct = []
    for row in rows:
        list_direct.append(row[0])
    return list_direct

def love_movies(db):
    query = "SELECT title FROM movies WHERE title LIKE '%love%' ORDER BY title ASC"
    db.execute(query)
    rows = db.fetchall()
    list_love = []
    for row in rows:
        list_love.append(row[0])
    return list_love

def directors_named_like_count(db, name):
    query = "SELECT count(*) from directors d WHERE name LIKE '%" + name + "%'"
    db.execute(query)
    rows = db.fetchone()
    return rows[0]

def movies_longer_than(db, min_length):
    query = "SELECT title from movies GROUP BY id HAVING minutes >'" + str(
        min_length) + "' ORDER BY title ASC"
    db.execute(query)
    rows = db.fetchall()
    list_film_lenght = []
    for row in rows:
        list_film_lenght.append(row[0])
    return list_film_lenght
