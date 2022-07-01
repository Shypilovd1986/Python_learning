# class Animal:
#     def __init__(self, **kwargs):
#         if 'type' in kwargs: self._type = kwargs['type']
#         if 'name' in kwargs: self._name = kwargs['name']
#         if 'sound' in kwargs: self._sound = kwargs['sound']
#
#     def type(self, t = None):
#         if t: self._type = t
#         try: return self._type
#         except AttributeError: return None
#
#     def name(self, n = None):
#         if n: self._name = n
#         try: return self._name
#         except AttributeError: return None
#
#     def sound(self, s = None):
#         if s: self._sound = s
#         try: return self._sound
#         except AttributeError: return None
#
# class Duck(Animal):
#     def __init__(self, **kwargs):
#         self._type = 'duck'
#         if 'type' in kwargs: del kwargs['type']
#         super().__init__(**kwargs)
#
# class Kitten(Animal):
#     def __init__(self, **kwargs):
#         self._type = 'kitten'
#         if 'type' in kwargs: del kwargs['type']
#         super().__init__(**kwargs)
#
# def print_animal(o):
#     if not isinstance(o, Animal):
#         raise TypeError('print_animal(): requires an Animal')
#     print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')
#
# def main():
#     a0 = Kitten(name = 'fluffy', sound = 'rwar')
#     a1 = Duck(name = 'donald', sound = 'quack')
#     print_animal(a0)
#     print_animal(a1)
#
# if __name__ == '__main__': main()

# ************************      #2        *************************
#
# import sys
# try:
#     x = 3/0
# except ZeroDivisionError as hotfix:
#     print(f'I don\'t know what happened {sys.exc_info()[1]}')

# **************************      #3       ************************
# s = 'It\'s a good' ' day'
# print(s)

# **************************      $4        ***********************
# x = 42
# print('number in binary is {:b}'.format(x))
# print('number in octal is {:o}'.format(x))
# print('number in hexadecimal is {:x}'.format(x))
# print(f'number in binary is {x:b}')
# f = open(r'C:\\spam.txt')
# for i in f:
#     print(i)

# *************************        #5          ********************
#  x ='43'
# int(x)   ->
# actually int() it's not a function , it's a constructor for the int type
# same for float(), str(), list()

# ***********************          #6          *********************
# x = 47
# y = divmod(x, 3)
# print(y, type(y))
# divmod returns quotient and a reminder

# x = 10
# y1 = complex(x,73)  #-> (10+73j)
# y2 = x + 73j # -> (10+73j), type of y2 and y1 are tuples
# print(y1, type(y1))
# print(y2)
# j in Python is imaginary part of number

# ************************        #7         ***********************
# class Int_test():
#     def __init__(self, n):
#         self.n = n
#
#     def __repr__(self):
#         return f'repr : like this '
#
# x = Int_test(3)
# print(x)
# print(repr(x))
# print(ascii(x))   #represintatin only with ascii characters
# print(chr(43))   # return  unicode position

# ************************        #8         ***********************
# x = (3,2,1,55)
# y = reversed(x)
# print(y)
# # <reversed object at 0x000001BA76D39160>
# for i in y:
#     print(i)

