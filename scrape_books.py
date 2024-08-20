import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    """
    Send a GET request to the specified URL and return the response object.
    
    Parameters:
    url (str): The URL to fetch.
    
    Return:
    requests.Response: The response object from the GET request."""
    
    response = requests.get(url)
    return response

def parse_page(response):
    """
    Parse the content of the response using BeautifulSoup.
    
    Parameters:
    response (request.Response): The response object to parse.
    
    Returns:
    beautifulSoup: The parsed BeautifulSoup object.
    """
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_books(soup):
    """
    Extract book details from the BeautifulSoup object.
    
    Parameters:
    soup (BeautifulSoup)"""