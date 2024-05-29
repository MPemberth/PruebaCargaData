import pandas as pd

from data.generators.generadorDisposicionResiduos import generarDatosDisposicionResiduos
from helpers.generarTabla import createTablaHTML

def construirDataFrameDisposicionResiduos():
    datosDisposicionResiduos=generarDatosDisposicionResiduos()

    disposicionResiduosDF=pd.DataFrame(datosDisposicionResiduos, columns=['Comuna', 'Total de población', 'Tamaño muestra','Fecha encuesta', 'Nombre', 'ID', 'Clasificación', 'Aprovechamiento'])

    print(disposicionResiduosDF)
    createTablaHTML(disposicionResiduosDF,"analisisDisposicionResiduos")

construirDataFrameDisposicionResiduos()

#Comuna
#TotalPoblación
#TamanoMuestra
#FechaEncuesta
#Nombre
#ID
#Clasificación
#Aprovechamiento
