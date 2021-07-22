# pylint: disable=C0103, missing-docstring

def detailed_movies(db):

    query = 'SELECT m.title, m.genres, d.name from movies m JOIN directors d ON  d.id = m.director_id'
    db.execute(query)
    rows = db.fetchall()
    return rows


def late_released_movies(db):
    query = 'SELECT m.title, CASE WHEN m.start_year>d.death_year THEN 1 ELSE 0 END AS death from movies m JOIN directors d ON d.id = m.director_id GROUP BY m.title HAVING death = 1 ORDER BY m.title ASC'
    db.execute(query)
    rows = db.fetchall()
    list_mov = []
    for row in rows:
        list_mov.append(row[0])
    return list_mov

def stats_on(db, genre_name):
    query ="SELECT genres, COUNT(*), AVG(minutes) FROM movies WHERE genres IS '" + genre_name + "'"
    db.execute(query)
    rows = db.fetchone()
    result = {
        'genre': rows[0],
        'number_of_movies': rows[1],
        'avg_length': round(rows[2],2)
    }
    return result
    '''return a dict of stats for a given genre'''

def top_five_directors_for(db, genre_name):
    query = "SELECT d.name, count(d.name) as contar FROM directors d join movies m on d.id = m.director_id WHERE m.genres ='" + genre_name  + "' GROUP BY d.name ORDER BY contar DESC, d.name ASC LIMIT 5"
    db.execute(query)
    rows = db.fetchall()
    #list_5 = []
    #for row in rows:
    #    list_5.append(row[1])
    return rows
    '''return the top 5 of the directors with the most movies for a given genre'''

def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    query = "SELECT d.name, (m.start_year -  d.birth_year) as age FROM directors d join movies m on d.id = m.director_id WHERE AGE <>'' ORDER BY age ASC LIMIT 5"
    db.execute(query)
    rows = db.fetchall()
    return rows
    '''return the top 5 youngest directors when they direct their first movie'''
    #pass  # YOUR CODE HERE
