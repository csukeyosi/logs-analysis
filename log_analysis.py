import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def execute(has_commit, query, *params):
    """
    Connects to the PostgreSQL database, executes the query and returns
    the rows, if any.
    """
    db = connect()
    c = db.cursor()

    if params:
        c.execute(query, params)
    else:
        c.execute(query)

    rows = []
    if has_commit:
        db.commit()
    else:
        rows = c.fetchall()

    db.close()

    return rows


def mostPopularArticle():
    """
    Retrieves and prints the articles that the most have been accessed (top 3).
    """
    query = 'SELECT * FROM top_articles LIMIT 3'
    rows = execute(False, query)
    for i in range(len(rows)):
        print '%s - %s views' % (rows[i][0], rows[i][1])


def mostPopularAuhtor():
    """
    Retrieves and prints the authors that the most have been accessed (top 10).
    """
    query = 'SELECT * FROM top_authors LIMIT 10'
    rows = execute(False, query)
    for i in range(len(rows)):
        print '%s - %s views' % (rows[i][0], rows[i][1])


def daysMoreOnePerErrors():
    """
    Retrieves and prints the days that the most have had errors > 1.
    """
    query = 'select * from errors_per_day where errors_perc > 1'
    rows = execute(False, query)
    for i in range(len(rows)):
        print '%s - %s%%' % (rows[i][0], rows[i][1])
