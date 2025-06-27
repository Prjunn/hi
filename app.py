from datetime import datetime
import csv
from flask import Flask, render_template

app = Flask(__name__)

def load_prices(path='data/prices.csv'):
    dates = []
    prices = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            date_str, price_str = row
            dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
            prices.append(float(price_str))
    return dates, prices

def linear_regression(xs, ys):
    n = len(xs)
    x_vals = list(range(n))
    sum_x = sum(x_vals)
    sum_y = sum(ys)
    sum_xx = sum(x * x for x in x_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, ys))
    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        return 0, ys[-1]
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

@app.route('/')
def index():
    dates, prices = load_prices()
    slope, intercept = linear_regression(dates, prices)
    next_index = len(prices)
    predicted = slope * next_index + intercept
    return render_template(
        'index.html', current=prices[-1], predicted=predicted)

if __name__ == '__main__':
    app.run(debug=True)
