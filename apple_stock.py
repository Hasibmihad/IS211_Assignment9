import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        page_content = response.read()

        soup = BeautifulSoup(page_content, 'html.parser')
        print(soup.prettify())
        # we need to look into  <table class="W(100%) M(0)" data-test="historical-prices">
        table = soup.find('table', class_='W(100%) M(0)')
       # for close price , i found class name <tr class="BdT Bdc($seperatorColor) C($tertiaryColor) H(36px)">
                 # <td class="Fz(xs)" colspan="7">
                  # <span>
                   # *Close price adjusted for splits.
                   #</span>
        rows = table.find_all('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
      
        for row in rows:
            date = row.find_all('span')[0].text
            close_price = row.find_all('span')[4].text

            #print(f"Date: {date}, Close Price: {close_price}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
