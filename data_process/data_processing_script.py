import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def read_data(file_path):
    """
    Reads the csv file into a DataFrame
    
    args:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Cleans the data by removing any unwanted characters and converting data types.
    
    Args:
    df (pd.DataFrame): The DataFrame to clean.
    
    Returns:
    pd.DataFrame: Cleaned DataFrame
    """
    
    # REmove any trailing charactrs from 'Salary' column
    df['Salary'] = df['Salary'].replace('[\$\K]', '', regex=True)
    
    # Convert salary to numeric
    df['Salary'] = df['Salary'].str.replace('K', '').astype(float) * 1000
    
    # Convert 'Date' to datetime format
    df['Date'] = pd.to_datetime(df['Date'], error='coerce')
    
    return df

def calculate_summary_statistics(df):
    """
    Calculates and prints summary statistics for numerical columns.
    
    Args:
    df (pd.DataFrame): The DataFrame to analye.
    
    Returns:
    None
    """
    
    print("\Summary Statistics:")
    print(df.describe(include='all'))
    
def filter_data_by_location(df, location):
    """
    Filters the DataFrame by job location.
    
    Args:
    df (pd.DataFrame): The Dataframe to filter.
    location (str): The location to filter by.
    
    Returns:
    pd.DataFrame: Filtered DataFrame.
    """
    
    return df[df['Location'].str.contains(location, na=False)]

def plot_salary_distribution(df):
    """
    Plots the distribution of salaries.
    
    Args
    df (pd.DataFrame): The DataFrame containing salary information.
    
    
    Returns:
    None
    """
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Salary"], bins=30, kde=True, color='blue')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.show()
    
def plot_salary_by_company(df):
    """
    Plots the average salary by company.
    
    Args:
    df (pd.Dataframe): The DataFrame containing salary information.
    
    Returns:
    None
    """
    
    avg_salary_by_company = df.groupby('Company')['Salary'].mean().sort_values()
    
    plt.figure(figsize=(12, 8))
    avg_salary_by_company.plot(ind='bar', color='green')
    plt.title('Average Salary by Company')
    plt.xlabel('Company')
    plt.ylabel('Average Salary')
    plt.ticks(rotation=45, ha='right')
    plt.show()
    
def plot_salary_boxplot(df):
    """
    Creates a box plot for salary distribution.
    
    Args:
    df (pd.DataFrame): The dataFrame containing salary information.
    
    Returns:
    None"""
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Company', y='Salary', data=df, palatte='Set2')
    plt.title('Salary Box Plot by Company')
    plt.xlabel('Company')
    plt.ylabel('Salary')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    
def plot_rating_distribution(df):
    """
    Plots the distirbution of company ratings.
    
    Args:
    df (pd.DataFrame): The Dataframe containing company ratings.
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    sns.histoplot(df['Company Score'], bins=20, kde=True, color='orange')
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
    sns.scatterplot(x='Company Score', y='Salary', data=df, hue='Company', palette='viridis')
    plt.title('Salary vs Company Rating')
    plt.xlabel('Company Rating')
    plt.ylabel('Salary')
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

def save_proccessed_data(df, file_path):
    """
    Saves the cleaned and process DataFrame to a new CSV File"""