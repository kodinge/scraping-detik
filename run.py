import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-populer')
def detikPopuler():
    result = requests.get('https://www.detik.com/terpopuler')
    soup = BeautifulSoup(result.text, 'html.parser')
    news = soup.find(attrs={'class': 'grid-row list-content'})
    titles = news.findAll(attrs={'class': 'media__title'})
    images = news.findAll(attrs={'class': 'media__image'})
    return render_template('detik-scraping.html', images=images)


@app.route('/idr-rates')
def idrRates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    data = source.json().values()
    return render_template('idr-rates.html', datas=data)


if __name__ == '__main__':
    app.run(debug=True)
