import numpy as np # type: ignore

#crear un arreglo unidimensional
arreglo_1d=np.array([1,2,3,4,5])
print("Arreglo unidimensional", arreglo_1d)

#crear un arreglo bidimensional (matriz)
arreglo_2d=np.array([[1,2,3], [4,5,6]])
print("Arreglo bidimensional: ", arreglo_2d)

#crear dos arreglos
arreglo_a=np.array([1,2,3])
arreglo_b=np.array([4,5,6])

#suma de arreglos
suma=arreglo_a + arreglo_b
print("Suma de arreglos: ", suma)

#resta de arrgelos
resta=arreglo_a - arreglo_b
print("Resta de arreglos: ", resta)

#producto elemento a elemento
producto=arreglo_a * arreglo_b
print("Producto de arreglos: ", producto)