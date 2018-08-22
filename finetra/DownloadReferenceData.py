from finetra.MFReference import Fund
from finetra.InfluxClient import connectTest
import pandas as pd
import requests

url = "https://www.amfiindia.com/spages/NAVAll.txt"
filePath = "/home/mehul/PycharmProjects/Finetra/nse.txt"


def downloadFile():
    data = requests.get(url)

    with open(filePath, "w") as f:
        f.write(data.text)


def processFile():
    i = 0
    df = pd.DataFrame()
    with open(filePath) as f:
        for line in f:
            i = i + 1
            #   ignore first line
            if i == 1:
                print('breaking on first header')
                continue
            #     select only semicolon seperated line
            if line.__contains__(";"):
                print('processing line', line , 'counter is ', i)
                line = line.rstrip('\n')
                df = df.append([line.split(";")])
                # if i >= 20:
                #     print('breaking on >= 20')
                #     break
                print('hello= ',df)
                connectTest(df)





def main():
    # downloadFile()
    processFile()


main()
