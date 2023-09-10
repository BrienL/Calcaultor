from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    First_Num = int(request.form["FirstNum"])
    Operation = request.form["Operation"]
    Second_Num = int(request.form["SecNum"])
    note = ""
    colour = "alert-success"
    if Operation == "plus":
        result = First_Num + Second_Num
        note = "Addition was performed successfully"
    elif Operation == "minus":
        result = First_Num - Second_Num
        note = "Subtraction was performed successfully"
    elif Operation == "multiply":
        result = First_Num * Second_Num
        note = "Multiplication was performed successfully"
    elif Operation == "divide": 
        result = First_Num / Second_Num
        note = "Division was performed successfully"   
    else:
        note = "There is an error please try again"
        return render_template("simple.html", note=note)
        colour="alert-danger"
    return render_template("simple.html", result=result, note=note, colour=colour)


if __name__ == "__main__":
    app.run(debug=True)