# ***********************           #9           *********************
# import sys
# import time
#
# __version__ = '1.3.0'
#
# class numwords():
#     '''
#         return a number as words,
#         e.g., 42 becomes 'forty-two'
#     '''
#     _words = {
#         'ones': (
#             'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
#         ), 'tens': (
#             '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
#         ), 'teens': (
#             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
#         ), 'quarters': (
#             'o\'clock', 'quarter', 'half'
#         ), 'range': {
#             'hundred': 'hundred'
#         }, 'misc': {
#             'minus': 'minus'
#         }
#     }
#     _oor = 'OOR'    # Out Of Range
#
#     def __init__(self, n):
#         self._number = n
#
#     def numwords(self, num = None):
#         'Return the number as words'
#         n = self._number if num is None else num
#         s = ''
#         if n < 0:           # negative numbers
#             s += self._words['misc']['minus'] + ' '
#             n = abs(n)
#         if n < 10:          # single-digit numbers
#             s += self._words['ones'][n]
#         elif n < 20:        # teens
#             s += self._words['teens'][n - 10]
#         elif n < 100:       # tens
#             m = n % 10
#             t = n // 10
#             s += self._words['tens'][t]
#             if m: s += '-' + numwords(m).numwords()    # recurse for remainder
#         elif n < 1000:      # hundreds
#             m = n % 100
#             t = n // 100
#             s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
#             if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
#         else:
#             s += self._oor
#         return s
#
#     def number(self, n = None):
#         'setter/getter'
#         if n is not None:
#             self._number = n
#         return str(self._number);
#
# class saytime(numwords):
#     '''
#         return the time (from two parameters) as words,
#         e.g., fourteen til noon, quarter past one, etc.
#     '''
#
#     _specials = {
#         'noon': 'noon',
#         'midnight': 'midnight',
#         'til': 'til',
#         'past': 'past'
#     }
#
#     def __init__(self, h = None, m = None):
#         self.time(h, m)
#
#     def time(self, h = None, m = None):
#         if h is not None:
#             self._hour = abs(int(h))
#         if m is not None:
#             self._min = abs(int(m))
#         return (h, m)
#
#     def time_t(self, t = None):
#         if t is None:
#             t = time.localtime()
#         self._hour = t.tm_hour
#         self._min = t.tm_min
#
#     def words(self):
#         h = self._hour
#         m = self._min
#
#         if h > 23: return self._oor     # OOR errors
#         if m > 59: return self._oor
#
#         sign = self._specials['past']
#         if self._min > 30:
#             sign = self._specials['til']
#             h += 1
#             m = 60 - m
#         if h > 23: h -= 24
#         elif h > 12: h -= 12
#
#         # hword is the hours word)
#         if h == 0: hword = self._specials['midnight']
#         elif h == 12: hword = self._specials['noon']
#         else: hword = self.numwords(h)
#
#         if m == 0:
#             if h in (0, 12): return hword   # for noon and midnight
#             else: return "{} {}".format(self.numwords(h), self._words['quarters'][m])
#         if m % 15 == 0:
#             return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword)
#         return "{} {} {}".format(self.numwords(m), sign, hword)
#
#     def digits(self):
#         'return the traditionl time, e.g., 13:42'
#         return f'{self._hour:02}:{self._min:02}'
#
# class saytime_t(saytime):   # wrapper for saytime to use time object
#     '''
#         set the time from a time object
#     '''
#     def __init__(self, t = None):
#         self.time_t()
#
# def main():
#     if len(sys.argv) > 1:
#         if sys.argv[1] == 'test':
#             test()
#         else:
#             try: print(saytime(*(sys.argv[1].split(':'))).words())
#             except TypeError: print('Invalid time ({})'.format(sys.argv[1]))
#     else:
#         print(saytime_t().words())
#
# def test():
#     st = saytime()
#     print('\nnumbers test:')
#     list = (
#         0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30,
#         50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000
#     )
#     for l in list:
#         st.number(l)
#         print(l, st.numwords())
#
#     print('\ntime test:')
#     list = (
#         (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
#         (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
#         (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
#     )
#     for l in list:
#         st.time(*l)
#         print(st.digits(), st.words())
#
#     st.time_t() # set time to now
#     print('\nlocal time is ' + st.words())
#
# if __name__ == '__main__': main()

# *************************          #10          **************************
# import sys
# import os
# import datetime
#
#
# def main():
#     v = sys.version_info
#     p = sys.platform
#     n = os.name
#     now = datetime.datetime.now()
#     current_directory = os.getcwd()  # shows current directory
#     os_random = os.urandom(23) #from operation system random generator  23 bytes long
#     os_random_hex = os.urandom(34).hex()
#     env = os.getenv('PATH')  # return path
#     print('Python version {}.{}.{}'.format(*v), f'platform is {p}, operation system is {n}')
#     print(f' path is {env}')
#     print(f'My current directory is {current_directory}')
#     print(f'Random number is {os_random}, type is {type(os_random)}')
#     print(os_random_hex)
#     print(f'Now is {now}')
#     print(type(now.year), now.year)
#
# if __name__ == '__main__': main()

#************************          #11             ******************
# with open(r'C:\ex.txt', 'w') as file:
#     file.write('What a wonderful day today')

