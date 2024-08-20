import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('books_with_ratings_and_links_all_pages.csv')

# Display basic information about the dataset
print("Data Overview:")
print(df.info())
print("\nFirst few rows of the data:")
print(df.head())

# Data Cleaning
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill or drop missing values if necessary
# df.fillna('N/A', inplace=True)  # Example: Fill missing values with 'N/A'
# df.dropna(inplace=True)  # Example: Drop rows with any missing values

# Clean the 'Price' column
# Remove currency symbols and convert to float
df['Price'] = df['Price'].replace('[£]', '', regex=True).replace('[\u20ac,]', '', regex=True)
df['Price'] = df['Price'].astype(float)

# Data Analysis
# Basic statistics
print("\nBasic statistics:")
print(df.describe(include='all'))

# Analyze price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Price Distribution of Books')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Analyze ratings distribution
rating_mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].map(rating_mapping)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Rating', order=[1, 2, 3, 4, 5])
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_books_data.csv', index=False)
print("\nCleaned data saved to cleaned_books_data.csv")
