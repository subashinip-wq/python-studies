from flask import Flask, render_template
import requests
import json
import os

app = Flask(__name__)

# -----------------------------
# GoldAPI Configuration
# -----------------------------

API_KEY = "goldapi-724936db914b460708f7151fc7e8c925-io"
TROY_OUNCE_IN_GRAMS = 31.1035

PREVIOUS_FILE = "previous_prices.json"


# -----------------------------
# Previous Price Functions
# -----------------------------

def get_previous_prices():

    if os.path.exists(PREVIOUS_FILE):
        with open(PREVIOUS_FILE, "r") as file:
            return json.load(file)

    return {
        "gold24": 0,
        "gold22": 0,
        "silver": 0
    }


def save_prices(prices):

    with open(PREVIOUS_FILE, "w") as file:
        json.dump(prices, file, indent=4)


# -----------------------------
# GoldAPI Function
# -----------------------------

def get_price(metal):

    url = f"https://www.goldapi.io/api/{metal}/INR"

    headers = {
        "x-access-token": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["price"]

        else:
            print("API Error:", response.text)
            return None

    except Exception as e:
        print("Request Error:", e)
        return None


# -----------------------------
# Conversion Functions
# -----------------------------

def to_10gram(price):

    return round((price / TROY_OUNCE_IN_GRAMS) * 10, 2)


def to_kg(price):

    return round((price / TROY_OUNCE_IN_GRAMS) * 1000, 2)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -----------------------------
# Rates Page
# -----------------------------

@app.route("/rates")
def rates():

    gold_price = get_price("XAU")
    silver_price = get_price("XAG")

    # -----------------------------
    # Demo Prices if API Fails
    # -----------------------------

    if gold_price is None:
        gold_price = 398700.00

    if silver_price is None:
        silver_price = 5940.00

    rates = {

        "gold24": to_10gram(gold_price),

        "gold22": round(to_10gram(gold_price) * 0.916, 2),

        "silver": to_kg(silver_price)

    }

    previous = get_previous_prices()

    trends = {

        "gold24": "▲" if rates["gold24"] >= previous["gold24"] else "▼",

        "gold22": "▲" if rates["gold22"] >= previous["gold22"] else "▼",

        "silver": "▲" if rates["silver"] >= previous["silver"] else "▼"

    }

    save_prices(rates)

    return render_template(
        "rates.html",
        rates=rates,
        trends=trends
    )


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# -----------------------------
# Run Flask
# -----------------------------

if __name__ == "__main__":

    app.run(debug=True)
