from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_student_details')
def get_students_info():

    # Call Project 2
    response = requests.get("http://127.0.0.1:5001/student_db_data")

    # Convert JSON response into Python dictionary
    student_data = response.json()

    return jsonify(student_data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
