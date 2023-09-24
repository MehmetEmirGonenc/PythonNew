import pandas as pd
import matplotlib.pyplot as plt
#
#https://pandas.pydata.org/docs/user_guide/visualization.html#histograms

#Open dataset
df = pd.read_csv('titanic.csv')
                                                            #Stage 1
#We will check missing values, duplicate values and editing neceseery changes to perep data to work
#Task 1: Handling Missing Data

#Step-1     Check is there any missing value
'''
print(df.isnull().sum()) # Same as isna()
'''
# Missing values = 177 age; 687 Cabin; 2 Embarked

#Step-2     Handle with missing values; (Fill them or drop them)
# Dropping
#We have any missing value now but only 183 values left, so we can use other method on here
''' 
df = df.dropna(subset=['Age', 'Cabin', 'Embarked'])
print(df.isnull().sum()) # Same as isna()
'''
# Fill
# We fill missing ages with mean Age; Cabin with unknown; Embarked with unknown
df['Age'].fillna(df['Age'].mean(), inplace=True) # inplace true , means we change df directly don't need to (df = ...), We change pointed value directly
df['Cabin'].fillna('Unknown', inplace=True)
df['Embarked'].fillna('Unknown', inplace=True)


#Task 2: Data Type Conversions
# Check DataTypes
'''
print(df.dtypes)
'''
# Change age with int type, but we don't do it. Remember : astype(type)
'''
df['Age'] = df['Age'].astype(int)
print(df.dtypes)
'''


#Task 3: Removing Duplicates
df = df.drop_duplicates()


#Task 4: Renaming Columns
'''
df.rename(columns={'Pclass': 'PassengerClass'}, inplace=True)
print(df)
'''
# Done!
                                                            #Stage 2
#We will analyze and exploring dataset.
#Task 1: Descriptive Statistics
print(df[['Age', 'Fare']].describe())


#Task 2: Grouping and Aggregation
#1- Group by Pclass and find average age for each 
print(df.groupby(['Pclass']).mean()['Age'])

#2- Find number of survived or dead, grouped by Pclass and gender
print(df.groupby(['Pclass', 'Sex']).count()['Survived'])


#Task 3: Data Visualization with Pandas
#1- Create a histogram to visualize the distribution of ages among passengers.
plt.hist(df['Age'], bins=50, edgecolor='k', color='b') # Options can changeable
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.title('Age Distribution Among Passengers')
plt.show()
plt.close()

#2- Create a bar chart to show the number of passengers in each passenger class.
# Create a bar chart
classCounts = df['Pclass'].value_counts()
#Way 1
classCounts.plot(kind='bar', edgecolor='k')

#Way 2
'''
plt.figure(figsize=(8,5))
plt.bar(classCounts.index, classCounts.values)     
'''                                             
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('Number of Passengers in Each Passenger Class')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.show()   
plt.close()                                                     
                                                            
# Done!                                                                                                        
                                                            #Stage 3 Data manuplation;
#Task 1: Slicing and Indexing
print(df.loc[(df['Age'] >= 20) & (df['Age'] <= 30), ['Name', 'Age']]) # Check also "iloc" function

#Task 2: Conditional Updates
#Update values in the DataFrame based on certain conditions. For example, update the "Sex" column to replace "male" with "M" and "female" with "F."
df['Sex'].replace({'male' : 'M' , 'female' : 'F'}, inplace=True)
print(df)

#Task 3: Merging and Joining DataFrames
# Suppose you have another DataFrame called 'additional_info'
# This DataFrame should have a common key, such as 'PassengerId' or 'Name'

# Merge the two DataFrames based on a common key (e.g., 'PassengerId')
'''merged_df = df.merge(additional_info, on='PassengerId', how='inner')'''

# 'how' parameter specifies the type of merge (e.g., 'inner' for common elements)

'''
'inner' (default): This option performs an inner join, returning only the rows with matching keys in both DataFrames.

'outer': An outer join returns all rows from both DataFrames, filling in missing values with NaN for columns that don't have a match in the other DataFrame.

'left': A left join returns all rows from the left DataFrame and the matched rows from the right DataFrame. For unmatched rows in the right DataFrame, NaN values are filled in.

'right': A right join is similar to a left join but returns all rows from the right DataFrame and the matched rows from the left DataFrame. Unmatched rows in the left DataFrame receive NaN values.

'cross': A cross join (also known as a Cartesian join) returns the Cartesian product of the two DataFrames, resulting in every possible combination of rows.
'''
#Task 4: Reshaping Data
pivot_table = df.pivot_table(index='Pclass', columns='Sex', values='Age', aggfunc='mean')

print(pivot_table)

#Done

