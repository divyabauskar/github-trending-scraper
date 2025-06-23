import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
URL = "https://github.com/trending"

# Send HTTP GET request
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all repository elements
    repo_list = soup.find_all('article', class_='Box-row')[:5]  # Only top 5

    # Prepare data list
    data = []

    for repo in repo_list:
        # Extract repo name and URL
        full_repo_name = repo.h2.a.get_text(strip=True).replace(' / ', '/')
        repo_url = "https://github.com" + repo.h2.a['href']
        data.append([full_repo_name, repo_url])

    # Save to CSV
    with open("github_trending.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Repository Name", "Link"])
        writer.writerows(data)

    print("Top 5 trending repositories saved to github_trending.csv")

else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
