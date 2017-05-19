# logs-analysis
Reporting tool that summarizes data from a large database (just messing around with python and SQL).

Prerequisites
-------------
1. Python
2. psycopg2
3. PostgreSQL
4. Database populated according to Log Analysis Project (udacity)

Database: How to Create the Views
-----------------------------
Log into the PostgreSQL from the command line: `psql`.

Use the command `\i create_views.sql` to import the whole file into psql at once.

Log out from PostgreSQL `\q`.

How to Run the Analysis
-------------------------
After building up the database, use the command `python main.py`.
