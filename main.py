import requests

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

                print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
            else:
                print(f"Currency '{target_currency}' not found in the exchange rates.")
        else:
            print(f"Error fetching data from API: {data.get('error-type')}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

def main():

    api_key = "4ba72f3265f703a998baba49"  

    while True:
        base_currency = input("Enter the base currency (e.g., CHF): ").upper()
        if is_valid_currency_code(base_currency):
            break
        print("Invalid currency code. Please enter a three-letter code like USD or EUR.")

    while True:
        target_currency = input("Enter the target currency (e.g., USD): ").upper()
        if is_valid_currency_code(target_currency):
            break
        print("Invalid currency code. Please enter a three-letter code like USD or EUR.")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount > 0:
                break
            print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    currency_converter(api_key, base_currency, target_currency, amount)

if __name__ == "__main__":
    main()
