import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# List to store book data
book_data = []

# Loop through multiple pages (Adjust the range to the number of pages you want to scrape)
for page in range(1, 51):  
    # Construct the URL for the current page
    url = base_url.format(page)
    
    # Send a GET request to the current page
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully fetched page {page}")
        
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract book details including title, price, availability, rating, and link to individual pages
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
    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
        break

# Create a DataFrame to store the data
df = pd.DataFrame(book_data, columns=['Title', 'Price', 'Availability', 'Rating', 'Book URL'])

# Display the data
print(df)

# Save the data to a CSV file
df.to_csv('books_with_ratings_and_links_all_pages.csv', index=False)
print("Data saved to books_with_ratings_and_links_all_pages.csv")
