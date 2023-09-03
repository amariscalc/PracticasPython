# Data Analysis


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
'''
“What are the characteristics that have the most impact on the car price?”

· Descriptive Statistics
· GroupBy
· Anova
· Correlation
'''
print (data_frame_wmv.describe())
'''
        symboling  wheel-base      length       width      height  curb-weight  engine-size  compression-ratio    city-mpg  highway-mgp         price
count  201.000000  201.000000  201.000000  201.000000  201.000000   201.000000   201.000000         201.000000  201.000000   201.000000    201.000000
mean     0.840796   98.797015  174.200995   65.889055   53.766667  2555.666667   126.875622          10.164279   25.179104    30.686567  13207.129353
std      1.254802    6.066366   12.322175    2.101471    2.447822   517.296727    41.546834           4.004965    6.423220     6.815150   7947.066342
min     -2.000000   86.600000  141.100000   60.300000   47.800000  1488.000000    61.000000           7.000000   13.000000    16.000000   5118.000000
25%      0.000000   94.500000  166.800000   64.100000   52.000000  2169.000000    98.000000           8.600000   19.000000    25.000000   7775.000000
50%      1.000000   97.000000  173.200000   65.500000   54.100000  2414.000000   120.000000           9.000000   24.000000    30.000000  10295.000000
75%      2.000000  102.400000  183.500000   66.600000   55.500000  2926.000000   141.000000           9.400000   30.000000    34.000000  16500.000000
max      3.000000  120.900000  208.100000   72.000000   59.800000  4066.000000   326.000000          23.000000   49.000000    54.000000  45400.000000
'''
### Group by

df_test = data_frame_wmv [["drive-wheels","body-style","price"]]
df_groupby = df_test.groupby(["drive-wheels","body-style"], as_index=False).mean()

print (df_groupby)
'''
   drive-wheels   body-style         price
0           4wd    hatchback   7603.000000
1           4wd        sedan  12647.333333
2           4wd        wagon   9095.750000
3           fwd  convertible  11595.000000
4           fwd      hardtop   8249.000000
5           fwd    hatchback   8396.387755
6           fwd        sedan   9811.800000
7           fwd        wagon   9997.333333
8           rwd  convertible  23949.600000
9           rwd      hardtop  24202.714286
10          rwd    hatchback  14337.777778
11          rwd        sedan  21711.833333
12          rwd        wagon  16994.222222
'''
# pivot table
df_pivot = df_groupby.pivot(index="drive-wheels",columns="body-style")
print ("....")
print (df_pivot)
'''
                   price
body-style   convertible       hardtop     hatchback         sedan         wagon
drive-wheels
4wd                  NaN           NaN   7603.000000  12647.333333   9095.750000
fwd              11595.0   8249.000000   8396.387755   9811.800000   9997.333333
rwd              23949.6  24202.714286  14337.777778  21711.833333  16994.222222
'''

# Correlation
# df.corr()
data_frame_wmv[["stroke","price"]].corr()

data_frame_wmv.describe()