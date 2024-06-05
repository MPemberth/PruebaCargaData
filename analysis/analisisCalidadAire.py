import pandas as pd

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import createTablaHTML

#1. Para analizar datos con Python debemos construir un dataframe

def construirDataFrameCalidadAire():
    datosCalidadAire=generarDatosCalidadAire()

    #Contruyo DataFrame
    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['Comuna', 'Total de población', 'Tamaño muestra', 'ICA', 'Fecha encuesta', 'Nombre', 'ID'])

    #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    print(calidadAireDF)
    #calidadAireDF.replace('-',pd.NA,inplace=True)
    #calidadAireDF.replace('sin',pd.NA,inplace=True)
    
    #2.Limpiando (elimando valores)
    calidadAireDF.replace('Sin',pd.NA,inplace=True)
    calidadAireDF.replace('-',pd.NA,inplace=True)
    calidadAireDF.dropna(inplace=True)

    #3. Filtrando datos para depurar la informacion

    #Contar datos
    #consultar datos especificos
    #filtroICAPositivo=calidadAireDF.query ("(ICA>=20) and (ICA<50)")
    
    #filtroICAModerado=calidadAireDF.query ("(ICA>=50) and (ICA<70)")

    filtroICAPeligroso=calidadAireDF.query ("(ICA>=70)").value_counts()

    #print(filtroICAPositivo)
    #print("\n")
    #print(filtroICAModerado)
    print("\n")
    print(filtroICAPeligroso)
    print("\n")
    
    
    #probando.... 
    print("\n")
    print(calidadAireDF)
    #createTablaHTML(calidadAireDF,"calidadAire")

construirDataFrameCalidadAire()