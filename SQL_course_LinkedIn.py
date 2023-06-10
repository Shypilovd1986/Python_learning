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

#