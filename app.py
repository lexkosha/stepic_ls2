# Импорты
from flask import Flask, render_template

from data import *

app = Flask(__name__)


@app.route('/')
def get_index():
    """Главная страница"""
    data = data_list[:6]
    return render_template('index.html', data=data)


@app.route('/departures/<url>/')
def det_departures(url):
    """Направления"""
    data = []
    night = []
    price = []
    for i in data_list:
        if url == i['departure']:
            data.append(i)
            night.append(i['nights'])
            price.append(i['price'])
    context = {
        'data': data,
        'night': night,
        'price': price,
        'departures': departures.get(url),
    }
    return render_template('departure.html', context=context)


@app.route('/tours/')
def get_tours():
    """Туры"""
    data = tours
    meta_data = {
        'title': title,
        'description': description,
    }
    return render_template('tour.html', data=data, meta=meta_data)



if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)