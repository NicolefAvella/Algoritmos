# Algoritmos
Algoritmos desarrollados con python


1. Hallar el siguiente numero a 40755 que sea triangular, pentagonal y hexagonal
2. Hallar rutas posibles para cuadricula 20x20 
3. Hallar la probabilidad de tener covid19 con sintomas severos (estadisticas 01/06/2020 Colombia)

Dockerfile:
1. Para ejercicio #1 
COPY ./tripenhex.py /tripenhex.py
CMD ["python", "/tripenhex.py"]

2. Para ejercicio #2
COPY ./rutascuadriculadas.py /rutascuadriculadas.py
CMD ["python", "/rutascuadriculadas.py"] 

3. Para ejercicio #3
COPY ./covid19.py /covid19.py
CMD ["python", "/covid19.py"] 

Comandos para ejecutar programa:
1. docker build -t algoritmo .
2. docker run algoritmo
