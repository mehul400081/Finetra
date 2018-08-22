import pandas as pd

from influxdb import DataFrameClient

host = "localhost"
port = "8086"
user = "root"
password = "root"
dbName = "finetra"
tbName = "referenceData"


def connectTest(df):

    timeValues = df[ ['col3'] ]
    timeValues.index = df[ ['col5'] ]
    tags = {'col0': df[['col0']], 'col1': df[['col1']]}

    dbConnDF = DataFrameClient(host, port, user, password, dbName)
    dbConnDF.write_points(dbName, tbName, timeValues, tags=tags)




