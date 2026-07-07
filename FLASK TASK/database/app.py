from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student_db_data')
def get_students_info_from_db():

    student = {
        "name": "Karunya",
        "location": "Coimbatore"
    }

    return jsonify(student)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
