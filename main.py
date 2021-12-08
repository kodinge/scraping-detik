import requests
from bs4 import BeautifulSoup


def get_data():
    result = requests.get('https://www.detik.com/terpopuler')
    soup = BeautifulSoup(result.text, 'html.parser')
    news = soup.find(attrs={'class': 'grid-row list-content'})
    titles = news.findAll(attrs={'class': 'media__title'})
    images = news.findAll(attrs={'class': 'media__image'})

    for image in images:
        # print(title.text)
        image = image.find('img')['title']
        print(image)


if __name__ == '__main__':
    get_data()
