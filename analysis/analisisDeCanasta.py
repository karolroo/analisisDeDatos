#1. importar el paquete o paquetes con los que voy a analzar la informacion

import pandas as pd

def analizarCanastaBasica():

#2. Sin importar la fuente (sql, xls, JSON, csv...)
#Crear una tabla tabulada que se llama DATAFRAME
    tabla= pd.read_csv("./data/bdcanasta.csv")

   # print(tabla)
#3 Aplico filtros para limpiar o seleccionar datos
    
    #print(tabla.head(20)) #Primeros N registros
    #print(tabla.tail()) #Ultimos regsitros

    print(tabla.describe())