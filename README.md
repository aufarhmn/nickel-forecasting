# Forecasting Nickel Prices

## Introduction
This repository contains the code and data for the forecasting of nickel prices. The data is consisted of nickel price and nickel production data. This repository using two forecasting methods, that is exponential smoothing and linear regression. 

## Data
The nickel price data is obtained from [Statista](https://www.statista.com/statistics/236578/iron-ore-prices-since-2003/). \
The nickel production data is obtained from [Statista](https://www.statista.com/statistics/260748/mine-production-of-nickel-since-2006/).

## File Directory
There are 3 main files in this repository:
| File | Description |
| --- | --- |
| Nickel-Price-Production.csv | The data file containing the nickel price and nickel production data
| 1-timeseries-manual.py | The code for the exponential smoothing method using manual calculation
| 1-timeseries.py | The code for the exponential smoothing method using pandas library
| 2-causal.py | The code for the linear regression method

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install pandas numpy matplotlib 
```

## Author
Aufa Nasywa Rahman - 21/475255/TK/52454

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.