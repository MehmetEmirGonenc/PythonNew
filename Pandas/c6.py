#Challenge 6: Categorize
#Seperate each group and show just their gender, average score and group name. Make a sort by arerage score and if average score is same sort them by gender; first: female, then male

import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
df['Average Score'] = df.iloc[:, 5:8].mean(axis=1)
cols = list(df.columns)
df = df[cols[0:2] + [cols[-1]]]
print(df)
# Sorting
df = df.sort_values(['race/ethnicity', 'Average Score', 'gender'], ascending=(1,0,1))

print(df)

