# \list shows all databases
# \c name_database     connect to database
# \dt  or \d  show tables in database
# \d <table name>   show info about table name

# pip3 install psycopg2-binary

# Like SQLite3 and MySQL Connector, the Psycopg2 module is compliant with the Python database API. This means
# interacting with this module will look pretty similar to how we've used the other modules with other database
# management systems. However, under the hood, a different database management system is being used with Psycopg2,
# it's Postgres.

# \copy <table name> FROM '/User/local/desktop/file.csv' WITH DELIMITER ',' CSV HEADER; copy data from CSV file to table

#                                 SQLAlchemy Core example


# from sqlalchemy import create_engine
# from sqlalchemy import Table, MetaData
#
# engine = create_engine('postgresql://postgres:19865421@localhost:5432/test1')
#
#
# with engine.connect() as connection:
#     meta = MetaData(engine)
#     house_table = Table('house', meta, autoload=True, autoload_with=engine)
#
#     # insert data into table
#
#     insert_room = house_table.insert().values(room_id=10,
#                                               house_room='kitchen',
#                                               room_description='for cooking')
#     connection.execute(insert_room)
#
#     select_room = house_table.select().limit(10)
#     result = connection.execute(select_room)
#
#     for r in result:
#         print(r)
#
#     # update room
#
#     update_room = house_table.update().where(house_table.c.room_id == 5).values(room_description='room for children',
#                                                                               house_room='playing_room')
#     connection.execute(update_room)
#
#     print("**********************")
#
#     # select
#
#     select_info_room = house_table.select().where(house_table.c.house_room == 'bedroom')
#     result_2 = connection.execute(select_info_room)
#     print(f'founded rows: {result_2.rowcount}')
#
#     for r in result_2:
#         print(r)
#
#     # delete room
#     delete_room = house_table.delete().where(house_table.c.room_id == 10)
#     connection.execute(delete_room)

#                           SQLAlchemy ORM

# from sqlalchemy import create_engine, func
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
#
# engine = create_engine('postgresql://postgres:19865421@localhost:5432/test1')
# Base = declarative_base(engine)
# Base.metadata.reflect(engine)
# # Base.metadata.reflect and pass in the engine. What this call means is communicate with the database, read it, and have
# # our base object reflect that database and the data that's in it. So that includes the tables, the columns, all of that
# # good stuff. Why is it useful? Well, when we create our Sales class, we can just read in that table data with the
# # base.metadata.tables and pass in the name of the table that we want to read the data from. This will pass in all the
# # metadata about that sales table, so that when we create this class, all we have to do is write a two string function
# # or a string representation of this object.
#
#
# class House(Base):
#     __table__ = Base.metadata.tables['house']
#
#     def __repr__(self):
#         return '''<Rom in the house: {0}, description of room: {1}>'''.format(self.house_room, self.room_description)
#
#
# def loadSession():
#     ''' This configures the session that we can use to interact with our database. '''
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session
#
#
# if __name__ == '__main__':
#     session = loadSession()
#
#     # Read
#     house_info = session.query(House).order_by(House.room_id).limit(10)
#     for room in house_info:
#         print(room)
#     print(house_info[1].room_id)
#
#     # Insert
#     insert_room = House(room_id=14, house_room='wardrobe', room_description='for storing cloth')
#     print(insert_room)
#     session.add(insert_room)
#     session.commit()
#
#     # Update
#     update_room = session.query(House).filter(House.room_id == 6).first()
#     update_room.room_description = 'children bath'
#     session.commit()
#
#     # Delete
#     session.delete(session.query(House).filter(House.room_id == 14).first())
#     session.commit()


# A stored procedure is prepared SQL code that usually consists of several SQL statements that are saved and reused
# over and over again.

# We are using the SQLAlchemy name or our Python name inside of this relationship because relationship is for SQLAlchemy
# . It's not for Postgres. For Postgres, we provide these ForeignKeys, and so we have the authors.author_id. Authors is
# the name of the table, as we set here, and books is also the name of the table. That sets us up for the Postgres side.

# session.add(author)
# session.flush()
#  we'll add that author that we created up here, then we'll do session.flush. This will send a series of operations to
#  the database, think insert, update, delete, whatever we're doing, in this case, it's an add, but they're going to
#  still be pending operations until a commit is received. What this really does is update our author with an author id
#  so that when we add the pairing, we can pass in that author id. It's already generated for us with this flush.

# CREATE ROLE myuser WITH LOGIN PASSWORD 'password';
# create a new user in the postgres shell that requires a password

# retrieve a table reference from a database using SQLAlchemy Core in Python
# Create an engine and create a metadata object with the engine. Then, retrieve the table with
# Table('myTable', metadataObject, autoload=True, autoload_with=engine)

#   task = db.relationship('Task', cascade='all, delete-orphan')    will also delete the task objects if they become
#   disassociated with the project object.


#                           PROCEDURE
# \h CREATE PROCEDURE   will show help about creating procedure in PostgreSQL
# CREATE OR REPLACE PROCEDURE return_nondiscounted_item(INT, INT)
# So this will overwrite the procedure if we already have a procedure of this type. In this case, the name of the
# procedure is going to be return non-discounted item. And it's going to have two parameters. The first will be an order
# ID, which is an int, and the second will also be an int, it'll be the number of items to be returned.

#