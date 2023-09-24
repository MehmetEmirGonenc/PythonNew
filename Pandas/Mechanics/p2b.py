# Calculate the survival rate for passengers in each passenger class and gender. The survival rate is the percentage of survivors in each group.
import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100) # 100 times mean make it pecentage