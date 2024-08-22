import unittest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
import pandas as pd
from scrape_books import fetch_page, parse_page, extract_books, extract_product_info, scrape_books, save_data

class TestScrapeBooks(unittest.TestCase):

    @patch('scrape_books.requests.get')
    def test_fetch_page(self, mock_get):
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        url = 'http://example.com'
        response = fetch_page(url)
        
        mock_get.assert_called_once_with(url)
        self.assertEqual(response.status_code, 200)

    def test_parse_page(self):
        html_content = '<html><body><h1>Test</h1></body></html>'
        response = Mock()
        response.content = html_content
        
        soup = parse_page(response)
        
        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.h1.text, 'Test')

    def test_extract_books(self):
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
        soup = BeautifulSoup(html_content, 'html.parser')
        books = extract_books(soup)
        
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0], ['Book Title 1', '£10.00', 'In stock', 'Three', 'http://books.toscrape.com/catalogue/book1.html'])

    @patch('scrape_books.fetch_page')
    def test_extract_product_info(self, mock_fetch_page):
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
        response = Mock()
        response.content = html_content
        mock_fetch_page.return_value = response
        
        book_url = 'http://books.toscrape.com/catalogue/book1.html'
        product_info = extract_product_info(book_url)
        
        mock_fetch_page.assert_called_once_with(book_url)
        self.assertEqual(product_info, {'UPC': '123456789', 'Product Type': 'Book'})

    @patch('scrape_books.fetch_page')
    @patch('scrape_books.extract_product_info')
    def test_scrape_books(self, mock_extract_product_info, mock_fetch_page):
        mock_response = Mock()
        mock_response.status_code = 200
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
        mock_fetch_page.return_value = mock_response
        mock_extract_product_info.return_value = {'UPC': '123456789', 'Product Type': 'Book'}
        
        base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        df = scrape_books(base_url, 1)
        
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Book Title'], 'Book Title 1')
        self.assertEqual(df.iloc[0]['Price'], '£10.00')
        self.assertEqual(df.iloc[0]['Availability'], 'In stock')
        self.assertEqual(df.iloc[0]['Rating'], 'Three')
        self.assertEqual(df.iloc[0]['UPC'], '123456789')

    @patch('scrape_books.pd.DataFrame.to_csv')
    def test_save_data(self, mock_to_csv):
        df = pd.DataFrame({'Book Title': ['Book Title 1'], 'Price': ['£10.00']})
        file_path = 'books_with_detailed_info.csv'
        
        save_data(df, file_path)
        
        mock_to_csv.assert_called_once_with(file_path, index=False)

if __name__ == '__main__':
    unittest.main()
