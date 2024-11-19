import random

# Generar un número aleatorio entre 1 y 10 (incluyendo ambos extremos)
numero_aleatorio = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", numero_aleatorio)

# Lista de elementos
colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja']

# Elegir un color aleatorio
color_aleatorio = random.choice(colores)
print("Color aleatorio elegido:", color_aleatorio)

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Mezclar la lista
random.shuffle(numeros)
print("Lista de números mezclada:", numeros)
