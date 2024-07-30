import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import os
def get_all_links(main_url):
    # Send a GET request to the main URL
    response = requests.get(main_url)
    if response.status_code != 200:
        print(f"Failed to access {main_url}")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all anchor tags
    anchor_tags = soup.find_all('a')

    # Get the href attribute from each anchor tag
    links = set()
    for tag in anchor_tags:
        href = tag.get('href')
        if href:
            # Join the URL if it's relative
            full_url = urljoin(main_url, href)
            # Ensure the link is within the same domain
            if urlparse(full_url).netloc == urlparse(main_url).netloc:
                links.add(full_url)

    return list(links)

def save_to_csv(links, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])  # Write the header
        for link in links:
            writer.writerow([link])
    
    

if __name__ == "__main__":
    main_url = input("enter the main home page url : ")  #"https://example.com"  # Replace with the main home page URL
    file_name = input("enter the main home page name : ")
    file_name = file_name + ".csv"
    csv_file_path = os.path.join("src\csv",file_name)
    related_pages = get_all_links(main_url)
    print(f"Related pages found: {len(related_pages)}")
    for page in related_pages:
        print(page)
        
    save_to_csv(related_pages, csv_file_path)
    print(f"Related pages saved to {csv_file_path}")
