import unittest
import pandas as pd
from data_processing import (
    read_data,
    extract_salary,
    clean_data,
    calculate_summary_statistics,
    filter_data_by_location,
    plot_salary_distribution,
    plot_salary_by_company,
    plot_salary_boxplot,
    plot_rating_distribution,
    plot_salary_vs_rating,
    plot_heatmap_correlation,
    save_processed_data
)
from unittest.mock import patch, MagicMock
import numpy as np

class TestDataProcessing(unittest.TestCase):
    """
    This class contains unit tests for the functions in the data_processing module.
    It uses the unittest framework to test various functionalities.
    """

    @patch('data_processing.pd.read_csv')
    def test_read_data(self, mock_read_csv):
        """
        Test the read_data function to ensure it correctly reads a CSV file into a DataFrame.
        Mocks pd.read_csv to return a predefined DataFrame and checks if the function output matches.
        """
        # Setup: Mock DataFrame to be returned by pd.read_csv
        mock_df = pd.DataFrame({'Salary': ['50K-100K', '60K', '70K-120K'], 'Location': ['Remote', 'On-site', 'Remote']})
        mock_read_csv.return_value = mock_df
        
        # Test: Call read_data and compare the result with the mock DataFrame
        df = read_data('dummy_path.csv')
        pd.testing.assert_frame_equal(df, mock_df)
    
    def test_extract_salary(self):
        """
        Test the extract_salary function to ensure it correctly parses salary strings.
        Tests various salary formats and validates the output tuples.
        """
        # Test cases for different salary strings
        self.assertEqual(extract_salary('50K-100K'), (50000.0, 100000.0, 75000.0))
        self.assertEqual(extract_salary('60K'), (60000.0, 60000.0, 60000.0))
        self.assertEqual(extract_salary('Invalid'), (None, None, None))
        self.assertEqual(extract_salary(12345), (None, None, None))
    
    def test_clean_data(self):
        """
        Test the clean_data function to ensure it correctly processes and cleans the DataFrame.
        Compares the cleaned DataFrame with the expected DataFrame to ensure accuracy.
        """
        # Setup: DataFrame with mixed salary formats
        df = pd.DataFrame({'Salary': ['50K-100K', '60K', '70K-120K', 'Invalid'], 'Location': ['Remote', 'On-site', 'Remote', 'Remote']})
        cleaned_df = clean_data(df)
        
        # Expected cleaned DataFrame
        expected_df = pd.DataFrame({
            'Salary': ['50K-100K', '60K', '70K-120K'],
            'Location': ['Remote', 'On-site', 'Remote'],
            'Salary_Low': [50000.0, 60000.0, 70000.0],
            'Salary_High': [100000.0, 60000.0, 120000.0],
            'Average_Salary': [75000.0, 60000.0, 95000.0]
        })
        
        # Test: Compare the cleaned DataFrame with the expected DataFrame
        pd.testing.assert_frame_equal(cleaned_df, expected_df)
    
    @patch('data_processing.print')
    def test_calculate_summary_statistics(self, mock_print):
        """
        Test the calculate_summary_statistics function to ensure it prints summary statistics.
        Mocks print to verify that it is called when the function is executed.
        """
        df = pd.DataFrame({'Salary': [50000, 60000, 70000], 'Company Score': [4.5, 3.7, 4.8]})
        calculate_summary_statistics(df)
        # Test: Ensure print was called to output summary statistics
        mock_print.assert_called()
    
    def test_filter_data_by_location(self):
        """
        Test the filter_data_by_location function to ensure it correctly filters DataFrame by location.
        Compares the filtered DataFrame with the expected DataFrame for accuracy.
        """
        df = pd.DataFrame({'Salary': ['50K-100K', '60K'], 'Location': ['Remote', 'On-site']})
        filtered_df = filter_data_by_location(df, 'Remote')
        expected_df = pd.DataFrame({'Salary': ['50K-100K'], 'Location': ['Remote']})
        # Test: Compare the filtered DataFrame with the expected DataFrame
        pd.testing.assert_frame_equal(filtered_df, expected_df)
    
    @patch('data_processing.plt.show')
    def test_plot_salary_distribution(self, mock_show):
        """
        Test the plot_salary_distribution function to ensure it generates a histogram of salary distributions.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Average_Salary': [50000, 60000, 70000]})
        plot_salary_distribution(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.plt.show')
    def test_plot_salary_by_company(self, mock_show):
        """
        Test the plot_salary_by_company function to ensure it generates a bar plot of average salaries by company.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Company': ['Company A', 'Company B'], 'Average_Salary': [50000, 60000]})
        plot_salary_by_company(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.plt.show')
    def test_plot_salary_boxplot(self, mock_show):
        """
        Test the plot_salary_boxplot function to ensure it generates a box plot of salaries by company.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Company': ['Company A', 'Company B'], 'Average_Salary': [50000, 60000]})
        plot_salary_boxplot(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.plt.show')
    def test_plot_rating_distribution(self, mock_show):
        """
        Test the plot_rating_distribution function to ensure it generates a histogram of company ratings.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Company Score': [4.5, 3.7, 4.8]})
        plot_rating_distribution(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.plt.show')
    def test_plot_salary_vs_rating(self, mock_show):
        """
        Test the plot_salary_vs_rating function to ensure it generates a scatter plot of salary versus company rating.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Company Score': [4.5, 3.7, 4.8], 'Average_Salary': [50000, 60000, 70000], 'Company': ['A', 'B', 'C']})
        plot_salary_vs_rating(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.plt.show')
    def test_plot_heatmap_correlation(self, mock_show):
        """
        Test the plot_heatmap_correlation function to ensure it generates a heatmap of correlations between numerical columns.
        Mocks plt.show to verify that it is called to display the plot.
        """
        df = pd.DataFrame({'Salary': [50000, 60000, 70000], 'Company Score': [4.5, 3.7, 4.8]})
        plot_heatmap_correlation(df)
        # Test: Ensure plt.show was called to display the plot
        mock_show.assert_called()
    
    @patch('data_processing.pd.DataFrame.to_csv')
    def test_save_processed_data(self, mock_to_csv):
        """
        Test the save_processed_data function to ensure it correctly saves the DataFrame to a CSV file.
        Mocks pd.DataFrame.to_csv to verify that it is called with the correct parameters.
        """
        df = pd.DataFrame({'Salary': ['50K-100K'], 'Location': ['Remote'], 'Salary_Low': [50000.0], 'Salary_High': [100000.0], 'Average_Salary': [75000.0]})
        save_processed_data(df, 'dummy_path.csv')
        # Test: Ensure to_csv was called with the correct file path and index parameter
        mock_to_csv.assert_called_with('dummy_path.csv', index=False)

if __name__ == '__main__':
    unittest.main()