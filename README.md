# FINE3300-2026-A1
**FINE 3300 Assignment 1 – Python Currency Exchange Rate Calculator** 

## Project Description 

This project creates a Python-based currency exchange calculator that converts between Canadian dollars (CAD) and US dollars (USD) using annual exchange rate data provided by the Bank of Canada.
There are two parts to this assignment. Part one consists of an independently developed Python program, and part two is an AI-generated version using Claude Opus 5.5 (extra mode).

## PART ONE - Exchange Rate Calculator

This program was created manually using Python programming concepts covered in our FINE 3300 class. Per class instructions, AI use was not permitted for part one. Therefore, AI was not used for any of the code in ExchangeRates.py.

The program uses an ExchangeRates class to:
- Read the USD/CAD exchange rate from the final row of the provided CSV file (BankOfCanadaExchangeRate.2026.csv).
- Convert between USD and CAD using the appropriate exchange rate.
- Prompt users to enter an amount, the original currency (from), and the desired currency (to).
- Display the converted amount with dollar signs, currency identifiers, and two decimal places. 

The program uses csv.DictReader to read the exchange rate data, float for numerical calculations, and if and elif statements to determine the direction of conversion.

## PART TWO - AI-Generated Exchange Rate Calculator 

The second program ExchangeRatesAI.py, was generated using Claude Opus by Anthropic.

The AI-generated program performs the same currency conversions but incorporates additional programming techniques, including: 
- The decimal library for precise financial calculations.
- A dictionary that stores currency values in CAD to simplify conversions.
- Additional methods to organize the program and improve code reusability.
- Currency input validation and file-handling features. 

Both programs use the same Bank of Canada exchange rate data and produce identical results for the two required conversion tests.


## HOW TO RUN THE PROGRAMS

### Requirements:
- Python 3 installed on your computer.
- Visual Studio Code is recommended for opening, editing, and running the programs.
- No additional third-party Python packages are required.

### Instructions:
 1. Download or clone the repository from GitHub and open the project folder in Visual Studio Code.
 2. Make sure that ExchangeRates.py, ExchangeRatesAI.py, and BankOfCanadaExchangeRate.2026.csv are in the same project folder.
 3. Open the integrated terminal in VS Code by selecting Terminal, then New Terminal.
 4. Make sure the terminal is in the project directory, then run either program using one of the following commands: 

 **Part 1 – Original Program**

```bash
python3 ExchangeRates.py
```

**Part 2 – AI-Generated Program**

```bash
python3 ExchangeRatesAI.py
```
 5. Enter the amount to convert, followed by the original currency (USD or CAD) and the desired currency (USD or CAD).
 6. The program will display the converted amount in the terminal.

## TEST RESULTS 

Both programs were tested using the final exchange rate provided in the CSV file.

Exchange Rate: 1 USD = 1.3978 CAD

| Conversion | Result |
| --- | --- |
|$100,000 USD to CAD | $139,780.00 CAD 
|$100,000 CAD to USD | $71,540.99 USD

Both programs successfully performed the conversions and produced the matching results. 

## DATA SOURCE

Bank of Canada. Annual exchange rate data, provided through FINE 3300 course materials. 

**Data File:** `BankOfCanadaExchangeRate.2026.csv`


    