# *****************          #12            ***************
# import sqlite3
# #
# # def main():
# #     print('connect')
# #     db = sqlite3.connect('db-api.db')
# #     cur = db.cursor()
# #     print('create')
# #     cur.execute("DROP TABLE IF EXISTS test")
# #     cur.execute("""
# #         CREATE TABLE test (
# #             id INTEGER PRIMARY KEY, string TEXT, number INTEGER
# #         )
# #         """)
# #     print('insert row')
# #     cur.execute("""
# #         INSERT INTO test (string, number) VALUES ('one', 1)
# #         """)
# #     print('insert row')
# #     cur.execute("""
# #         INSERT INTO test (string, number) VALUES ('two', 2)
# #         """)
# #     print('insert row')
# #     cur.execute("""
# #         INSERT INTO test (string, number) VALUES ('three', 3)
# #         """)
# #     print('commit')
# #     db.commit()
# #     print('count')
# #     cur.execute("SELECT COUNT(*) FROM test")
# #     count = cur.fetchone()[0]
# #     print(f'there are {count} rows in the table.')
# #     print('read')
# #     for row in cur.execute("SELECT * FROM test"):
# #         print(row)
# #     print('drop')
# #     cur.execute("DROP TABLE test")
# #     print('close')
# #     db.close()
# #
# # if __name__ == '__main__': main()


# import sqlite3
d = {'filename':'db'}
print(d.get('filename'))

# #  ***************   example of finished database


