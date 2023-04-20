from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://www.omgtu.ru/l/?SHOWALL_1=1'
    page = requests.get(url)
    News = []
    soup = BeautifulSoup(page.text, "html.parser")
    News = soup.findAll('h3', class_='news-card__title')
    for data in News:
        z = data.text.strip()
        print(z)


def pr():
    url = 'https://www.omgtu.ru/l/?SHOWALL_1=1'
    page = requests.get(url)
    News = []
    soup = BeautifulSoup(page.text, "html.parser")
    News = soup.findAll('h3', class_='news-card__title')
    for data in News:
        z = data.text.strip()
        with open("News.txt", "a", encoding='utf-8') as f:
            f.write(z + "\n")
    f.close()
