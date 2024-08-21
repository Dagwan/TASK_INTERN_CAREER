import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

def read_data(file_path):
    """
    Reads the CSV file into a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def extract_salary(salary_str):
    """
    Extracts the low, high, and average salary from a salary string.
    
    Args:
        salary_str (str): The salary string (e.g., '50K-100K').
    
    Returns:
        tuple: A tuple containing the low, high, and average salary.
    """
    if not isinstance(salary_str, str):
        print(f"Invalid salary format (not a string): {salary_str}")
        # Return None values if input is not a string
        return None, None, None  
    
    # Remove any unwanted characters except for digits, 'K', and '-'
    clean_str = re.sub(r'[^\dK-]', '', salary_str)
    
    # Debugging: Print the cleaned salary string
    print(f"Processing salary: {clean_str}")
    
    # Split the string into low and high salary parts
    salary_parts = clean_str.split('-')
    
    try:
        if len(salary_parts) == 2:
            # Convert to numeric, handling the 'K' multiplier
            salary_low = float(salary_parts[0].replace('K', '')) * 1000
            salary_high = float(salary_parts[1].replace('K', '')) * 1000
            average_salary = (salary_low + salary_high) / 2
            return salary_low, salary_high, average_salary
        elif len(salary_parts) == 1:
            salary = float(salary_parts[0].replace('K', '')) * 1000
            return salary, salary, salary
        else:
            print(f"Unexpected salary format: {salary_str}")
            return None, None, None
    except ValueError as e:
        # print(f"Error processing salary: {salary_str}, Error: {e}")
        return None, None, None


def clean_data(df):
    """
    Clean the dataset by removing unwanted characters from the salary
    column, handling missing values, and converting data types.
    
    Args:
        df (pd.DataFrame): The raw data.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    # Ensure the 'Salary' column is a string
    df['Salary'] = df['Salary'].astype(str)
    
    # Extract salary components and create new columns
    df[['Salary_Low', 'Salary_High', 'Average_Salary']] = df['Salary'].apply(lambda x: pd.Series(extract_salary(x)))
    
    # Drop rows where salary could not be extracted
    df = df.dropna(subset=['Salary_Low', 'Salary_High', 'Average_Salary'])
    
    return df

def calculate_summary_statistics(df):
    """
    Calculates and prints summary statistics for numerical columns.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
        None
    """
    print("\nSummary Statistics:")
    print(df.describe(include='all'))

def filter_data_by_location(df, location):
    """
    Filters the DataFrame by job location.
    
    Args:
        df (pd.DataFrame): The DataFrame to filter.
        location (str): The location to filter by.
    
    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    return df[df['Location'].str.contains(location, na=False)]

def plot_salary_distribution(df):
    """
    Plots the distribution of average salaries.
    
    Args:
        df (pd.DataFrame): The DataFrame containing salary information.
    
    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Average_Salary'], bins=30, kde=True, color='blue')
    plt.title('Average Salary Distribution')
    plt.xlabel('Average Salary')
    plt.ylabel('Frequency')
    plt.show()

def plot_salary_by_company(df):
    """
    Plots the average salary by company.
    
    Args:
        df (pd.DataFrame): The DataFrame containing salary information.
    
    Returns:
        None
    """
    avg_salary_by_company = df.groupby('Company')['Average_Salary'].mean().sort_values()
    
    plt.figure(figsize=(12, 8))
    avg_salary_by_company.plot(kind='bar', color='green')
    plt.title('Average Salary by Company')
    plt.xlabel('Company')
    plt.ylabel('Average Salary')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def plot_salary_boxplot(df):
    """
    Creates a box plot for salary distribution.
    
    Args:
        df (pd.DataFrame): The DataFrame containing salary information.
    
    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Company', y='Average_Salary', data=df, palette='Set2')
    plt.title('Salary Box Plot by Company')
    plt.xlabel('Company')
    plt.ylabel('Average Salary')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def plot_rating_distribution(df):
    """
    Plots the distribution of company ratings.
    
    Args:
        df (pd.DataFrame): The DataFrame containing company ratings.
    
    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Company Score'], bins=20, kde=True, color='orange')
    plt.title('Company Rating Distribution')
    plt.xlabel('Company Rating')
    plt.ylabel('Frequency')
    plt.show()

def plot_salary_vs_rating(df):
    """
    Creates a scatter plot of salary versus company rating.
    
    Args:
        df (pd.DataFrame): The DataFrame containing salary and company rating.
    
    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Company Score', y='Average_Salary', data=df, hue='Company', palette='viridis')
    plt.title('Salary vs Company Rating')
    plt.xlabel('Company Rating')
    plt.ylabel('Average Salary')
    plt.show()

def plot_heatmap_correlation(df):
    """
    Plots a heatmap showing the correlation between numerical columns.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
        None
    """
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

def save_processed_data(df, file_path):
    """
    Saves the cleaned and processed DataFrame to a new CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_path (str): Path where the CSV file will be saved.
    
    Returns:
        None
    """
    df.to_csv(file_path, index=False)
    print(f"Processed data saved to {file_path}")

# Main function to execute the script
def main():
    # File paths
    input_file = 'software_engineer_salaries.csv'
    output_file = 'processed_software_engineer_salaries.csv'
    
    # Read data
    df = read_data(input_file)
    
    # Clean data
    df = clean_data(df)
    
    # Calculate summary statistics
    calculate_summary_statistics(df)
    
    # Filter data (example: filter for 'Remote' jobs)
    remote_jobs = filter_data_by_location(df, 'Remote')
    print(f"\nRemote Jobs Data:\n{remote_jobs.head()}")
    
    # Plot visualizations
    plot_salary_distribution(df)
    plot_salary_by_company(df)
    plot_salary_boxplot(df)
    plot_rating_distribution(df)
    plot_salary_vs_rating(df)
    plot_heatmap_correlation(df)
    
    # Save processed data
    save_processed_data(df, output_file)

if __name__ == "__main__":
    main()