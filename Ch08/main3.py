from bs4 import BeautifulSoup
import cloudscraper

def get_exchange_rate(target1, target2):
    scraper = cloudscraper.create_scraper()
    content = scraper.get(f'https://kr.investing.com/currencies/{target1}-{target2}')

    soup = BeautifulSoup(content.text, 'html.parser')
    containers = soup.find('div', {'data-test': 'instrument-price-last'})
    print(f"{target1}-{target2} 환율: {containers.text}")

get_exchange_rate('usd', 'krw')