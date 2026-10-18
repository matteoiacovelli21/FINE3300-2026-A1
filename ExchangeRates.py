import csv
# This class stores the exchange rate and provides a method to convert between USD and CAD.
class ExchangeRates:
    def __init__ (self,filename):
        with open (filename, "r") as file:
            # Open the CSV file and read the last row to get the latest exchange rate.
            reader = csv.DictReader(file)
            # Go through each row and keep the last row of data.
            for row in reader:
                last_row = row
        # Get the exchange rate from the last row and convert it to a number (float) for calculations.
        self.rate = float (last_row["FXAUSDCAD"])

    # This method converts USD to CAD, or CAD to USD.
    def convert (self, amount, from_currency, to_currency):
        # Multiply by the exchange rate when converting USD to CAD.
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        
        # Divide by the exchange rate when converting CAD to USD.
        elif from_currency == "CAD" and to_currency == "USD": 
            return amount / self.rate 
        
# Ask the user for the amount they want to convert and currencies they want to convert from and to.        
amount = float(input("Enter amount: " ))
from_currency = input ("From (USD or CAD) : ") .upper ()
to_currency = input ("To (USD or CAD) : ") .upper ()
# Create an object that reads the exchange rate from the CSV file.
rates = ExchangeRates ("BankOfCanadaExchangeRate.2026.csv")
# Convert the amount using the currencies entered by the user.
result = rates.convert (amount,from_currency, to_currency)
# Print the result of the converted amount rounded to two decimal places. 
print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
    