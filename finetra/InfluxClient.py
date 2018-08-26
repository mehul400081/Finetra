import pandas as pd

from influxdb import DataFrameClient

host = "localhost"
port = "8086"
user = "root"
password = "root"
dbName = "finetra"
tbName = "referenceData"


def connectTest(df):

    timeValues = df[['NAV']]
    timeValues.index = df[['DATE']]
    tags = {'AMFI': df[['AMFI']], 'ISIN': df[['ISIN']]}

    dbConnDF = DataFrameClient(host, port, user, password, dbName)
    dbConnDF.write_points(df, dbName, tbName, timeValues, tags)




