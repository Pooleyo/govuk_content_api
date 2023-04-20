import requests
import csv
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url_root = "https://www.gov.uk/api/content"

# Connect to the file I just downloaded
filename = r'C:\Users\apool\Downloads\2023-04-13 Technical exercise base paths for 271122 - Senior Data Scientist.csv'

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    first_column = [row[0] for row in reader]

sample_landing = first_column[1:10]
print(sample_landing)
for landing_page in sample_landing:
    print(landing_page)
    url = url_root + landing_page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(strip=True)
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)
        for key in scores:
            print(f"{key}: {scores[key]}")
    
    else:
        print("Error: ", response.status_code)