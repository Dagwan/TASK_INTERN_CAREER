import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def display_basic_info(df):
    """
    Display basic information about the dataset.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    """
    print("Data Overview:")
    print(df.info())
    print("\nFirst few rows of the data:")
    print(df.head())

def clean_data(df):
    """
    Clean the DataFrame by handling missing values and converting data types.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Fill or drop missing values if necessary
    # Example: Fill missing values with 'N/A'
    # df.fillna('N/A', inplace=True)
    # Example: Drop rows with any missing values
    # df.dropna(inplace=True)
    
    # Clean the 'Price' column
    # Remove currency symbols and convert to float
    df['Price'] = df['Price'].replace('[£]', '', regex=True).replace('[\u20ac,]', '', regex=True)
    df['Price'] = df['Price'].astype(float)
    
    return df

def analyze_data(df):
    """
    Perform data analysis and generate visualizations.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    """
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

def save_cleaned_data(df, output_file_path):
    """
    Save the cleaned DataFrame to a new CSV file.
    
    Parameters:
    df (pd.DataFrame): The cleaned DataFrame.
    output_file_path (str): The path where the cleaned CSV file will be saved.
    """
    df.to_csv(output_file_path, index=False)
    print("\nCleaned data saved to", output_file_path)

# Main workflow
def main():
    # File paths
    input_file_path = 'books_with_detailed_info.csv'
    output_file_path = 'cleaned_books_data.csv'
    
    # Load the data
    df = load_data(input_file_path)
    
    # Display basic information
    display_basic_info(df)
    
    # Clean the data
    df = clean_data(df)
    
    # Analyze the data
    analyze_data(df)
    
    # Save the cleaned data
    save_cleaned_data(df, output_file_path)

# Run the main workflow
if __name__ == "__main__":
    main()