# Binning
# Python binning is a data preprocessing technique used to group a set of continuous values into a smaller number of "bins". 

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

# linspace. A Numpy function that return a array with "bins" that contains 4 equally spaced numbers over the specified interval of the price.
sir_bin = numpy.linspace ( min( data_frame_wmv["price"]),max(data_frame_wmv["price"]),4)
# Create a list with the price names
price_names = ["low","Medium","High"]
# Add a new column "price-binned"
data_frame_wmv ["price-binned"] = pandas.cut (data_frame_wmv["price"],sir_bin,labels=price_names,include_lowest=True)

print (data_frame_wmv)

# Export Data
path = r"D:\Python\DataScience\automobile.csv"
data_frame_wmv.to_csv(path)