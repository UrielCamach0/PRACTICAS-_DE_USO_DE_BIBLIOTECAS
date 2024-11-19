import sys

#lista de argumentos de la línea de comandos
print(sys.argv)

#mostrar la version de Python
print("Versión de Python:", sys.version)

#mostrar informacion del sistema operativo
print("Sistema operativo:", sys.platform)

print("Este mensaje se muestra.")
sys.exit()  #salida del programa
print("Este mensaje no se mostrará.")