from flask import Flask, render_template, request
from main import currency_converter, is_valid_currency_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        base_currency = request.form["base_currency"].upper()
        target_currency = request.form["target_currency"].upper()
        amount = float(request.form["amount"])

        if is_valid_currency_code(base_currency) and is_valid_currency_code(target_currency):
            api_key = "4ba72f3265f703a998baba49" 
            result = currency_converter(api_key, base_currency, target_currency, amount)
        else:
            result = "Invalid currency codes provided."

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=False)