# Create a bar chart to visualize the number of passengers in each passenger class (First Class, Second Class, Third Class).
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

class_counts = df['Pclass'].value_counts()
class_counts.plot(kind='bar')
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Number of Passengers In Each Passenger Class")
plt.show()
