import unittest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
import pandas as pd
from scrape_books import fetch_page, parse_page, extract_books, extract_product_info, scrape_books, save_data

class TestScrapeBooks(unittest.TestCase):
    """
    This class contains unit tests for the scrape_books.py functions.
    Each test checks a specific function to ensure it behaves as expected.
    """

    @patch('scrape_books.requests.get')
    def test_fetch_page(self, mock_get):
        """
        Test the fetch_page function to ensure it correctly makes an HTTP GET request.
        
        Steps:
        1. Mock the `requests.get` method to simulate an HTTP request.
        2. Define a fake URL and pass it to the `fetch_page` function.
        3. Check if the `requests.get` method was called once with the correct URL.
        4. Verify that the returned response has a status code of 200, indicating success.
        """
        
        # Create a mock response object
        mock_response = Mock() 
        
        # Set the status code to 200 (OK)
        mock_response.status_code = 200  
        
        # Make the mock `requests.get` return the mock response
        mock_get.return_value = mock_response  
        
        url = 'http://example.com'
        response = fetch_page(url)
        
        # Check if `requests.get` was called with the URL
        mock_get.assert_called_once_with(url)  
        
        # Ensure the response status code is 200
        self.assertEqual(response.status_code, 200)  

    def test_parse_page(self):
        """
        Test the parse_page function to verify it correctly parses HTML content.
        
        Steps:
        1. Create a simple HTML string to simulate a web page.
        2. Mock a response object containing this HTML as its content.
        3. Pass the mocked response to the `parse_page` function.
        4. Ensure that the function returns a BeautifulSoup object.
        5. Verify that the parsed HTML content is correctly structured.
        """
        html_content = '<html><body><h1>Test</h1></body></html>'
        
        # Mock a response object
        response = Mock()  
        
        # Set the content of the response to our HTML
        response.content = html_content  
        
        soup = parse_page(response)
        
        # Check if the return type is BeautifulSoup
        self.assertIsInstance(soup, BeautifulSoup)  
        
        # Verify that the content is correctly parsed
        self.assertEqual(soup.h1.text, 'Test')  

    def test_extract_books(self):
        """
        Test the extract_books function to ensure it correctly extracts book data from HTML.
        
        Steps:
        1. Define a simple HTML structure representing a list of books.
        2. Parse this HTML into a BeautifulSoup object.
        3. Pass the BeautifulSoup object to the `extract_books` function.
        4. Verify that the function returns the correct book details, including title, price, availability, rating, and URL.
        """
        html_content = '''
        <html>
        <body>
            <article class="product_pod">
                <h3><a title="Book Title 1" href="book1.html">Book Title 1</a></h3>
                <p class="price_color">£10.00</p>
                <p class="instock availability">In stock</p>
                <p class="star-rating Three"></p>
            </article>
        </body>
        </html>
        '''
        
        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')  
        
        # Extract book details
        books = extract_books(soup)  
        
        # Ensure one book was found
        self.assertEqual(len(books), 1)  
        self.assertEqual(books[0], ['Book Title 1', '£10.00', 'In stock', 'Three', 'http://books.toscrape.com/catalogue/book1.html'])

    @patch('scrape_books.fetch_page')
    def test_extract_product_info(self, mock_fetch_page):
        """
        Test the extract_product_info function to ensure it correctly extracts product information.
        
        Steps:
        1. Mock the `fetch_page` function to simulate fetching a book's detail page.
        2. Define a simple HTML structure representing the product info table.
        3. Set this HTML as the content of the mock response.
        4. Pass a fake book URL to the `extract_product_info` function.
        5. Verify that the function correctly extracts and returns product information as a dictionary.
        """
        html_content = '''
        <html>
        <body>
            <table class="table table-striped">
                <tr><th>UPC</th><td>123456789</td></tr>
                <tr><th>Product Type</th><td>Book</td></tr>
            </table>
        </body>
        </html>
        '''
        # Mock a response object
        response = Mock()  
        
        # Set the content of the response to our HTML
        response.content = html_content  
        
        # Mock the `fetch_page` function to return this response
        mock_fetch_page.return_value = response 
        
        book_url = 'http://books.toscrape.com/catalogue/book1.html'
        product_info = extract_product_info(book_url)
        
        # Ensure `fetch_page` was called with the book URL
        mock_fetch_page.assert_called_once_with(book_url)  
        self.assertEqual(product_info, {'UPC': '123456789', 'Product Type': 'Book'})  

    @patch('scrape_books.fetch_page')
    @patch('scrape_books.extract_product_info')
    def test_scrape_books(self, mock_extract_product_info, mock_fetch_page):
        """
        Test the scrape_books function to ensure it correctly scrapes data from multiple pages.
        
        Steps:
        1. Mock the `fetch_page` function to simulate fetching book list pages.
        2. Mock the `extract_product_info` function to simulate fetching detailed book info.
        3. Define simple HTML structures representing a book list page and product info.
        4. Set these HTML structures as the content of the mock responses.
        5. Call the `scrape_books` function with a base URL and number of pages to scrape.
        6. Verify that the function correctly combines book details with product info and returns a DataFrame.
        """
        # Mock a response object
        mock_response = Mock() 
        
        # Set status code to 200 
        mock_response.status_code = 200  
        
        # Define a simple HTML for a book listing
        mock_response.content = '''
        <html>
        <body>
            <article class="product_pod">
                <h3><a title="Book Title 1" href="book1.html">Book Title 1</a></h3>
                <p class="price_color">£10.00</p>
                <p class="instock availability">In stock</p>
                <p class="star-rating Three"></p>
            </article>
        </body>
        </html>
        '''  
        # Mock `fetch_page` to return the book list HTML
        mock_fetch_page.return_value = mock_response  
        
        # Mock product info extraction
        mock_extract_product_info.return_value = {'UPC': '123456789', 'Product Type': 'Book'}  
        
        base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        
        # Scrape one page of books
        df = scrape_books(base_url, 1)  
        
        self.assertEqual(len(df), 1)  
        self.assertEqual(df.iloc[0]['Book Title'], 'Book Title 1')  
        self.assertEqual(df.iloc[0]['Price'], '£10.00')  
        self.assertEqual(df.iloc[0]['Availability'], 'In stock')  
        self.assertEqual(df.iloc[0]['Rating'], 'Three')  
        self.assertEqual(df.iloc[0]['UPC'], '123456789')  

    @patch('scrape_books.pd.DataFrame.to_csv')
    def test_save_data(self, mock_to_csv):
        """
        Test the save_data function to ensure it correctly saves a DataFrame to a CSV file.
        
        Steps:
        1. Create a simple DataFrame with book details.
        2. Define a file path where the CSV should be saved.
        3. Call the `save_data` function with the DataFrame and file path.
        4. Verify that the `to_csv` method was called once with the correct file path and parameters.
        """
        # Create a simple DataFrame
        df = pd.DataFrame({'Book Title': ['Book Title 1'], 'Price': ['£10.00']})  
        file_path = 'test_books_with_detailed_info.csv'
        
        save_data(df, file_path)
        
        # Check if `to_csv` was called with the correct path        
        mock_to_csv.assert_called_once_with(file_path, index=False)  

if __name__ == '__main__':
    unittest.main()