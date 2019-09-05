# Algoritmos
Algoritmos desarrollados con python


1. Ejercicio 1: Hallar el siguiente numero a 40755 que sea triangular, pentagonal y hexagonal
2. Ejercicio 2: Hallar rutas posibles para cuadricula 20x20 


Dockerfile:
1. Para ejercicio #1 
COPY ./tripenhex.py /tripenhex.py
CMD ["python", "/tripenhex.py"]

2. Para ejercicio #2
COPY ./rutascuadriculadas.py /rutascuadriculadas.py
CMD ["python", "/rutascuadriculadas.py"] 


Comandos para ejecutar programa:
1. docker build -t algoritmo .
2. docker run algoritmo
