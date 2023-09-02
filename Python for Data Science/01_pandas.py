# Pandas

'''
Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks.
'''
import pandas

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

### Object Creation

'''
Creating a Series by passing a list of values, letting pandas create a default RangeIndex.
'''
In [3]: s = pandas.Series([1, 3, 5, np.nan, 6, 8])

In [4]: s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64