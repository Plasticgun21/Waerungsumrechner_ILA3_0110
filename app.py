from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def is_valid_currency_code(code):
    return len(code) == 3 and code.isalpha()

def currency_converter(api_key, base_currency, target_currency, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data.get("result") == "success":
            exchange_rates = data.get('conversion_rates')

            if target_currency in exchange_rates:
                exchange_rate = exchange_rates[target_currency]
                converted_amount = amount * exchange_rate
                return f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}"
            else:
                return f"Currency '{target_currency}' not found in the exchange rates."
        else:
            return f"Error fetching data from API: {data.get('error-type')}"

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except Exception as err:
        return f"An unexpected error occurred: {err}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        api_key = "4ba72f3265f703a998baba49"  
        base_currency = request.form.get('base_currency').upper()
        target_currency = request.form.get('target_currency').upper()
        try:
            amount = float(request.form.get('amount'))
        except ValueError:
            result = "Invalid amount. Please enter a valid number."
            return render_template('index.html', result=result)

        if not is_valid_currency_code(base_currency) or not is_valid_currency_code(target_currency):
            result = "Invalid currency code. Please enter three-letter currency codes like USD or EUR."
        else:
            result = currency_converter(api_key, base_currency, target_currency, amount)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
