import pandas as pd

from influxdb import DataFrameClient

host = "localhost"
port = "8086"
user = "root"
password = "root"
dbname = "finetra"


def addToDB(df):
    print('in addToDB')



def connectTest():
    client = DataFrameClient(host, port, user, password, dbname)

