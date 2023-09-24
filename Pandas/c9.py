#Challenge 9:
#Read file chuck by chunk (To handle large amounts of data)
import pandas as pd

for df in pd.read_csv('StudentsPerformance.csv', chunksize=10):
    print("\nChuck\n")
    print(df)
