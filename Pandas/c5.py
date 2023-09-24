#Challenge 5: Grouping and Aggregation
#Group the DataFrame by a categorical column and calculate summary statistics for each group. For example, calculate the mean and median of the 'Salary' column for each group.

import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
# We do it for math, reading and writing scores , we mean them
df['Average Score'] = df.iloc[:, 5:8].mean(axis=1)
print(df)
# We can change its position on table
# Now it is in the end of the table
# We take it to betweeen test prep course and math score
cols = list(df.columns) # To make our life easier
df = df[cols[0:5] + [cols[-1]] + cols[5:8]]
print(df)