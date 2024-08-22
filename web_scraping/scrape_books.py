import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    """
    Send a GET request to the specified URL and return the response object.
    
    Parameters:
    url (str): The URL to fetch.
    
    Returns:
    requests.Response: The response object from the GET request.
    """
    response = requests.get(url)
    return response

def parse_page(response):
    """
    Parse the content of the response using BeautifulSoup.
    
    Parameters:
    response (requests.Response): The response object to parse.
    
    Returns:
    BeautifulSoup: The parsed BeautifulSoup object.
    """
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_books(soup):
    """
    Extract book details and links from the BeautifulSoup object.
    
    Parameters:
    soup (BeautifulSoup): The BeautifulSoup object containing the page content.
    
    Returns:
    list of lists: A list where each sublist contains details of a book and its URL.
    """
    book_data = []
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        # Extract rating by checking the class of the <p> tag containing the rating
        rating_class = book.find('p', class_='star-rating')['class'][1]
        rating = rating_class
        
        # Get the link to the individual book page
        book_url = book.h3.a['href']
        full_book_url = f"http://books.toscrape.com/catalogue/{book_url}"
        
        book_data.append([title, price, availability, rating, full_book_url])
    
    return book_data

def extract_product_info(book_url):
    """
    Extract detailed product information from a book's detail page.
    
    Parameters:
    book_url (str): The URL of the book's detail page.
    
    Returns:
    dict: A dictionary containing detailed product information.
    """
    response = fetch_page(book_url)
    soup = parse_page(response)
    
    # Extract product information
    product_info = {}
    info_table = soup.find('table', class_='table table-striped')
    if info_table:
        rows = info_table.find_all('tr')
        for row in rows:
            key = row.find('th').text.strip()
            value = row.find('td').text.strip()
            product_info[key] = value
    
    return product_info

def scrape_books(base_url, pages):
    """
    Scrape books from multiple pages and return the collected data.
    
    Parameters:
    base_url (str): The base URL of the website with a placeholder for page numbers.
    pages (int): The number of pages to scrape.
    
    Returns:
    pd.DataFrame: A DataFrame containing all the scraped book data.
    """
    all_books = []
    
    for page in range(1, pages + 1):
        url = base_url.format(page)
        response = fetch_page(url)
        
        if response.status_code == 200:
            print(f"Successfully fetched page {page}")
            soup = parse_page(response)
            books = extract_books(soup)
            
            for book in books:
                title, price, availability, rating, book_url = book
                product_info = extract_product_info(book_url)
                # Combine the book's main info with its detailed product info
                book_data = {
                    'Book Title': title,
                    'Price': price,
                    'Availability': availability,
                    'Rating': rating,
                    'Book URL': book_url
                }
                # Add detailed info to the book data
                book_data.update(product_info)  
                all_books.append(book_data)
        else:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            break
    
    # Create a DataFrame to store the data
    df = pd.DataFrame(all_books)
    return df

def save_data(df, file_path):
    """
    Save the DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path to save the CSV file.
    """
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# Main workflow
def main():
    # Define the base URL and number of pages to scrape
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    num_pages = 5
    output_file_path = 'books_with_detailed_info.csv'
    
    # Scrape the books and get the DataFrame
    df = scrape_books(base_url, num_pages)
    
    # Display the data
    print(df)
    
    # Save the data to a CSV file
    save_data(df, output_file_path)

# Run the main workflow
if __name__ == "__main__":
    main()