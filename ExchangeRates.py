import csv
class ExchangeRates:
    def __init__ (self,filename):
        with open (filename, encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_row = row
        self.rate = float (last_row["FXAUSDCAD"])

    def convert (self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD": 
            return amount / self.rate 
        
amount = float(input("Enter amount" ))
from_currency = input ("From (USD or CAD) : ") .upper ()
to_currency = input ("To (USD or CAD) : ") .upper ()

rates = ExchangeRates ("BankOfCanadaExchangeRate.2026.csv")
result = rates.convert (amount,from_currency, to_currency)

print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
    