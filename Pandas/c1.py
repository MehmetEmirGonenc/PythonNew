#1: Loading Data
#Load a CSV file into a pandas DataFrame. You can use the read_csv function. Once loaded, display the first 5 rows of the DataFrame.
import pandas as pd

DataFrame = pd.read_csv('StudentsPerformance.csv')

print(DataFrame) #Print all data
print(DataFrame.head(5)) #Print 5 row from beginning
print(DataFrame.tail(5)) #Print 5 row from end