"""
Quick script to calculate allocation amounts in $ and shares to "Lily's Forever Portfolio".
See Composer Trade breakdown here: https://app.composer.trade/symphony/Vqo3Taxh3mEwpYjIEX95/details

Usage:
```
python3 calc_allocations_to_lilys_forever_portfolio.py 10000
```

Note: This is intended to be rebalanced yearly
"""


import sys
from pprint import pprint
import yfinance as yf

# Check if the command line argument for amount_to_allocate is provided
if len(sys.argv) < 2:
    print("Please provide the amount_to_allocate as a command line argument.")
    sys.exit(1)

# Retrieve the amount_to_allocate from the command line argument
amount_to_allocate = float(sys.argv[1])

xlp_weight = 16.67
xlv_weight = 25
xlk_weight = 25
tlt_weight = 16.67
gldm_weight = 16.66

# Fetch the latest share prices
xlp_ticker = yf.Ticker("XLP")
xlp_latest_price = xlp_ticker.history(period="1d").iloc[-1]["Close"]
# print('xlp_latest_price', xlp_latest_price)

xlv_ticker = yf.Ticker("XLV")
xlv_latest_price = xlv_ticker.history(period="1d").iloc[-1]["Close"]

xlk_ticker = yf.Ticker("XLK")
xlk_latest_price = xlk_ticker.history(period="1d").iloc[-1]["Close"]

tlt_ticker = yf.Ticker("TLT")
tlt_latest_price = tlt_ticker.history(period="1d").iloc[-1]["Close"]

gldm_ticker = yf.Ticker("GLDM")
gldm_latest_price = gldm_ticker.history(period="1d").iloc[-1]["Close"]

# Calculate the number of shares for each asset
amounts_to_allocate = {
    "XLP": {
        "latest price": xlp_latest_price,
        "dollars": amount_to_allocate * xlp_weight / 100,
        "shares": (amount_to_allocate * xlp_weight / 100) / xlp_latest_price,
    },
    "XLV": {
        "latest price": xlv_latest_price,
        "dollars": amount_to_allocate * xlv_weight / 100,
        "shares": (amount_to_allocate * xlv_weight / 100) / xlv_latest_price,
    },
    "XLK": {
        "latest price": xlk_latest_price,
        "dollars": amount_to_allocate * xlk_weight / 100,
        "shares": (amount_to_allocate * xlk_weight / 100) / xlk_latest_price,
    },
    "TLT": {
        "latest price": tlt_latest_price,
        "dollars": amount_to_allocate * tlt_weight / 100,
        "shares": (amount_to_allocate * tlt_weight / 100) / tlt_latest_price,
    },
    "GLDM": {
        "latest price": gldm_latest_price,
        "dollars": amount_to_allocate * gldm_weight / 100,
        "shares": (amount_to_allocate * gldm_weight / 100) / gldm_latest_price,
    },
}

pprint(amounts_to_allocate)
