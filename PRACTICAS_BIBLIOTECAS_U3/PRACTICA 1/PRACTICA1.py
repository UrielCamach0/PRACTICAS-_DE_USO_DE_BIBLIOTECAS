import os

#obtener el directorio actual
directorio_actual = os.getcwd()
print("Directorio Actual:", directorio_actual)

#listar archivos y carpetas en el directorio actual
contenido = os.listdir('.')
print("El contenido del directorio actual: ", contenido)

#crear un nuevo directorio
nuevo_directorio="mi_carpeta_nueva"
os.mkdir(nuevo_directorio)

print("Directorio creado:", nuevo_directorio)