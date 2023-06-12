# Portfolio Allocation Script
This script calculates the allocation of a given amount to the assets and weightings defined in "Lily's Forever Portfolio".

It fetches the latest share prices of the assets using the Yahoo Finance API and calculate allocation in terms of share counts based on the previous market close and USD.

## Installation

```
pip install yfinance
```

## Usage
```
python calc_allocations_to_lilys_forever_portfolio.py 10000
```

Replace `10000` with the desired amount to allocate.

