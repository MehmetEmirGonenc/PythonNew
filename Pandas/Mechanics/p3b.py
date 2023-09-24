#Create a pie chart to visualize the proportion of survivors and non-survivors among passengers.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

survivors = df['Survived'].sum()
non_survivors = df['Survived'].count() - survivors

plt.pie([survivors, non_survivors], labels=['Survived', 'Non-Survived'], autopct='%1.1f%%', startangle=90)
# Parameter 1: Variables
# Parameter 2: Labels of variables
# Parameter 3: Format of write on pie chart(after '.' means how mant decimal num will write) ('%%' double percentage means write normal percentage)
plt.title("Survivors and Non-survivors Among Passengers")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
plt.close()