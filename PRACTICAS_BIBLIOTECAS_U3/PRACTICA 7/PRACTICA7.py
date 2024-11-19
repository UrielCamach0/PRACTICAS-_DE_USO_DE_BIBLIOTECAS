import pandas 

# Crear un dataframe a traves de un diccionario
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Maria'],  
    'Edad': [23, 25, 22, 24],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(datos)

# Mostrar el dataframe
print(df)

# Describir las estadisticas basicas del dataframe
print(df.describe())

# Informacion general del dataframe
print(df.info())
