import statsmodels.tsa.stattools as ts
from numpy import cumsum, log, polyfit, sqrt, std, subtract
import pandas

data = pandas.read_csv("C:\\Users\\sam\\Desktop\\NSEBANK.csv")


def hurst(ts):
    '''ts = ts if not isinstance(ts, pandas.Series) else ts.to_list()
    # """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0] * 2.0'''


    Hval="{:.1f}".format((hurst(data['Open'])))
    print(Hval)

if Hval > '0.5':
    print("Time series is Trending")
if Hval < '0.5':
    print("Time series is Mean Reversion")
if Hval == '0.5':
    print("Time series is Random Walk")
