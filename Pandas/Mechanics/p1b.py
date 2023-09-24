# Select all rows from the Titanic dataset where the "Age" column is 25 or younger. How many passengers are 25 or younger?
import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.loc[df['Age'] <= 25].count()['PassengerId'])