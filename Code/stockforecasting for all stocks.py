import os
from os.path import basename

from hurst import compute_Hc
import glob
import pandas

files = glob.glob('C:\\Users\\sam\\Desktop\\d-kite\3++\d-kite\\*.csv')

title0 = "File Name"
title2 = "Type of Time series"
title3 = "Reason"
print("%-15s %-15s %15s" % (title0, title2, title3))

for file in files:
    data = pandas.read_csv(file)
    name = os.path.splitext(basename(file))[0]
    colName = data["Price"]
    H, c, val = compute_Hc(colName)
    H = round(H, 1)

    if H > 0.5:
        print("%-15s %-28s %s" % (name, "Trending", "Hurst exponent value is > 0.5"))
    if H < 0.5:
        print("%-15s %-28s %s" % (name, "Mean Reversion", "Hurst exponent value is < 0.5"))
    if H == 0.5:
        print("%-15s %-28s %s" % (name, "Random Walk", "Hurst exponent value is = 0.5"))
