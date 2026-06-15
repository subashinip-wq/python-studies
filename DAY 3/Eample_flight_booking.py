from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flight Booking System</h1>
    <p>Flight Number: AI101</p>
    <p>Source: Delhi</p>
    <p>Destination: Mumbai</p>
    <p>Price: ₹5500</p>
    """
app.run(debug=True)
