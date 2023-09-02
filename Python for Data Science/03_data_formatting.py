# Import our friends; Sir Pandas and NumPy!
import pandas
import numpy

'''
As a part of dataset cleaning, data formatting ensures that data is consistent and easily
understandable.
For example, people may use different expressions to represent New York City, such as N.Y., Ny,
NY, and New York.
Sometimes, this “uncleaned” data is a good thing to see.
'''
### Setup Dataframe to work ! ;)
url_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
data_frame = pandas.read_csv(url_data,header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mgp","price"]

data_frame.columns = headers

#path = r"D:\Python\DataScience\automobile.csv"
#data_frame.to_csv(path)

##### rename(). Change a header label. 
data_frame.rename (columns={"city-mpg":"city-L/100Km"}, inplace = True)

### Operators with the values
data_frame ["city-L/100Km"] = 235 / data_frame ["city-L/100Km"]

# Convert type field
data_frame_temp = data_frame.replace ("?",numpy.NaN)
data_frame_wmv = data_frame_temp.dropna  (subset = ["price"], axis=0)

data_frame_wmv ["price"] = data_frame_wmv ["price"].astype("int64")

print (data_frame_wmv)
print (data_frame_wmv.dtypes)