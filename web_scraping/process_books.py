import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    """
    Load the CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' does not exist. Please check the path and try again.")
    
    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.EmptyDataError:
        raise ValueError(f"Error: The file '{file_path}' is empty.")
    except pd.errors.ParserError:
        raise ValueError(f"Error: There was an issue parsing the file '{file_path}'.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while loading the file: {e}")

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
    
    # Drop rows with missing values in 'Price'
    df.dropna(subset=['Price'], inplace=True)
    
    # Clean the 'Price' column
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
    try:
        df.to_csv(output_file_path, index=False)
        print(f"\nCleaned data successfully saved to {output_file_path}")
    except PermissionError:
        print(f"Error: The file '{output_file_path}' is currently open in another program. Please close the file and try again.")
    except FileNotFoundError:
        print(f"Error: The directory or file path '{output_file_path}' was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main workflow
def main():
    # File paths
    input_file_path = 'books_with_scraped_info.csv'
    output_file_path = 'cleaned_books_data.csv'
    
    try:
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
    
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred in the main workflow: {e}")

# Run the main workflow
if __name__ == "__main__":
    main()