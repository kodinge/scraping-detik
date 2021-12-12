import requests
from bs4 import BeautifulSoup


class News:
    def __init__(self, url, description):
        self.url = url
        self.result = None
        self.description = description

    def get_data(self):
        print('scraping data')

    def tampil(self):
        print('tampil hasil scraping')

    def run(self):
        self.get_data()
        self.tampil()


class Kompas(News):
    def __init__(self, url):
        super(Kompas, self).__init__(url, 'to get the populer news in kompas.com')

    def get_data(self):
        try:
            result = requests.get(self.url)
        except Exception:
            return None
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            pop = soup.find(attrs={'class': 'col-bs10-7'})
            populer = pop.findChildren(attrs={'class': 'trenLatest__title'})
            hasil = []
            for popu in populer:
                hasil.append(popu.text)
            self.result = hasil
        else:
            return None

    def tampil(self):
        if self.result is None:
            print('Data tidak bisa didapatkan')
        for res in self.result:
            print(res)


class Detik(News):
    def __init__(self, url):
        super(Detik, self).__init__(url, 'to get the populer news in detik.com')

    def get_data(self):
        try:
            result = requests.get(self.url)
        except Exception:
            return None
        if result.status_code == 200:
            soup = BeautifulSoup(result.text, 'html.parser')
            news = soup.find(attrs={'class': 'grid-row list-content'})
            titles = news.findAll(attrs={'class': 'media__title'})
            # images = news.findAll(attrs={'class': 'media__image'})

            hasil = []
            for title in titles:
                hasil.append(title.text)
                # image = image.find('img')['title']
                # print(image)
            self.result = hasil
        else:
            return None

    def tampil(self):
        if self.result is None:
            print('Tidak bisa mendapat data')
            return
        for res in self.result:
            print(res)


if __name__ == '__main__':
    berita = input('Inputkan website beritu yang anda inginkan: ')
    if berita == 'detik':
        NewsDetik = Detik('https://www.detik.com/terpopuler/')
        NewsDetik.run()
    elif berita == 'kompas':
        NewsKompas = Kompas('https://www.kompas.com/tren/')
        NewsKompas.run()