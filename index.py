from flask import Flask, render_template, url_for, request

CaloriesTotal = 0
ProtienTotal = 0
FiberTotal = 0

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    Calories_Num = int(request.form["CaloriesNum"])
    Protien_Num = int(request.form["ProtienNum"])
    Fiber_Num = int(request.form["FiberNum"])
    global CaloriesTotal
    global ProtienTotal
    global FiberTotal
    CaloriesTotal += Calories_Num 
    ProtienTotal += Protien_Num
    FiberTotal += Fiber_Num
    result = "Calories: " + str(CaloriesTotal) + " Protien: " + str(ProtienTotal) + " Fiber: " + str(FiberTotal)
    return render_template("index.html", result=result, CaloriesTotal=CaloriesTotal, ProtienTotal=ProtienTotal, FiberTotal=FiberTotal)

@app.route("/reset", methods=["POST"])
def reset():
    global CaloriesTotal
    global ProtienTotal
    global FiberTotal
    CaloriesTotal = 0
    ProtienTotal = 0
    FiberTotal = 0
    result = "Calories: " + str(CaloriesTotal) + " Protien: " + str(ProtienTotal) + " Fiber: " + str(FiberTotal)
    return render_template("index.html", result=result, CaloriesTotal=CaloriesTotal, ProtienTotal=ProtienTotal, FiberTotal=FiberTotal)


if __name__ == "__main__":
    app.run(debug=True)