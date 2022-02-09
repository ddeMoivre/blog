#   * Collect daily US Treasury yield data from FRED,
#     the Federal Reserve Economic Database, and stores them
#     in fred_data.csv”.

import pandas as pd
import pandas_datareader.data as web
import datetime

# Set start and end date for collection in YYYYMMDD (numeric) format
start = datetime.datetime(2011,10,15)
end = datetime.datetime(2021,10,15)

# Series name | Description
#
# DGS3MO      | 3-Month Treasury, constant maturity rate
# DGS1        | 1-Year Treasury, constant maturity rate
# DGS5        | 5-Year Treasury, constant maturity rate
# DGS10       | 10-Year Treasury, constant maturity rate
#
# DAAA        | Moody's Seasoned Aaa Corporate Bond Yield
# DBAA        | Moody's Seasoned Baa Corporate Bond Yield
#
# DCOILWTICO  | Crude Oil Prices: West Text Intermediate (WTI) - Cushing, Oklahoma

DGS3MO = web.DataReader("DGS3MO",'fred', start, end)
DGS1 = web.DataReader("DGS1",'fred', start, end)
DGS5 = web.DataReader("DGS5",'fred', start, end)
DGS10 = web.DataReader("DGS10",'fred', start, end)
DAAA = web.DataReader("DAAA",'fred', start, end)
DBAA = web.DataReader("DBAA",'fred', start, end)
DCOILWTICO = web.DataReader("DCOILWTICO",'fred', start, end)

# Each object is a 1-column matrix with time series data
# The column-name is the same as the object name

# Merge data series together
# Create data frame with all FRED series from 2011/10/15 on

fred = pd.concat([DGS3MO, DGS1, DGS5, DGS10, DAAA,
                    DBAA, DCOILWTICO], axis=1)




# Transform to data frame
fred = pd.DataFrame(fred)

# Save as csv file
fred.to_csv('fred_data.csv') 
