from flask import Flask, request

app = Flask(__name__)

class Result:

    def calculate(self, regno, name, m1, m2, m3):

        total = m1 + m2 + m3
        average = total / 3

        # Result
        if m1 >= 35 and m2 >= 35 and m3 >= 35:
            status = "PASS"
        else:
            status = "FAIL"

        # Grade
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        return f"""
        <h1>Student Result</h1>

        <h3>Student Details</h3>
        Register Number : {regno}<br>
        Name : {name}<br><br>

        <h3>Marks</h3>
        Python : {m1}<br>
        AI : {m2}<br>
        Machine Learning : {m3}<br><br>

        <h3>Result Summary</h3>
        Total Marks : {total}<br>
        Average : {average:.2f}<br>
        Grade : {grade}<br>
        Status : {status}<br>
        """

result = Result()

@app.route("/")
def home():

    return """
    <h1>Exam Result Management System</h1>

    <form action="/result">

        Register Number:
        <input type="text" name="regno"><br><br>

        Student Name:
        <input type="text" name="name"><br><br>

        Python Mark:
        <input type="number" name="m1"><br><br>

        AI Mark:
        <input type="number" name="m2"><br><br>

        Machine Learning Mark:
        <input type="number" name="m3"><br><br>

        <input type="submit" value="Generate Result">

    </form>
    """

@app.route("/result")
def show_result():

    regno = request.args.get("regno")
    name = request.args.get("name")

    m1 = int(request.args.get("m1"))
    m2 = int(request.args.get("m2"))
    m3 = int(request.args.get("m3"))

    return result.calculate(regno, name, m1, m2, m3)

app.run(debug=True)
