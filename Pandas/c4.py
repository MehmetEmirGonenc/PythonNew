#Challenge 4: Sorting Data
#Sort the DataFrame by a specific column in ascending and descending order. Display the top 5 rows for each sorting.
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
df = df.sort_values(['reading score'],ascending=1) # A -> Z  & low -> high
print(df.head(5))
df = df.sort_values(['reading score'],ascending=0) # Z -> A & high -> low
print(df.head(5))