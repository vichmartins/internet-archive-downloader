import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from iadl.extensions import ALL_EXTENSIONS

class InternetArchiveScraper:
    def __init__(self, url="https://archive.org", item_id="rr-sega-mega-cd"):
        """Initialize the scraper with the URL and collection ID"""
        self.url = url
        self.item_id = item_id
        self.session = requests.Session()
    
    def get_file_links(self, file_extensions=None, show_links=False):
        """
        Scrape all file links from the collection.
        If file_extensions is provided, only include files with matching extensions.
        If file_extensions is None, include all files.
        If show_links is True, display the file links in a prettier format.
        """
        if file_extensions is None:
            file_extensions = ALL_EXTENSIONS
        
        print(f"Visiting {self.url}/details/{self.item_id}...")
        
        try:
            # Visit the main page first
            response = self.session.get(f"{self.url}/details/{self.item_id}")
            response.raise_for_status()
            print("Main page fetched successfully.")
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            print("Parsed main page HTML.")
            
            # Find all download links
            download_links = soup.select('a[href*="/download/"]')
            print(f"Found {len(download_links)} download links.")
            
            # Filter links by file extensions (if provided)
            file_links = []
            for link in download_links:
                href = link.get('href', '')
                if any(href.endswith(ext) for ext in file_extensions):
                    full_url = urljoin(self.url, href)
                    file_links.append(full_url)
            
            # Display file links in a prettier format if show_links is True
            if show_links and file_links:
                print("\n=== File Links ===")
                for i, file_url in enumerate(file_links, 1):
                    print(f"{i:>3}. {file_url}")
                print("==================\n")
        
            return file_links
        
        except Exception as e:
            print(f"Error scraping file links: {str(e)}")
            return []