import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
page = requests.get("https://medium.com/")

# Parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Get all the links
links = soup.find_all('a')

# Order the links by the number of times they appear in the page
links = sorted(links, key=lambda x: str(x).count('href'), reverse=True)

# Create a dictionary with the links and https as a key
links = {link.get('href'): 'https' in link.get('href') for link in links}

# Filter the links that are not https
links = {link: https for link, https in links.items() if https}

# Extract the links to json file
with open('reports/links.json', 'w') as f:
    json.dump(links, f)


    
