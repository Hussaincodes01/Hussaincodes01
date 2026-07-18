import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Failed to fetch contributions for {username}")
        return
    
    soup = BeautifulSoup(res.text, 'html.parser')
    days = soup.find_all('td', class_='ContributionCalendar-day')
    
    data = []
    for day in days:
        date = day.get('data-date')
        count = day.get('data-level') # level is easier for coloring
        if date:
            data.append({"date": date, "level": int(count)})
            
    os.makedirs('data', exist_ok=True)
    with open('data/contributions.json', 'w') as f:
        json.dump(data, f)
    print(f"Saved {len(data)} days of contributions")

if __name__ == "__main__":
    fetch_contributions('Hussaincodes01')
