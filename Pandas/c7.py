#Challenge 7: Counting
#Seperete each group and count them and show how many male and female is in the each group.
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

df = df.groupby(['race/ethnicity', 'gender']).count()
print(df)
#As you noticed this counts each column but it unnecessary and hard to analyse and bad view so we can do it with different way
# First reload data
df = pd.read_csv('StudentsPerformance.csv')
df = df.groupby(['race/ethnicity', 'gender']).count()['math score']
print(df)
# We can count just like that but it is not best way because this way works just columns that data types int so better way
# Reload again
df = pd.read_csv('StudentsPerformance.csv')
df['counter'] = 1 # create a new column
df = df.groupby(['race/ethnicity', 'gender']).count()['counter']
print(df)