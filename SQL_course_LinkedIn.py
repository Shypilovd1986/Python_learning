#                       MYSQL
# if not find mysql in terminal !!!!
# virtualenv mysql-workspace    create virtual env in terminal
# cd mysql-workspace
# source  bin/activate
# pip3 install mysql-connector-python

# my_db = mysql.connect(
#             host='localhost',
#             user='root',
#             password='19865421',
#             database=db_name,
#             allow_local_infile=True   !!!!!  add data from file
#         )

# q = '''LOAD DATA LOCAL INFILE '/Users/author/desctop/mysql-csv/sales.scv'
# INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"'
# (first_name, email, city);'''
# cursor.execute(q)

    # sudo nano /etc/paths
    # /usr/local/mysql/bin
    # /usr/local/mysql/support-files

# CREATE DATABASE project;
# use project;    switch to project database
# CREATE TABLE users(user_id INT AUTO_INCREMENT NOT NULL, name VARCHAR(20),surname VARCHAR(20),PRIMARY KEY(user_id));

# CREATE TABLE IF NOT EXISTS tasks(task_id INT NOT NULL AUTO_INCREMENT, user_id INT NOT NULL, task_name VARCHAR(20),
#  description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY(user_id) REFERENCES users(user_id));

# cursor.lastrowid    takes last id in row

# show tables;    show existing tables

# describe users;   show information about table users, it's columns
#
#  \q   exit from the MySQL server

# cursor.executemany('''INSERT INTO tasks(user_id, task_name, description) VALUES(%s, %s, %s)''', task_list)
# execute many commands



# DML data manipulation language (INSERT, SELECT, UPDATE, DELETE)
# DDL data definition language   (CREATE, DROP, TRUNCATE, ALTER, RENAME) DDL statements are autocommit !!!!!!!
# DCL
# TCL transaction control language (COMMIT, ROLLBACK, SAVEPOINT)

# A transaction begins when the first DML statement is executed, and it ends in three different scenarios. When COMMIT
# or ROLLBACK is issued, or when a DDL or DCL statement is executed, autocommit will occur. And the third scenario is if
# the user exits the system or the system crashes.

#  Rollback discard all pending data changes and ends the current transaction. Savepoint creates a marker point within
#  a transaction. By using commit and rollback we can preview the data changes before making them permanent.

#

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

# a cursor object for maintaining context in a sequence of query responses,
# c = con.cursor
# c.execute("SELECT * FROM books")

# !!!!   Cursors in the DB-API serve two purposes. They act as iterators keeping track of a position in the database.
# This allows your code to step through a query result without the need to hold more than one row at a time in active
# memory. In the DB-API implementation, cursors also act as prepared statements. This allows you to use placeholders in
# a query, provides automatic sanitation of parameters and significant performance improvements.
# for row in c.execute("SELECT * FROM books"):
#     print(row)

# common hooks for committing and rolling back transactions,
# con.commit()
# con.rollback()
#
# and a common set of exceptions for catching errors from the DBMS.
# try:
#     con.execute("INSERT INTO books (book_name) VALUES ("Konan Doil")")
# except sqlite3.Error:
#     print("cannot add duplicate book")
#
# Each DBMS has its own implementation, which may include different connection details.

# SELECT VERSION();    show version of your mysql server

#                       Grouping Data
# SELECT YEAR(sb_start) as year, COUNT(sb_book) AS quantity_book FROM subscriptions GROUP BY year ORDER BY year;
#
# SELECT IF(sb_is_active='Y', 'Not returned', 'Returnd' ) AS status, COUNT(sb_id) FROM subscriptions GROUP BY status ORDER BY status;

#
# SELECT b_name, a_name, g_name
# FROM books
# 	JOIN m2m_books_authors USING (b_id)
#     JOIN authors USING (a_id)
#     JOIN m2m_books_genres USING(b_id)
#     JOIN genres USING(g_id);

#
# SELECT b_name,
# 	   s_id,
#        s_name,
#        sb_start,
#        sb_finish
# FROM books
# 	JOIN subscriptions ON b_id=sb_book
#     JOIN subscribers ON sb_subscriber=s_id;

# SELECT b_id, b_name, a_id, quantity_writen_book, a_name FROM books
#   JOIN m2m_books_authors USING(b_id)
#   JOIN authors USING(a_id)
#   JOIN (SELECT a_id, COUNT(a_id) AS quantity_writen_book FROM m2m_books_authors  GROUP BY a_id) AS d_table USING(a_id)
# WHERE quantity_writen_book >1;

#
# SELECT b_id, b_name FROM books
# 	JOIN m2m_books_genres USING(b_id)
#     JOIN genres USING(g_id)
#     JOIN (SELECT g_id,COUNT(g_id) AS quantity_genres FROM m2m_books_genres GROUP BY g_id) AS g_table USING(g_id)
# WHERE quantity_genres = 1;

# SELECT  b_name AS book
#     GROUP CONCAT (DISTINCT a_name ORDER BY a_name SEPARATOR ',') AS authors ,
#     GROUP CONCAT (DISTINCT g_name ORDER BY g_name SEPARATOR ',') AS genres
# FROM books
#   JOIN m2m_books_authors USING(b_id)
#   JOIN authors USING(a_id)
#   JOIN m2m_books_genres USING(b_id)
#   JOIN genres USING(g_id)
# GROUP BY b_id
# ORDER BY b_name

# DESCRIBE table_name;   or DESC table_name;    describe table !!!!!! type of value, quantity of column, primary key ...

# types of constraint
# PRIMARY KEY
# FOREIGN KEY
# NOT NULL
#                                DDL statements!!!!!!!!

