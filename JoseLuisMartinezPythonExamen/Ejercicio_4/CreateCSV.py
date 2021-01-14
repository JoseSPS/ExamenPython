import pandas as pd
import csv
from datetime import date

class ReadCSV():
    def __init__(self):
        pass
    
    def readCSV(self, filename="VectorAnalitico24H.csv"):
        self.filename = filename

        #Convirtiendo CSV a diccionario
        new_prices_pip = pd.read_csv(filename, encoding ='latin1')
        new_prices_pip_dict = new_prices_pip.to_dict('records')

        self.convertDicCSV(new_prices_pip_dict)

    def convertDicCSV(self, dic):
        self.dic = dic

        #Obtener Fecha para escribir titulo de archivo CSV
        today = date.today()
        year = today.year
        month = today.month
        day = today.day


        with open('Prices_PIP_%s%s%s_1.csv' %(year, month, day), 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['TICKER', 'PRECIO', 'MONEDA', 'VAR']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for new_value in dic:
                if (new_value['TIPO VALOR'] == 'FA' or new_value['TIPO VALOR'] == 'FB' or new_value['TIPO VALOR'] == 'FC' or new_value['TIPO VALOR'] == 'FI') and (new_value['SECTOR'] == 'DERIVADOS') and (int(new_value['FECHA EMISION'][-4:]) >= 2020):
                    writer.writerow({'TICKER': new_value['TIPO VALOR'] + '_' + new_value['EMISORA'] + '_' + new_value['SERIE'], 'PRECIO': new_value['PRECIO LIMPIO'], 'MONEDA': new_value['MONEDA EMISION'], 'VAR': new_value['VAR']})



LeerCSV = ReadCSV().readCSV("VectorAnalitico24H.csv")