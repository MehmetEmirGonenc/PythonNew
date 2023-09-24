#Challenge 2: Data Exploration
#Explore the loaded DataFrame by answering the following questions:
#
#How many rows and columns does the DataFrame have?
#What are the names of the columns?
#What are the data types of each column?
#Are there any missing values in the DataFrame?
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
#1) df.shape, gives a tuple that includes number of rows and columns
print("Rows: ", df.shape[0])
print("Columns: ", df.shape[1])
#2)
print(df.columns)
#3)
print(df.dtypes)
#4)
print(df.isnull().any().any()) # This return False, so we have no null value on DataFrame
