# Bitcoin Price Prediction Web App

This repository contains a simple Flask web application that demonstrates a very basic approach to predicting Bitcoin's price based on a small sample dataset.

## Running the Application

1. Install dependencies (Flask):
   ```bash
   pip install flask
   ```
2. Run the server:
   ```bash
   python app.py
   ```
3. Visit `http://localhost:5000` in your browser.

The prediction uses a simple linear regression over the data in `data/prices.csv` and is **not** meant for real trading decisions.
