import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        page_content = response.read()
        soup = BeautifulSoup(page_content, 'html.parser')
        table = soup.find('table', class_='wikitable sortable')
        rows = table.find_all('tr')
        recent_years = min(10, len(rows) - 1)  
        for row in rows[1:recent_years + 1]:  
            columns = row.find_all('td')
            year = columns[0].text.strip()
            winning_team = columns[2].text.strip()
            losing_team = columns[4].text.strip()

            print(f"Year: {year}, Winning Team: {winning_team}, Losing Team: {losing_team}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
