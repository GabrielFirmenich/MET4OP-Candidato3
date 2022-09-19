Lista1 = []
while len(Lista1) < 10:
    valor = int(input("Ingrese un número entero: "))
    Lista1.append(valor)

print(Lista1)
numeros_pares=0
numeros_impares=0
acumulado_de_pares=0
numeros_positivos=0
numeros_negativos=0
cant_multiplos_5 = 0

for valor in Lista1:
    if valor > 0:
        print("Este número es positivo: ", valor)
    elif valor < 0:
        print("Este número es negativo: ", valor)

for valor in Lista1:
    if valor%2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

for valor in Lista1:
    if valor%2 == 0:
        acumulado_de_pares = acumulado_de_pares + valor

for valor in Lista1:
    if valor < 0:
        numeros_negativos += 1
    else:
        numeros_positivos += 1

for valor in Lista1:
    if valor%5 == 0:
        cant_multiplos_5 +=1

print("Impares: ", numeros_impares)
print("Pares: ", numeros_pares)
print("Hay", numeros_positivos, "números positivos")
print("Hay", numeros_negativos, "números negativos")
print("El acumulado de pares es: ", acumulado_de_pares)
print("Llegando a su fin, esta es la cantidad de múltiplos de 5: ", cant_multiplos_5)



        
    



