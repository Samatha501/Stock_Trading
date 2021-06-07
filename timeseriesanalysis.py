# Import the Time Series library
import pandas as pd
import statsmodels.tsa.stattools as ts
import pandas as pd
import matplotlib.pyplot as plt
# Import Datetime and the Pandas DataReader
from datetime import datetime
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn


df = pd.read_csv("C:\\Users\\sam\\Desktop\\NSEBANK.csv")

# Output the results of the Augmented Dickey-Fuller test for Google
# with a lag order value of 1
sam=ts.adfuller(df['Price'], 1)
print(sam)

def hurst(ts):
    """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    ts = ts if not isinstance(ts, pd.Series) else ts.to_list()
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0]*2.0

# Create a Gometric Brownian Motion, Mean-Reverting and Trending Series
gbm = log(cumsum(randn(100000))+1000)
mr = log(randn(100000)+1000)
tr = log(cumsum(randn(100000)+1)+1000)

# Output the Hurst Exponent for each of the above series
# and the price of Google (the Adjusted Close price) for
# the ADF test given above in the article
print("Hurst(GBM):   %s" % hurst(gbm))
print("Hurst(MR):    %s" % hurst(mr))
print("Hurst(TR):    %s" % hurst(tr))

# Assuming you have run the above code to obtain 'goog'!
print("Hurst(NSEBANK):  %s" % hurst(df['Price']))
