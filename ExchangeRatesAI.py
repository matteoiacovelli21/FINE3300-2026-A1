"""
ExchangeRatesAI.py
==================
FINE 3300 (Fall 2026) - Assignment #1, Part 2: Vibe Coding

AI-generated version of the Part 1 exchange rate calculator.
Model used: Claude Opus 5.5 (Anthropic, model ID: claude-opus-5-5)

What the program does
---------------------
1. Reads the Bank of Canada annual exchange rate file (CSV).
2. Takes the most recent USD/CAD rate (the last row of the file).
3. Prompts the user for an amount, a 'from' currency and a 'to' currency
   (USD or CAD) and prints the converted amount, rounded to the nearest cent.

About the rate
--------------
Column FXAUSDCAD is quoted as Canadian dollars per 1 U.S. dollar, so:
    USD -> CAD : multiply by the rate
    CAD -> USD : divide by the rate

Data source: Bank of Canada, annual exchange rates
(BankOfCanadaExchangeRate.2026.csv, provided on Canvas).

Run from the repository folder:
    python ExchangeRatesAI.py
"""

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

# The CSV is looked up next to this script rather than in the terminal's
# current folder, so the program works however VS Code launches it.
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_FILE_NAME = "BankOfCanadaExchangeRate.2026.csv"


class ExchangeRates:
    """Convert amounts between CAD and USD using Bank of Canada data.

    The rate is read once, when the object is created, so every call to
    convert() reuses it without re-opening the file.
    """

    DATE_COLUMN = "Date"
    USD_CAD_COLUMN = "FXAUSDCAD"          # CAD per 1 USD (annual rate)
    SUPPORTED_CURRENCIES = ("USD", "CAD")
    CENT = Decimal("0.01")                # rounding unit for money

    def __init__(self, file_path):
        """Store the file path and load the latest USD/CAD rate from it."""
        self.file_path = Path(file_path)
        self.rate_date, self.usd_cad_rate = self._read_latest_rate()

        # Value of one unit of each currency, expressed in CAD. Every
        # conversion goes through CAD:  amount x (from in CAD) / (to in CAD).
        # Adding another currency later only means adding one entry here.
        self._cad_per_unit = {
            "CAD": Decimal("1"),
            "USD": self.usd_cad_rate,
        }

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def convert(self, amount, from_currency, to_currency):
        """Convert `amount` from one currency to the other.

        `amount` can be an int, float, str or Decimal. Currency codes are
        case-insensitive ("usd" works). Returns a Decimal rounded to the
        nearest cent (half-up, the usual rule for money).
        """
        source = self._normalize_code(from_currency)
        target = self._normalize_code(to_currency)

        # str() first so a float such as 0.1 isn't turned into
        # 0.1000000000000000055511151231257827...
        value = Decimal(str(amount))

        # Multiply before dividing to keep full precision until the end.
        converted = value * self._cad_per_unit[source] / self._cad_per_unit[target]
        return converted.quantize(self.CENT, rounding=ROUND_HALF_UP)

    def get_rate(self, from_currency, to_currency):
        """Return how many units of `to_currency` one unit of `from_currency` buys."""
        source = self._normalize_code(from_currency)
        target = self._normalize_code(to_currency)
        return self._cad_per_unit[source] / self._cad_per_unit[target]

    @classmethod
    def format_amount(cls, amount, currency):
        """Format money for display, e.g. Decimal('1234.5') -> '$1,234.50 USD'.

        Rounds half-up to the cent first; Python's built-in formatting
        would otherwise round half-to-even (1234.565 -> 1234.56).
        """
        cents = Decimal(str(amount)).quantize(cls.CENT, rounding=ROUND_HALF_UP)
        return f"${cents:,.2f} {currency.strip().upper()}"

    def __str__(self):
        """Describe the rate in use, e.g. for printing the object."""
        return (f"1 USD = {self.usd_cad_rate} CAD "
                f"(Bank of Canada, {self.rate_date})")

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _read_latest_rate(self):
        """Return (date, rate) from the last row that has a USD/CAD value.

        The file is in chronological order, so the last row holds the
        latest rate. A row with a blank USD/CAD cell is skipped in case the
        newest year has not been filled in yet.
        """
        latest_row = None

        # utf-8-sig removes the invisible byte-order mark that Excel adds to
        # CSVs; without it the first header would read '﻿Date'.
        with self.file_path.open(newline="", encoding="utf-8-sig") as csv_file:
            for row in csv.DictReader(csv_file):
                if (row.get(self.USD_CAD_COLUMN) or "").strip():
                    latest_row = row

        if latest_row is None:
            raise ValueError(
                f"No {self.USD_CAD_COLUMN} rate found in {self.file_path.name}"
            )

        # Decimal(str) keeps the rate exactly as printed in the file
        # (1.3978), avoiding the tiny errors a float would carry.
        rate = Decimal(latest_row[self.USD_CAD_COLUMN].strip())
        return latest_row[self.DATE_COLUMN], rate

    def _normalize_code(self, currency):
        """Clean up a currency code (' usd ' -> 'USD') and check it is supported."""
        code = str(currency).strip().upper()
        if code not in self.SUPPORTED_CURRENCIES:
            raise ValueError(
                f"Unsupported currency '{currency}'. "
                f"Use one of: {', '.join(self.SUPPORTED_CURRENCIES)}"
            )
        return code


def find_data_file():
    """Locate the Bank of Canada CSV in the same folder as this script.

    Falls back to any similarly named file, in case the download was saved
    as e.g. 'BankOfCanadaExchangeRate.2026 (2).csv' or '...Rates.2026.csv'.
    """
    default_path = SCRIPT_DIR / DEFAULT_FILE_NAME
    if default_path.exists():
        return default_path

    matches = sorted(SCRIPT_DIR.glob("BankOfCanadaExchangeRate*.csv"))
    if matches:
        return matches[0]

    raise FileNotFoundError(
        f"Could not find {DEFAULT_FILE_NAME} in {SCRIPT_DIR}. "
        "Place the Bank of Canada CSV next to this script."
    )


def main():
    """Prompt the user, run the conversion and print the formatted result."""
    rates = ExchangeRates(find_data_file())

    print("Currency Converter (USD <-> CAD)")
    print(f"Rate used: {rates}\n")

    # Inputs are assumed valid (per the assignment). '$' and ',' are
    # stripped so entries like "$100,000" are accepted as well as "100000".
    amount_text = input("Enter the amount to convert: ")
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()

    amount = Decimal(amount_text.replace("$", "").replace(",", "").strip())
    result = rates.convert(amount, from_currency, to_currency)

    print(f"\n{rates.format_amount(amount, from_currency)} = "
          f"{rates.format_amount(result, to_currency)}")


# Run main() only when the file is executed directly, not when it is
# imported (e.g. to reuse the ExchangeRates class in another script).
if __name__ == "__main__":
    main()
