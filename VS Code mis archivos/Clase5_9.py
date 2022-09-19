#def suma(x,y) :
    #resultado = x+y 
    #return resultado

#x = 2
#y = 4
#z = suma(x, y)
#print(z) 

#Ejemplo de la empresa
#def bienvenida(nombre, pais="Argentina") :
    #print("Damos la bienvenida a la empresa a " + nombre + "de" + pais)
    #print("Pedro") #Por ahora no funciono, veremos mañana

import math
def raiz_cuadrada(*args):
    for i in args:
        print("La raíz cuadrada de", i, "es:", math.sqrt(i))

raiz_cuadrada(1,2,3,4,5,6,7) 