#Hallar rutas posibles en una cuadricula m*n

"""
Analizando una matriz m*n se observa que cada ruta
tiene m+n pasos para completar la ruta
En cada ruta solo se pueden mover hacia abajo m pasos """

n=20
m=20

paso_total = m + n

"""A traves de la funcion recursiva para hallar el factorial determinamos
las combinaciones posibles de rutas (paso_total!/(m!*(n)!)) """

def factorial(f):
    if f == 1:
        return 1
    else:
        return f * factorial(f-1)

rutas = int((factorial(paso_total))/(factorial(m)*factorial(n)))
print(rutas)
