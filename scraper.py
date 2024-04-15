import requests
from bs4 import BeautifulSoup

def scrape_website(url, headline_selector, summary_selector, url_selector):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all articles based on provided selectors
        articles = soup.find_all('article')

        # Extract and print information for each article
        for article in articles:
            # Extract headline
            headline = article.select_one(headline_selector)
            if headline:
                print("Headline:", headline.text.strip())

            # Extract summary
            summary = article.select_one(summary_selector)
            if summary:
                print("Summary:", summary.text.strip())

            # Extract URL
            url_element = article.select_one(url_selector)
            if url_element:
                article_url = url_element.get('href')
                print("URL:", article_url)

            print()  # Add a blank line for better readability between articles
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

# Example usage:
if __name__ == "__main__":
    url = "https://example.com/news"  # Replace with the URL of the news website
    headline_selector = ".headline"   # CSS selector for headline elements
    summary_selector = ".summary"     # CSS selector for summary elements
    url_selector = "a"                # CSS selector for URL elements

    scrape_website(url, headline_selector, summary_selector, url_selector)
