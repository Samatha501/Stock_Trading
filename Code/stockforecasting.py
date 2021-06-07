import glob
import os.path
import statsmodels.tsa.stattools as ts
from numpy import log, polyfit, sqrt, std, subtract
import pandas as pd

df = pd.read_csv("C:\\Users\\sam\\Desktop\\NSEBANK.csv")
title1 = "File Name"
title2 = "Type of Timeseries"
title3 = "Reason"

print("%-15s %-28s %-15s" % (title1, title2, title3))

def hurst(ts):
    #sending Series as the ts argument. All you have to do is send a List not a Series
    ts = ts if not isinstance(ts, pd.Series) else ts.to_list()
    # """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0] * 2.0

files = glob.glob('C:\\Users\\sam\\Desktop\\d-kite\\d-kite\\*.csv')

for file in files:
    data = pd.read_csv(file)
    base = os.path.basename(file)
    name = os.path.splitext(base)[0]
    Hval = "{:.1f}".format((hurst(data['Open'])))


    if Hval > '0.5':
        print("%-15s %-28s %s" % (name, "Trending","Hurst Exponent value is > " +Hval))
    if Hval < '0.5':
        print("%-15s %-28s %s" % (name, "Mean Reversion","Hurst Exponent value is < " +Hval))
    if Hval == '0.5':
        print("%-15s %-28s %s" % (name, "Random Walk","Hurst Exponent value is = " +Hval))
