from flask import Flask, request, render_template

app = Flask(__name__)

class Result:

    def calculate(self, m1, m2, m3):

        total = m1 + m2 + m3
        average = total / 3

        if m1 >= 35 and m2 >= 35 and m3 >= 35:
            status = "PASS"
        else:
            status = "FAIL"

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

        return total, average, grade, status

result = Result()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result")
def show_result():

    regno = request.args.get("regno")
    name = request.args.get("name")

    m1 = int(request.args.get("m1"))
    m2 = int(request.args.get("m2"))
    m3 = int(request.args.get("m3"))

    total, average, grade, status = result.calculate(m1, m2, m3)

    return render_template(
        "result.html",
        regno=regno,
        name=name,
        m1=m1,
        m2=m2,
        m3=m3,
        total=total,
        average=average,
        grade=grade,
        status=status
    )

app.run(debug=True)
