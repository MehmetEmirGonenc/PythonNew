#Challenge 3: Filtering Data
#Filter the DataFrame to only include rows where a specific column meets a certain condition. For example, filter the DataFrame to only include rows where the 'Age' column is greater than 30.

import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
# Accourding to challenge we filter by 'math score' greater then 80.
filtered_df = df.loc[df['math score'] > 80]
print(filtered_df)