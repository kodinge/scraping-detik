import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detikPopuler():
    result = requests.get('https://www.detik.com/terpopuler')
    soup = BeautifulSoup(result.text, 'html.parser')
    news = soup.find(attrs={'class': 'grid-row list-content'})
    titles = news.findAll(attrs={'class': 'media__title'})
    images = news.findAll(attrs={'class': 'media__image'})
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
