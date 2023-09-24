#Challenge 8: Analysis
#Show each groups female and male mean of average scores.
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
df['Average Score'] = df.iloc[:, 5:8].mean(axis=1)
df = df.groupby(['race/ethnicity', 'gender']).mean()['Average Score']
print(df)