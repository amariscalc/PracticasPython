# Pandas and NumPy

'''
It´s neccesary installa Anaconda or Miniconda:
https://docs.conda.io/projects/miniconda/en/latest/

'''
import pandas
'''
Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks.
'''

# Numpy
import numpy
'''
NumPy (Numerical Python) is an open source Python library that's used in almost every field of science and engineering. 
It's the universal standard for working with numerical data in Python, and it's at the core of the scientific Python and PyData ecosystems.
'''

'''
Pandas provides two types of classes for handling data:
· Series: a one-dimensional labeled array holding data of any type
such as integers, strings, Python objects etc.

· Dataframe: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
'''

# Get a file example from Internet
url_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# Create a object (the file has not header)
data_frame = pandas.read_csv(url_data,header=None)
print (type(data_frame)) # <class 'pandas.core.frame.DataFrame'>

# head (). Show the first "n" first rows of data frame
print (data_frame.head(3))

# tailf (). Show the botton "n" rows of data frame
print (data_frame.tail(3))

# How replace headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mgp","price"]

data_frame.columns = headers

print (data_frame.head(2))

# Save the changed
#Define a path
path = r"D:\Python\DataScience\automobile.csv"
data_frame.to_csv(path)

'''
for others formats

csv    panda.read_csv()   panda.to_csv()
json   panda.read_json()  panda.to_json()
excel  panda.read_excel() panda.to_excel()
sql    panda.real_sql()   panda.to_sql()
'''