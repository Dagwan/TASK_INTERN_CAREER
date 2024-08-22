import unittest
import pandas as pd
from io import StringIO
import os
from process_books import load_data, display_basic_info, clean_data, analyze_data, save_cleaned_data, main

class TestProcessBooks(unittest.TestCase):
    """
    Unit tests for functions in process_books.py.
    This test suite ensures that each function behaves as expected when handling data related to books.
    """

    def setUp(self):
        """
        Set up test data and environment before each test.
        
        This method prepares a mock CSV dataset in memory using StringIO and saves it as a CSV file.
        It also defines file paths that will be used in subsequent tests.
        """
        # Sample CSV data as a string to simulate reading from a CSV file
        self.csv_data = """Title,Author,Price,Rating
                            Book A,Author A,£10.99,Four
                            Book B,Author B,€12.50,Three
                            Book C,Author C,£7.99,One
                            Book D,Author D,,Five
                         """
        # Create a DataFrame from the sample data
        self.df = pd.read_csv(StringIO(self.csv_data))
        # Define file paths for the test and cleaned data files
        self.test_file_path = 'test_books.csv'
        self.cleaned_file_path = 'cleaned_test_books.csv'
        # Save the DataFrame to a CSV file to simulate a real file input
        self.df.to_csv(self.test_file_path, index=False)
    
    def tearDown(self):
        """
        Clean up the environment after each test.
        
        This method deletes the test and cleaned data files if they exist, ensuring no leftover files
        interfere with subsequent tests.
        """
        # Remove the test CSV file if it exists
        if os.path.isfile(self.test_file_path):
            os.remove(self.test_file_path)
        # Remove the cleaned CSV file if it exists
        if os.path.isfile(self.cleaned_file_path):
            os.remove(self.cleaned_file_path)
    
    def test_load_data(self):
        """
        Test the load_data function to ensure it correctly loads a CSV file into a DataFrame.
        
        The test checks:
        - Whether the loaded data is a DataFrame.
        - Whether the DataFrame contains the correct number of rows.
        """
        # Load the test CSV data using the function
        df = load_data(self.test_file_path)
        # Assert that the returned object is a DataFrame
        self.assertIsInstance(df, pd.DataFrame, "The loaded data should be a DataFrame.")
        # Assert that the DataFrame has 4 rows
        self.assertEqual(df.shape[0], 4, "The number of rows in the loaded DataFrame should be 4.")
    
    def test_load_data_file_not_found(self):
        """
        Test the load_data function for handling file not found errors.
        
        The test ensures that attempting to load a non-existent file raises a FileNotFoundError.
        """
        # Attempt to load a non-existing file and expect a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            load_data('non_existing_file.csv')
    
    def test_clean_data(self):
        """
        Test the clean_data function to ensure it properly cleans the dataset.
        
        The test checks:
        - That the 'Price' column is converted to a float data type.
        - That there are no missing values in the 'Price' column after cleaning.
        """
        # Clean the DataFrame using the function
        df = clean_data(self.df)
        # Check if the 'Price' column has been converted to float
        self.assertTrue(df['Price'].dtype == float, "The 'Price' column should be of type float.")
        # Check that there are no missing values in the 'Price' column after cleaning
        self.assertEqual(df['Price'].isnull().sum(), 0, "There should be no missing values in the 'Price' column after cleaning.")

    
    def test_analyze_data(self):
        """
        Test the analyze_data function to ensure it runs without errors.
        
        This test does not check the analysis results but ensures that the function
        executes successfully without raising any exceptions.
        """
        try:
            # Call the analyze_data function to ensure it runs without errors
            analyze_data(self.df)
        except Exception as e:
            # If an exception is raised, the test fails
            self.fail(f"analyze_data raised an exception: {e}")
    
    def test_save_cleaned_data(self):
        """
        Test the save_cleaned_data function to ensure it correctly saves the cleaned data to a CSV file.
        
        The test checks:
        - That the cleaned CSV file is created.
        """
        # Clean the DataFrame and save it using the function
        cleaned_df = clean_data(self.df)
        save_cleaned_data(cleaned_df, self.cleaned_file_path)
        # Check if the cleaned data file was created
        self.assertTrue(os.path.isfile(self.cleaned_file_path), "The cleaned data file should be created.")

    def test_main_workflow(self):
        """
        Test the entire main workflow to ensure it executes correctly.
        
        The test captures standard output to verify that the main function prints the expected success message.
        """
        from io import StringIO
        import sys

        # Redirect standard output to capture print statements
        output = StringIO()
        sys.stdout = output
        
        try:
            # Run the main function
            main()
            # Check if the success message was printed
            self.assertIn("Cleaned data successfully saved to", output.getvalue(), "The main workflow did not print the success message.")
        finally:
            # Restore standard output to its original state
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
