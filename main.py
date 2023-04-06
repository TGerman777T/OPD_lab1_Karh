from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://www.omgtu.ru/l/?SHOWALL_1=1'
    page = requests.get(url)
    News = []
    filteredNews = []
    soup = BeautifulSoup(page.text, "html.parser")
    News = soup.findAll('h3', class_='news-card__title')
    for data in News:
        filteredNews.append(data.text)
    for data in filteredNews:
        print(data)