#                               Синтаксис оператора ALTER TABLE
#
# ALTER [IGNORE] TABLE tbl_name alter_spec [, alter_spec ...]
# alter_specification:
#         ADD [COLUMN] create_definition [FIRST | AFTER column_name ]
#   или   ADD [COLUMN] (create_definition, create_definition,...)
#   или   ADD INDEX [index_name] (index_col_name,...)
#   или   ADD PRIMARY KEY (index_col_name,...)
#   или   ADD UNIQUE [index_name] (index_col_name,...)
#   или   ADD FULLTEXT [index_name] (index_col_name,...)
#   или   ADD [CONSTRAINT symbol] FOREIGN KEY [index_name] (index_col_name,...)
#             [reference_definition]
#   или   ALTER [COLUMN] col_name {SET DEFAULT literal | DROP DEFAULT}
#   или   CHANGE [COLUMN] old_col_name create_definition
#                [FIRST | AFTER column_name]
#   или   MODIFY [COLUMN] create_definition [FIRST | AFTER column_name]
#   или   DROP [COLUMN] col_name
#   или   DROP PRIMARY KEY
#   или   DROP INDEX index_name
#   или   DISABLE KEYS
#   или   ENABLE KEYS
#   или   RENAME [TO] new_tbl_name
#   или   ORDER BY col
#   или   table_options

# CREATE TABLE IF NOT EXISTS user (u_id INT AUTO_INCREMENT PRIMARY KEY,
# user_name VARCHAR(20) NOT NULL,
# card_name INT UNIQUE NOT NULL
# )
#
# SELECT * FROM user;
#
# INSERT INTO user (user_name, card_name) VALUES ('Dmitriy', 2322332);
#
# DESC user;
#
# CREATE TABLE IF NOT EXISTS bank_info (bank_id INT AUTO_INCREMENT PRIMARY KEY,
# 									 account_info VARCHAR(100),
#                                      user_id INT NOT NULL,
#                                      FOREIGN KEY(user_id) REFERENCES user(u_id)
# );
#
# CREATE TABLE subscriber_info AS (SELECT sb_id, sb_book, sb_subscriber FROM subscriptions );
#
# DESC subscriber_info;
#
# SELECT * FROM subscriber_info;
#
# ALTER TABLE subscriber_info ADD (age INT NOT NULL);
#
# ALTER TABLE subscriber_info MODIFY age SMALLINT NOT NULL;
#
# ALTER TABLE subscriber_info DROP COLUMN age;

# DROP TABLE table_name;

# TRUNCATE TABLE table_name;    delete table and release all storage space used by the table

# RENAME old_name_table TO new_name;

#  CGI is, in this context, the common gateway interface. It's one of the original web protocols dating back to the
#  early 1990s. CGI is how we pass information back and forth between a web browser and a web server.

# Keep in mind that the web is inherently stateless. This means that each time a web browser submits information back
# to the web server, it does not know what just happened unless your script keeps track. T

# show table status;     in MYSQL  you can get a different set of details

# show create table table_name     show information about consist of table in MYSQL

# show variables;   show all variables of mysql server

# show variables like 'time%';    show all variables which start with 'time'

# SET time_zone = '+00:00';   we can set our time zone   , if 'system' time zone , will show time, where computer stands

# select now();   show present time and date

# select utc_timestamp();   show time and date in ' 00:00 ' zone

# type TIMESTAMP    The timestamp is supposed to automatically update. !!!
# stamp DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

# select 10 mod 7 ;  result 3 is the same as 10%7
# select 10 // 7 ; result 1 is the same as 10 // 7

# SELECT
#     CASE  WHEN a < 5 THEN 'true' ELSE 'false' END AS boola,
#     CASE  WHEN b < 5 THEN 'true' ELSE 'false' END AS boolb,
#     FROM table_name
# ;

# SELECT IF (age < 20, 'true', 'false') FROM table_name;

# XOR   For an output of true, either the left side or the right side must be true, but not both.

# SELECT name FROM teacher WHERE name RLIKE 'regular expression' ORDER BY name;
# use regular expression

# SELECT CONCAT('hello', 'world', '!')    will concatenate string

# SELECT OCT(343);  show octal equivalent of number 343
# SELECT HEX(343);  same for hex decimal number 343
# SELECT BIN(343);
# SELECT CONV(343, 10, 16)  convert number 343 from decimal to hex decimal
# SELECT CONV('157 ', 16, 10)  convert number 343 from decimal to hex decimal
# SELECT LOWER(name) from teacher;
# SELECT UPPER(name) from teacher;

# SELECT SUBSTRING('hello world', 4)    return 'lo world'  from 4 symbol,  -4 will return from the end 4 symbol

# SELECT CEILING(AVG(age)) AS 'average age' from teacher;
# SELECT ROUND(age) from teacher;
# SELECT FLOOR(age) from teacher;
# SELECT TRUNCATE(3,23) ;    ----->    takes only integer part

# SELECT SIN(2):
# SELECT TAN(PI());
# SELECT COS(2);
# SELECT ACOS(2);

# SELECT LOG(10, 100)
# SELECT LOG(2, 654)

# SELECT EXP(4);
# SELECT RADIANS(180);
# SELECT DEGREES(PI());

# SELECT 20 DIV 3; --> 6, 20//3 integer division
# SELECT MOD(20, 3) -->2   same 20%3

#   /*
#       comments in mysql
#   */

# -- text   comment in mysql
# # text    comment in mysql

# example how create table with constraint foreign key

# mysql> create table studying(id serial, teacher_id int , pupil_id int, foreign key(teacher_id) references teacher(id),
# foreign key(pupil_id) references pupil(id));