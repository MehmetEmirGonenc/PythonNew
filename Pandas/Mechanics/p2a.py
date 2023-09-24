#In Task 2a, you are tasked with calculating the average fare paid by passengers in each passenger class (First Class, Second Class, Third Class).
import pandas as pd


df = pd.read_csv('titanic.csv')

print(df.groupby(['Pclass']).mean()['Fare'])