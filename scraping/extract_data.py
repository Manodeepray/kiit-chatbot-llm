import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import pandas as pd
import os
def extract_data_from_page(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return {}

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all the text content
    text_content = soup.get_text(separator='\n', strip=True)

    text_content = str(text_content)
    return text_content
        

def save_to_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:

    # Step 2: Write text to the file
        file.write(data)



if __name__ == "__main__":
    
    url_csv_path = input("enter the url csv path : ")
    df = pd.read_csv(url_csv_path)
    for link in df['URL']: 
        url = link
        extracted_data = extract_data_from_page(url)
        print(f"Data extracted from {url}:\n")

        '''print("Text Content:")
        print(extracted_data['text'][:50])  # Print the first 500 characters of text

        print("\nLinks:")
        for link in extracted_data['links']:
            print(link)

        print("\nImages:")
        for img in extracted_data['images']:
            print(img)'''
            
        link = link.replace("/" , "_")
        link = link.replace("https:" , "")
        
        csv_path = f"{link}.txt"
        extracted_data_csv_path = os.path.join("kiit-chatbot-llm\scraping\extracted_data",csv_path)
        # Save the extracted data to a CSV file
        save_to_txt(extracted_data, extracted_data_csv_path)
        print(f"Extracted data saved to {extracted_data_csv_path}")



#separate pdf etc etc
