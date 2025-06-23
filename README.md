# 🔥 GitHub Trending Scraper

This project is a simple Python script that scrapes the **top 5 trending repositories** from [GitHub Trending](https://github.com/trending) using `requests` and `BeautifulSoup`, and saves the results in a CSV file.
 📌 Problem Statement
Use Python to extract repository names and links from [GitHub Trending](https://github.com/trending) and store them in a CSV file with two columns:
- **Repository Name**
- **Link**
🛠️ Technologies Used
- **Python** – Programming language
- **requests** – To fetch HTML content of GitHub Trending page
- **BeautifulSoup (bs4)** – For parsing and extracting data from HTML
- **csv module** – To save data in a `.csv` format
- **Git & GitHub** – Version control and code hosting
-  🧠 Approach
1. Send an HTTP GET request to `https://github.com/trending` using the `requests` library.
2. Parse the HTML using `BeautifulSoup` to find the top 5 repository blocks.
3. Extract each repository’s name and full GitHub link.
4. Store the extracted data in a CSV file named `github_trending.csv`.
5. Upload the script, CSV, and this README to a GitHub repository.
 📂 Files Included

| File Name             | Description                                      |
|-----------------------|--------------------------------------------------|
| `script.py`           | Python script that performs the web scraping     |
| `github_trending.csv` | Output file containing the top 5 trending repos  |
| `README.md`           | Project explanation and usage details            |
💻 How to Run
1. **Install dependencies** (if not already installed):
   ```bash
   pip install requests beautifulsoup4
   python script.py
Check the output file:
The script will generate a github_trending.csv file with 2 columns:
Repository Name
Link