# import sqlite3
#
# __version__ = '1.2.0'
#
# class bwDB:
#     def __init__(self, **kwargs):
#         """
#             db = bwDB( [ table = ''] [, filename = ''] )
#             constructor method
#                 table is for CRUD methods
#                 filename is for connecting to the database file
#         """
#         # see filename @property decorators below
#         self._filename = kwargs.get('filename')
#         self._table = kwargs.get('table', '')
#
#     def set_table(self, tablename):
#         self._table = tablename
#
#     def sql_do(self, sql, params=()):
#         """
#             db.sql_do( sql[, params] )
#             method for non-select queries
#                 sql is string containing SQL
#                 params is list containing parameters
#             returns nothing
#         """
#         self._db.execute(sql, params)
#         self._db.commit()
#
#     def sql_do_nocommit(self, sql, params=()):
#         """
#             sql_do_nocommit( sql[, params] )
#             method for non-select queries *without commit*
#                 sql is string containing SQL
#                 params is list containing parameters
#             returns nothing
#         """
#         self._db.execute(sql, params)
#
#     def sql_query(self, sql, params=()):
#         """
#             db.sql_query( sql[, params] )
#             generator method for queries
#                 sql is string containing SQL
#                 params is list containing parameters
#             returns a generator with one row per iteration
#             each row is a Row factory
#         """
#         c = self._db.execute(sql, params)
#         for r in c:
#             yield r
#
#     def sql_query_row(self, sql, params=()):
#         """
#             db.sql_query_row( sql[, params] )
#             query for a single row
#                 sql is string containing SQL
#                 params is list containing parameters
#             returns a single row as a Row factory
#         """
#         c = self._db.execute(sql, params)
#         return c.fetchone()
#
#     def sql_query_value(self, sql, params=()):
#         """
#             db.sql_query_row( sql[, params] )
#             query for a single value
#                 sql is string containing SQL
#                 params is list containing parameters
#             returns a single value
#         """
#         c = self._db.execute(sql, params)
#         return c.fetchone()[0]
#
#     def commit(self):
#         self._db.commit()
#
#     def getrec(self, recid):
#         """
#             db.getrec(recid)
#             get a single row, by id
#         """
#         query = f'SELECT * FROM {self._table} WHERE id = ?'
#         c = self._db.execute(query, (recid,))
#         return c.fetchone()
#
#     def getrecs(self):
#         """
#             db.getrecs()
#             get all rows, returns a generator of Row factories
#         """
#         query = f'SELECT * FROM {self._table}'
#         c = self._db.execute(query)
#         for r in c:
#             yield r
#
#     def insert_nocommit(self, rec):
#         """
#             db.insert(rec)
#             insert a single record into the table
#                 rec is a dict with key/value pairs corresponding to table schema
#             omit id column to let SQLite generate it
#         """
#         klist = sorted(rec.keys())
#         values = [rec[v] for v in klist]  # a list of values ordered by key
#         q = 'INSERT INTO {} ({}) VALUES ({})'.format(
#             self._table,
#             ', '.join(klist),
#             ', '.join('?' * len(values))
#         )
#         c = self._db.execute(q, values)
#         return c.lastrowid
#
#     def insert(self, rec):
#         lastrowid = self.insert_nocommit(rec)
#         self._db.commit()
#         return lastrowid
#
#     def update_nocommit(self, recid, rec):
#         """
#             db.update(id, rec)
#             update a row in the table
#                 id is the value of the id column for the row to be updated
#                 rec is a dict with key/value pairs corresponding to table schema
#         """
#         klist = sorted(rec.keys())
#         values = [rec[v] for v in klist]  # a list of values ordered by key
#
#         for i, k in enumerate(klist):  # don't udpate id
#             if k == 'id':
#                 del klist[i]
#                 del values[i]
#
#         q = 'UPDATE {} SET {} WHERE id = ?'.format(
#             self._table,
#             ',  '.join(map(lambda s: '{} = ?'.format(s), klist))
#         )
#         self._db.execute(q, values + [recid])
#
#     def update(self, recid, rec):
#         self.update_nocommit(recid, rec)
#         self._db.commit()
#
#     def delete_nocommit(self, recid):
#         """
#             db.delete(recid)
#             delete a row from the table, by recid
#         """
#         query = f'DELETE FROM {self._table} WHERE id = ?'
#         self._db.execute(query, [recid])
#
#     def delete(self, recid):
#         self.delete_nocommit(recid)
#         self._db.commit()
#
#     def countrecs(self):
#         """
#             db.countrecs()
#             count the records in the table
#             returns a single integer value
#         """
#         query = f'SELECT COUNT(*) FROM {self._table}'
#         c = self._db.execute(query)
#         return c.fetchone()[0]
#
#     # filename property
#     @property
#     def _filename(self):
#         return self._dbfilename
#
#     @_filename.setter
#     def _filename(self, fn):
#         self._dbfilename = fn
#         self._db = sqlite3.connect(fn)
#         self._db.row_factory = sqlite3.Row
#
#     @_filename.deleter
#     def _filename(self):
#         self.close()
#
#     def close(self):
#         self._db.close()
#         del self._dbfilename
#
#
# def test():
#     fn = ':memory:'  # in-memory database
#     t = 'foo'
#
#     recs = [
#         dict(string='one', number=42),
#         dict(string='two', number=73),
#         dict(string='three', number=123)
#     ]
#
#     # -- for file-based database
#     # try: os.stat(fn)
#     # except: pass
#     # else:
#     #     print('Delete', fn)
#     #     os.unlink(fn)
#
#     print('bwDB version', __version__)
#
#     print(f'Create database file {fn} ...', end='')
#     db = bwDB(filename=fn, table=t)
#     print('Done.')
#
#     print('Create table ... ', end='')
#     db.sql_do(f' DROP TABLE IF EXISTS {t} ')
#     db.sql_do(f' CREATE TABLE {t} ( id INTEGER PRIMARY KEY, string TEXT, number INTEGER ) ')
#     print('Done.')
#
#     print('Insert into table ... ', end='')
#     for r in recs:
#         db.insert(r)
#     print('Done.')
#
#     print(f'There are {db.countrecs()} rows')
#
#     print('Read from table')
#     for r in db.getrecs():
#         print(dict(r))
#
#     print('Update table')
#     db.update(2, dict(string='TWO'))
#     print(dict(db.getrec(2)))
#
#     print('Insert an extra row ... ', end='')
#     newid = db.insert({'string': 'extra', 'number': 512})
#     print(f'(id is {newid})')
#     print(dict(db.getrec(newid)))
#     print(f'There are {db.countrecs()} rows')
#     print('Now delete it')
#     db.delete(newid)
#     print(f'There are {db.countrecs()} rows')
#     for r in db.getrecs():
#         print(dict(r))
#     for r in db.sql_query(f"select * from {t}"):
#         print(r)
#     db.close()
#
#
# if __name__ == "__main__": test()
