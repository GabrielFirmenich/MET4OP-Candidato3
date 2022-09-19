#Estamos viendo variables LOCALES y GLOBALES
tres = 3

#def multiplico_por_tres(x): #Acá nunca estuvo definida la variable "tres", ya estaba definida globalmente
    #resultado = x*tres
    #return resultado

#multiplico_por_tres(5)
#print(multiplico_por_tres(5))

#def incremento(n):
    #print(["fn_1", n, id(n)])
    #n += 1
    #print()

#def asignar_valor(n, v):
    #n = v #Acá solo se igualan n y v adentro de la funcion de forma local
    #print(n, id(n), v, id(v)) #Este es el 2do print que sale en consolo

#L1 = [1, 2, 3]
#L2 = [4, 5, 6]
#print(L1, id(L1), L2, id(L2))

#asignar_valor(L1, L2)
#print(L1, id(L1), L2, id(L2))

#def asignar_valor(n, v):
    #n[:] = v[:] #La funcion hace una copia mediante slicing
    #print(n, id(n), v, id(v)) #Este es el 2do print que sale en consola

#L1 = [1, 2, 3]
#L2 = [4, 5, 6]
#print(L1, id(L1), L2, id(L2)) #Termina cambiando el contenido, pero no el id()

#asignar_valor(L1, L2) #El slicing le cambia el contenido
#print(L1, id(L1), L2, id(L2))

impar = lambda numero: numero%2 != 0 #Vemos lo interesante de lambda, es como un "if" en una linea de codigo
print(impar(3))
print(impar(14))

#valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#impar = list(filter(lambda: ))