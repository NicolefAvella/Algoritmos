#Calcular el siguiente numero de 40755 que es Triangular pentagonal y hexagonal

#Se importa del modulo math la raiz cuadrada para utilizar en la funcion hex_y_pen
from math import sqrt

""" Se utiliza la formula sqrt((24x)+1)+1)/6) para determinar si el numero es pentagonal
Si cumple la condicion se determina si este mismo numero es hexagonal sqrt((8x)+1)+1)/4) P
ara cumplir la condicion el residuo (%) debe ser igual a 0 """

def hex_y_pen(x):
	if (sqrt((24*x)+1)+1)%6 == 0:
		if (sqrt((8*x)+1)+1)%4 == 0:
			return (True)

""" Matematicamente todo numero hexagonal es un numero triangular De la ecuacion para numeros
triangulares se comienza a evaluar el resultado del n-esimo termino. El cual se evalua si cumple
la condicion de la funcion hex_y_pen
Si cumple, el ciclo while se rompera porque la bandera b sera 1
Si no cumple tn incrementara y el ciclo continua """

b=0
tn=286 #Se va a encontra el siguiente numero a 40755, tn=285

while b == 0:
	n = (tn*((tn+1)/2))
	if hex_y_pen(n) == True:
		pn= int((sqrt((24*n)+1)+1)/6)
		hn= int((sqrt((8*n)+1)+1)/4)
		print('tn:' + str(tn) + ' pn:' +str(pn) + ' hn:' + str(hn))
		print('El proximo numero es:' + str(int((n))))
		b=1
	else:
		tn += 1
