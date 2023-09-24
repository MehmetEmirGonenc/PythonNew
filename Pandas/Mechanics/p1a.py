# Select all rows from the Titanic dataset where the "Sex" column is equal to "female." How many female passengers are there?
import pandas as pd

df = pd.read_csv('titanic.csv')

print(df[df['Sex'] == 'female'].count()['PassengerId'])