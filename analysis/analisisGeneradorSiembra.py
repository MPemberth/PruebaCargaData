import pandas as pd

from data.generators.generadorSiembra import generarDatosSiembra
from helpers.generarTabla import createTablaHTML

def construirDataFrameSiembra():
    datosSiembra=generarDatosSiembra()

    siembraDF=pd.DataFrame(datosSiembra)
    createTablaHTML(siembraDF,"analisisGeneradorSiembra")

    print(siembraDF)

construirDataFrameSiembra()