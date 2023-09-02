# Dummy Variables
'''
A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value. 
We can create dummy variables in python using get_dummies() method.
'''
# Import our friends; Sir Pandas and NumPy!
import pandas
import numpy

# Setup the data
url_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
data_frame = pandas.read_csv(url_data,header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mgp","price"]

data_frame.columns = headers
data_frame_temp = data_frame.replace ("?",numpy.NaN)
data_frame_wmv = data_frame_temp.dropna  (subset = ["price"], axis=0)
data_frame_wmv ["price"] = data_frame_wmv ["price"].astype("int64")
############################################################################

# get_dummies(). Transforming categorical variables to dummy variables is simple.
fuel_types = pandas.get_dummies(data_frame_wmv["fuel-type"])
print (fuel_types)
'''
     diesel  gas
0         0    1
1         0    1
2         0    1
3         0    1
4         0    1
..      ...  ...
200       0    1
201       0    1
202       0    1
203       1    0
204       0    1
'''

# Export Data
path = r"D:\Python\DataScience\automobile_dummy.csv"
data_frame_wmv.to_csv(path)


print (data_frame.head (5))