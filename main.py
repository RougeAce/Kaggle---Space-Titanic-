import pandas as pd
import matplotlib.pyplot as plt

train_file = "spaceship-titanic/train.csv"
train = pd.read_csv(train_file)

# Drop rows with missing values
train = train.dropna(how='any')

# Group by HomePlanet and sum the Survived column for each group
survivors = train.groupby('VIP')['Transported'].sum()

# Create a pie chart
plt.pie(survivors, labels=survivors.index, autopct='%1.1f%%')
plt.title('Survivors by Planet')
plt.show()
print("cofriemd ")

