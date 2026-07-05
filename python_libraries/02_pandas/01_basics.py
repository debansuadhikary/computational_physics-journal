# We use pandas basically for importing data from csv, xlsx, json, etc. and for data manipulation and analysis. We can also use it for data cleaning, size mutability, and data visualization. It is built on top of numpy and provides a lot of functionality for working with data for statistical analysis.

# Data Structures in pandas:
# Data structures are collections of data types that provides the best way of organising items/values in terms of memory usage.

# 1. Series: A one-dimensional, size-immutable, labeled, homogeneous array capable of holding any data type. {If we add any string value in the series, then all the values will be converted to string.}
# 2. DataFrame: A two-dimensional, size-mutable, labeled data structure with columns of potentially different types.

# importing pandas library
import pandas as pd

# importing data from different file formats
# importing data from csv file
# df_csv = pd.read_csv("data.csv") # it imports data from a csv file and creates a dataframe

# importing data from excel file
# df_excel = pd.read_excel("data.xlsx") # it imports data from an excel file and creates a dataframe, it requires the "openpyxl" library to be installed

# We can understand the data in the dataframe using the following functions:
# df.head() # it prints the first 5 rows of the dataframe
# df.tail() # it prints the last 5 rows of the dataframe
# df.info() # it prints the summary of the dataframe
# df.describe(include='criterion') # it prints the statistical summary of the dataframe

# We can also find and handle missing values in the dataframe using the following functions:
# df.isnull() # it returns a dataframe of the same shape as the original dataframe with boolean values indicating whether the value is null or not
# df.dropna() # it drops the rows with missing values from the dataframe
# df.fillna(value) # it fills the missing values with the specified value in the dataframe
