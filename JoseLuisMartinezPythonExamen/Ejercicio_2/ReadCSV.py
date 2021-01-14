import pandas as pd
import csv
import json

# Para este ejercicio se creo un entorno virtual con la libreria Pandas instalada y el uso de la libreria json para mostrar una mejor presentacion del diccionario


class ReadCSV():
    def __init__(self):
        pass
    
    def leeCSV(self, filename="cotizacion.csv"):
        self.filename = filename

        #Convirtiendo CSV a diccionario
        cotizaciones = pd.read_csv(filename)
        diccionarioCotizaciones = cotizaciones.to_dict('records')

        #Formateando Diccionario, solo visual
        json_formatted_dic_cotizaciones = json.dumps(diccionarioCotizaciones, indent=2)

        #Imprimiendo diccionario formateado
        print("**********CSV Convertido a Diccionario**************")
        print(json_formatted_dic_cotizaciones)

        self.convierteDiccionarioCSV(diccionarioCotizaciones)

    def convierteDiccionarioCSV(self, diccionario):
        self.diccionario = diccionario

        with open('cotizacionConMedia.csv', 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['Nombre', 'Máximo', 'Mínimo', 'Media']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for registro in diccionario:
                media = ((registro['Máximo'] + registro['Mínimo'])/ 2)
                writer.writerow({'Nombre': registro['Nombre'], 'Máximo': registro['Máximo'], 'Mínimo': registro['Mínimo'], 'Media': str("{0:.2f}".format(media))})



LeerCSV = ReadCSV().leeCSV("cotizacion.csv")