# DML 
# DDL
# DCL
# TCL

# SELECT * FROM 'table_name';    all data selection

# SELECT DISTINCT 'sb_subscriber' FROM 'subscriptions';  show without duplication !! DISTINCT analyze all line not just
# one row sb_subscriber

# SELECT s_name, COUNT(*) AS people_count
# FROM subscribers
# GROUP BY s_name;

# COUNT(*)                       Classic approach, shows total count.
# COUNT(1)                       Alternative notation for the classic approach.
# COUNT(PrimaryKey)              Alternative notation for the classic approach.
# COUNT(FieldName)               Shows count of all not NULL values.
# COUNT(DISTINCT FieldName)      Shows count of all not NULL values without duplication.

#
# SELECT COUNT(sb_book) AS count_taken_book FROM subscriptions WHERE sb_is_active = 'Y';
#
# SELECT COUNT(DISTINCT sb_book) AS count_taken_book FROM subscriptions WHERE sb_is_active = 'Y';

#
# SELECT COUNT(s_name) AS count_subscribers FROM subscribers;
#
# SELECT COUNT(sb_id) AS count_taken_book FROM subscriptions;

# SELECT MIN(sb_finish) FROM subscriptions;

# SELECT b_name, b_year FROM books ORDER BY b_year  ASC;   or DESC

# compound conditions
# SELECT b_year, b_name, b_quantity FROM books WHERE b_year BETWEEN 1990 AND 2000 AND b_quantity >= 3;

# SELECT b_year, b_name, b_quantity FROM books WHERE b_year >= 1990 AND b_year <= 2000 AND b_quantity >= 3;
# double inequality

# SELECT b_id, b_quantity FROM books WHERE b_quantity < (SELECT AVG(b_quantity) FROM books);

#!!!! When you need to use an aggregate function inside a WHERE clause, you need to wrap the aggregate function call in
# a subquery.

# SELECT sb_id, sb_book FROM subscriptions WHERE sb_book = (SELECT MAX(sb_book) FROM subscriptions);

# SELECT AVG(DATEDIFF(sb_finish, sb_start)) AS avg_days FROM subscriptions WHERE sb_is_active='N';

# CURDATE()   function show current day
# YEAR('some date')  extract year from date

# Python uses a standard interface called DB-API to communicate with the database.
#  The purpose of the DB-API is to promote commonality among interfaces so that each database management system uses
#  more or less the same code to access data from Python. The DB-API is feature complete, including support for all
#  common relational database operations.

#                               connect parameters !!!!!!! :
# sqlite3.connect("db_name")      for SQLite3
#
# mysql.connector.connect(        for MySQL
#   user = "Dmitriy",
#   password = "11111111",
#   host = "127.0.0.1",
#   database = "db_name"
# )

# psycopg2.connect("dbname=db_name user=Dmitriy password=1111111")    for PostgreSQL

# pyodbc.connect(                       MS SQL Server
#   "DRIVER={ODBC Driver 17 for SQL Server}" + ";SERVER=" + server + ";DATABASE=" + database + ";UID=" + username
#   + ";PWD=" + password
# )

#