#Combined Practice:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

#    Task 1: Filtering and Summary Statistics
#    Select all female passengers who are 25 years old or younger and calculate the average fare paid by this group.

task1_df = df.loc[(df['Sex'] == 'female') & (df['Age'] <= 25)].mean()['Fare']

print("Task 1: ", task1_df)

#    Task 2: Data Visualization
#    Create a bar chart to visualize the number of female passengers in each passenger class (First Class, Second Class, Third Class).

task2_df = df[df['Sex'] == 'female']
class_counts = task2_df['Pclass'].value_counts()
class_counts.plot(kind='bar')
plt.xlabel("Passenger class")
plt.ylabel("Number of female passengers")
plt.title("Number of Female Passengers In Each Passenger Class")
plt.show()
plt.close()

#    Task 3: Data Analysis
#    Calculate the survival rate for male passengers who are 25 years old or younger.

task3_df = df[df['Sex'] == 'male']
task3_df = task3_df['Survived'].mean()*100
print("Task 2: ", task3_df)

#    Task 4: More Data Visualization
#    Create a pie chart to visualize the proportion of female survivors and non-survivors among passengers in the selected age group.

#Without ensuring input!!
age = int(input("-->"))
task4_df = df.loc[(df['Sex'] == 'female') & (df['Age'] <= age)]
survivors = task4_df['Survived'].sum()
non_survivors = task4_df['Survived'].count() - survivors
plt.pie([survivors, non_survivors], labels=['Survivors', 'Non-Survivors'], autopct='%1.1f%%', startangle=90)
plt.title("Female Survivors And Non-Survivors Among Passengers")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.close()