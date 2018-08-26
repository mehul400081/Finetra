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
    # TODO: Add Tag
    # tags = { "AMFI": df[["AMFI"]]}
    # print('tags are: \n',tags)
    dbConnDF = DataFrameClient(host, port, user, password, dbName)
    dbConnDF.write_points(dataframe=df, measurement=tbName, field_columns = timeValues, database = dbName)




