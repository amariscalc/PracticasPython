# Normalization

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

path = r"D:\Python\DataScience\automobile.csv"
data_frame_wmv.to_csv(path)

### Normalice the "length"
# For this example, we will use 3 columns (length width and height)
data_frame_wmv_min_max = pandas.read_csv (path, usecols=(11,12,13))
print (data_frame_wmv)
# Use the Min-max method. Takes each value, X_old, subtracted from the minimum value of that feature, then divides by the range of that feature.
data_frame_wmv_min_max ["length"] = (data_frame_wmv ["length"] - data_frame_wmv ["length"].min()) / (data_frame_wmv ["length"].max() - data_frame_wmv ["length"].min())
print (data_frame_wmv_min_max)

# z-score or standard score. for each value, you subtract the Mu which is the average of the feature, and then divide by the standard deviation (sigma).
# The resulting values hover around 0, and typically range between -3 and +3, but can be higher or lower.
data_frame_wmv_z_score = pandas.read_csv (path, usecols=(11,12,13))
data_frame_wmv_z_score ["length"] = (data_frame_wmv ["length"] - data_frame_wmv ["length"].mean()) / data_frame_wmv ["length"].std()
print (data_frame_wmv_z_score)