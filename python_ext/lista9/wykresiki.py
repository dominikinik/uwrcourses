import requests
import matplotlib.pyplot as plt
from requests.exceptions import HTTPError
import pandas as pd
import math
from random import randrange


def get_rates_of_currency():
    currency = 'gbp'
    rates_number = 255
    try:
        url = f'http://api.nbp.pl/api/' \
              f'exchangerates/rates/a/' \
              f'{currency}/' \
              f'last/{rates_number}/' \
              f'?format=json'
        response = requests.get(url)
    except HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        if response.status_code == 200:
            return response.json()


def get_rates():
    base = "USD"
    out_curr = "RUB"
    start_date = "2020-01-03"
    end_date = "2023-01-04"
    url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(
        base, start_date, end_date, out_curr)
    response = requests.get(url)
    response = requests.get(url)
    data = response.json()
    rates = []

    for i, j in data["rates"].items():
        rates.append([i, j[out_curr]])
    df = pd.DataFrame(rates)

    df.columns = ["date", "rate"]
    return df


def przew(dane):
    dane2 = []
    for i in range(366):
        dane2.append((dane[i]-dane[randrange(366)] +
                     dane[randrange(366)]+math.sin(i)))
    return dane2


if __name__ == '__main__':

    vod = get_rates_of_currency()
    Rates = [i['mid'] for i in vod['rates']]
    Qty = [i['effectiveDate'] for i in vod['rates']]

    vod2 = get_rates()
    x = vod2['date']
    y = vod2['rate']
    print(len(x))
    plt.plot(Qty, Rates)
    plt.title('latapoprzednie')
    plt.xlabel("czas")
    plt.ylabel("pln")
    plt.legend(['GBP/PLN'])
    plt.show()
    plt.plot(x, y)
    plt.legend(['USD/RUB'])
    plt.title('latapoprzednie')
    plt.xlabel("czas")
    plt.ylabel("rub")
    plt.show()
    plt.plot(x, przew(y))
    plt.legend(['USD/RUB'])
    plt.title('przewidywania')
    plt.xlabel("czas")
    plt.ylabel("rub")
    plt.show()
