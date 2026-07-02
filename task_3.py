import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/pritp/Desktop/internship_file/zomato_sample_dataset.csv")

print("Average Rating:", df['Aggregate rating'].mean())
print("Maximum Rating:", df['Aggregate rating'].max())
print("Minimum Rating:", df['Aggregate rating'].min())

plt.figure(figsize=(8,5))
plt.hist(df['Aggregate rating'], bins=10)
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Restaurants')
plt.show()

df['Has Online Delivery'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    figsize=(7,7)
)

plt.title('Online Delivery Distribution')
plt.ylabel('')
plt.savefig('online_delivery_distribution.png')
plt.show()
