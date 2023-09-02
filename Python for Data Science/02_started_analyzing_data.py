import pandas
import numpy

url_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
data_frame = pandas.read_csv(url_data,header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-weight","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mgp","price"]

data_frame.columns = headers

# print (data_file)

'''
The main types stored in Pandas objets are object, float, int, and datetime.

The "object" pandas type functions similar to "string" in Python, while the "datetime" pandas type, 
is a very useful type for handling time series.

it´s neccesary check the data type.
Pandas automatically assigns types based on the encoding it detects from the original data table.
For a number of reasons, this assignment may be incorrect.
'''

# to check the data types
#print (data_frame.dtypes)
'''
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                  object
stroke                object
compression-ratio    float64
horsepower            object
peak-rpm              object
city-mpg               int64
highway-mgp            int64
price                 object
dtype: object
'''
# Return a statiscal summary
print (data_frame.describe())
'''
        symboling  wheel-base      length       width      height  curb-weight  engine-size  compression-ratio    city-mpg  highway-mgp
count  205.000000  205.000000  205.000000  205.000000  205.000000   205.000000   205.000000         205.000000  205.000000   205.000000
mean     0.834146   98.756585  174.049268   65.907805   53.724878  2555.565854   126.907317          10.142537   25.219512    30.751220
std      1.245307    6.021776   12.337289    2.145204    2.443522   520.680204    41.642693           3.972040    6.542142     6.886443
min     -2.000000   86.600000  141.100000   60.300000   47.800000  1488.000000    61.000000           7.000000   13.000000    16.000000
25%      0.000000   94.500000  166.300000   64.100000   52.000000  2145.000000    97.000000           8.600000   19.000000    25.000000
50%      1.000000   97.000000  173.200000   65.500000   54.100000  2414.000000   120.000000           9.000000   24.000000    30.000000
75%      2.000000  102.400000  183.100000   66.900000   55.500000  2935.000000   141.000000           9.400000   30.000000    34.000000
max      3.000000  120.900000  208.100000   72.300000   59.800000  4066.000000   326.000000          23.000000   49.000000    54.000000

It returns the number of terms in the column as
"count", average column value as "mean",
column standard deviation as "std", the maximum and minimum values,
as well as the boundary of each of the quartiles.
By default, the dataframe.describe() function skips rows and columns that do not contain
numbers.
'''
print (data_frame.describe(include="all"))
'''
To enable a summary of all the columns, we could add an argument include = "all" inside
the describe function bracket.
Now the outcome shows the summary of all the 26 columns, including object-typed attributes.

"Unique" is the number of distinct objects in the column, "top" is the most frequently
occurring object, and "freq" is the number of times the top object appears in the column.

Some values in the table are shown here as "NaN", which stands for "not a number".
'''

# info (). Another method you can use to check your dataset is the dataframe.info function. This function shows the top 30 rows and bottom 30 rows of the dataframe.
print (data_frame.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 205 entries, 0 to 204
Data columns (total 26 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   symboling          205 non-null    int64
 1   normalized-losses  205 non-null    object
 2   make               205 non-null    object
 3   fuel-type          205 non-null    object
 4   aspiration         205 non-null    object
 5   num-of-doors       205 non-null    object
 6   body-style         205 non-null    object
 7   drive-wheels       205 non-null    object
 8   engine-location    205 non-null    object
 9   wheel-base         205 non-null    float64
 10  length             205 non-null    float64
 11  width              205 non-null    float64
 12  height             205 non-null    float64
 13  curb-weight        205 non-null    int64
 14  engine-type        205 non-null    object
 15  num-of-cylinders   205 non-null    object
 16  engine-size        205 non-null    int64
 17  fuel-system        205 non-null    object
 18  bore               205 non-null    object
 19  stroke             205 non-null    object
 20  compression-ratio  205 non-null    float64
 21  horsepower         205 non-null    object
 22  peak-rpm           205 non-null    object
 23  city-mpg           205 non-null    int64
 24  highway-mgp        205 non-null    int64
 25  price              205 non-null    object
dtypes: float64(5), int64(5), object(16)
memory usage: 41.8+ KB
None
'''