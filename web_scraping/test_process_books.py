import unittest
import pandas as pd
from io import StringIO
import os
from process_books import load_data, display_basic_info, clean_data, analyze_data, save_cleaned_data, main

class TestProcessBooks(unittest.TestCase):

    def setUp(self):
        """
        Set up test data and environment.
        """
        self.csv_data = """Title,Author,Price,Rating
                            Book A,Author A,£10.99,Four
                            Book B,Author B,€12.50,Three
                            Book C,Author C,£7.99,One
                            Book D,Author D,,Five
                         """
        self.df = pd.read_csv(StringIO(self.csv_data))
        self.test_file_path = 'test_books.csv'
        self.cleaned_file_path = 'cleaned_test_books.csv'
        self.df.to_csv(self.test_file_path, index=False)
    
    def tearDown(self):
        """
        Clean up files after tests.
        """
        if os.path.isfile(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.isfile(self.cleaned_file_path):
            os.remove(self.cleaned_file_path)
    
    def test_load_data(self):
        df = load_data(self.test_file_path)
        self.assertIsInstance(df, pd.DataFrame, "The loaded data should be a DataFrame.")
        self.assertEqual(df.shape[0], 4, "The number of rows in the loaded DataFrame should be 4.")
    
    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data('non_existing_file.csv')
    
    def test_clean_data(self):
        df = clean_data(self.df)
        # Implement logic to handle missing values in the 'Price' column (e.g., replace with 0 or remove rows)
        self.assertTrue(df['Price'].dtype == float, "The 'Price' column should be of type float.")
        # Adjust assertion based on your missing value handling logic
        self.assertEqual(df['Price'].isnull().sum(), 0, "There should be no missing values in the 'Price' column after cleaning.")

    
    def test_analyze_data(self):
        try:
            analyze_data(self.df)
        except Exception as e:
            self.fail(f"analyze_data raised an exception: {e}")
    
    def test_save_cleaned_data(self):
        cleaned_df = clean_data(self.df)
        save_cleaned_data(cleaned_df, self.cleaned_file_path)
        self.assertTrue(os.path.isfile(self.cleaned_file_path), "The cleaned data file should be created.")


    def test_main_workflow(self):
        from io import StringIO
        import sys

        output = StringIO()
        sys.stdout = output
        
        try:
            main()
            self.assertIn("Cleaned data successfully saved to", output.getvalue(), "The main workflow did not print the success message.")
        finally:
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
