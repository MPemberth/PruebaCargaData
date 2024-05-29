#funcion generica para convertir un dataFrame en HTML

def createTablaHTML(dataFrame,nombreTabla):

    #convertiumos el el df en html
    archivoHTML=dataFrame.to_html()

    #abrimos un archivo html en una ruta especifica
    archivo=open(f"./tables/{nombreTabla}.html","w")

    #escribimos la informacion en el archivo
    archivo.write(
        ''' 
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
        ''')
    archivo.write(archivoHTML)
    archivo.write(
        '''
        </body>
        </html>
        '''
    )
    archivo.close()  

