
#  Pandas is a popular library that gives us tools for doing practical, real world data analysis in Python.
#  It features robust built-in data structures that can help you organize your data and memory, and gain meaningful
#  insight from your data. Along with these analysis tools, pandas also has a tight integration with SQLAlchemy for
#  working with databases. So you can easily access the data you want to work with. When you're analyzing data with
#  Python, likely, you won't be making a traditional application. Instead, you'll be writing code to make diagrams,
#  plots, and calculations, and analyzing the visualizations they return.

# pip3 install pandas
# pip3 install jupyter
# pip3 install matplotlib     This will allow us to create some visualizations.

# jupyter notebook     will open jupyter notebook server

# df = pandas.read_csv('file.csv')    read csv files
# df.head()    will show first 5 files
# df.tail()    will show last 5 files
# df.info()    will show difference between fields
# df.describe()     will show statistic of values in each  row

# df['ProdCategory'].value_counts()     to see the most common values for a given variable or column. Let's take a
# look at what value counts returns for the product category column
#
# df['OrderType'].value_counts()      Interesting, wholesale orders are more common than retail orders. The value counts
# function works best for variables with a small set of values.

# df['OrderTotal'].describe()         l to grab that column.describe and it looks like the most frequent purchase

# df['OrderTotal'].value_counts()

# df['Quantity'].hist()      we can make a histogram of the values in a given column with hist.

# df['ProdCategory'].value_counts().plot(kind='barh')   will plot graphic

# ENUM type is type which can store list of other types