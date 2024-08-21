# Book Scraper Script

The **Book Scraper Script** is a Python application designed to scrape book information from an online bookstore (e.g., "Books to Scrape"). This script collects detailed data about books, including their title, price, availability, rating, and additional product-specific information.

## Overview

This project is a web scraper built to extract comprehensive details about books listed on a website. It scrapes data from multiple pages of books and retrieves additional product information by visiting each book's individual page.

#### to be updated [Software Demo Video](https://youtu./xGGPXlK9Lvs)

### Key Features:

- **Scrape Multiple Pages:** Automatically navigate through multiple pages of books to collect data.
- **Product Information Extraction:** Retrieve detailed product information, including UPC, Product Type, Price (excl. tax), Price (incl. tax), tax, availability, and the number of reviews.
- **Data Storage:** Store the scraped data in a structured format (CSV) for easy access and analysis.

### Scraped Information:

- **Main Book Page:**
  - **Title:** The title of the book.
  - **Price:** The price of the book.
  - **Availability:** Whether the book is in stock.
  - **Rating:** The book's rating based on the website's star system.
  - **Book URL:** The link to the book's detail page.

- **Product Information Page:**
  - **UPC:** Universal Product Code for the book.
  - **Product Type:** The category/type of the book.
  - **Price (excl. tax):** The price of the book excluding tax.
  - **Price (incl. tax):** The price of the book including tax.
  - **Tax:** The tax amount on the book.
  - **Availability:** The stock status of the book.
  - **Number of Reviews:** How many reviews the book has received.

## Development Environment

The Book Scraper Script was developed using the following tools:

- **Python:** A powerful programming language for general-purpose programming.
- **BeautifulSoup:** A library used to parse HTML and extract information from web pages.
- **Requests:** A simple HTTP library for Python, used to send HTTP requests.
- **Pandas:** A data manipulation and analysis library, used to organize and save the scraped data.

## Installation

To install the necessary dependencies, run the following command:

## bash
pip install requests beautifulsoup4 pandas

## How to Run the Script
### Running the Script Locally
- Clone the project repository from GitHub to your local machine.

* git clone "repository-url"
* cd "repository-directory"

## Install Dependencies:
Ensure all required libraries are installed using the command:
pip install -r requirements.txt

## Run the Script:
Execute the scripts by running one by one:
- python book_scraper.py
- python process_books.py

## Check the Output:
The script will create a CSV file named books_with_detailed_info.csv containing all the scraped data. 

## Script Workflow
- Fetching Pages:
The script fetches the HTML content from the website's pages.
- Parsing Pages:
It then parses the HTML using BeautifulSoup to find book details and their corresponding links.
- Extracting Data:
The script visits each book's page to extract detailed product information.
- Storing Data:
All the scraped data is stored in a CSV file for easy access and analysis.

## Future Work

While the current version of the Book Scraper Script provides essential functionality, there are several areas for improvement and future enhancements:

- **Error Handling:** Implement more robust error handling to manage network issues or changes in website structure.
- **Performance Optimization:** Improve the scraping speed by using asynchronous requests.
- **Scrape Additional Data:** Expand the script to collect more detailed information, such as book descriptions, author details, and publication dates.
- **Logging:** Add logging to monitor the scraping process and record any issues or errors encountered.

---------------------------------------------------------------------------------------------------------------------------------

## Useful Websites

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Pandas Documentatio](https://pandas.pydata.org/docs/index.html)


### License

This project is licensed under the MIT License - see the [LICENSE](/docs/LICENSE) file for details.