#print("Hola Mundo!") #Ejercicio1

#print("Ingrese su nombre:") #Ejercico2
#x = input()
#print("Hola..." + x)

#h_m = "Hola Mundo!" #Ejercico3
#print(h_m)

# x = input("Ingresa tu nombre pedazo de trolo: ") #Ejercico4
# y = int(input("Ahora ingresa un nùmero: "))
# print(x*y)

#mi_nombre = "Gabriel" #EJERCICO (5)
#print(mi_nombre)
#print(id(mi_nombre))
#print(mi_nombre.upper())

#operacion_aritmetica = ((3+2)%(2*5))**2 #EJERCICIO (6)
#float(operacion_aritmetica)
#print(id(operacion_aritmetica))
#print(type(operacion_aritmetica))
#print(operacion_aritmetica)

#x = input("¿Cómo es tu nombre?: " ) #Ejercicio (7)
#print("NOMBRE : " + x.upper())
#print("´n´ son la cantidad de letras: ") 
#print(len(x))

# print("Bienvenido a la empresa ´Hijos d euna buena puta´, para saber su sueldo siga las instrucciones: ")
# x = float(input("Ingrese cuantas horas trabaja por mes: ")) #EJERCICIO (9)
# y = float(input("¿Cuanto vale su hora de trabajo: "))
# print("Su salario mensual es de: ")
# print(x*y)

# EJERCICIO (10)
#print("Bienvenido al Vivero ´Flor de Poronga´, por favor indiquenos su pedido: ")
#monstera_peso = 1.5
#suculenta_peso = 0.300
#monstera_pedido = int(input("Introduzca cuantas Monsteras quiere: "))
#suculenta_pedido = int(input("Instroduzca cuantas suculentas quiere: "))
#peso_total = (monstera_pedido*monstera_peso)+(suculenta_pedido*suculenta_peso)
#print("La totalidad del peso en KG de su pedido será: ")
#print(peso_total)

#EJERCICIO (11)
#lista=[]
#Numero1 = int(input("Introduzca el primer numero que quiera:" ))
#Numero2 = int(input("Introduzca el segundo numero que quiera: "))
#Numero3 = int(input("Introduzca el tercer numero que quiera: "))
#lista.append(Numero1)
#lista.append(Numero2)
#lista.append(Numero3)
#print(lista)
#suma_numeros = Numero1 + Numero2 + Numero3
#producto_numeros = Numero1*Numero2*Numero3
#print("Suma de los elemntos: ")
#print(suma_numeros)
#print("El producto de los números es: ")
#print(producto_numeros)

#Ejercicio (12)
# candidatos = ["De Gasperini", "Nenni", "Brosio", "Giannini", "Pacciardi"]
# print(candidatos[0])
# print(candidatos[1])
# print(candidatos[4])

#EJERCICIO (13)
#anio = [1990, 1991, 1992, 1993, 1994, 1994, 1996, 1997, 1998, 1999]
#porcentajes = [2314, 84, 17.5, 7.4, 3.9, 1.6, 0.1, 0.3, 0.7, -1.2]
#resultados = dict(zip(anio, porcentajes))
#print(resultados)

#EJERCICIO (14)
# DNI = [41454623, 42454623, 43454623, 44454623, 45454623]
# nombres = ["Gabriel", "Gallego", "Micho", "Tito", "Negro"]
#identidad = dict(zip(DNI, nombres)) #Crear el Diccionario
# print(identidad.keys()) #Es importante escribir "keys", si usas "DNI" no lo printea
# print(identidad.values())
# print(identidad)

#EJERCICIO (15)

#distrito = ["Caba", "Pba", "Catamarca", "Cba"]
#cant_poblacion = [289151, 15625084, 367828, 3308867]
#poblacion = dict(zip(distrito, cant_poblacion))
#print(poblacion)
#del poblacion["Caba"]
#print(poblacion.items())
#poblacion["Pba"] = 12660320
#poblacion.update({"Corrientes": 992525})
#print(poblacion.items()) #Funcionaron las 3 consignas

#EJERCICIO (16)
#%%
Candidatos = {
  "CandidatoA" : {
    "nombre" : "Tony",
    "apellido": "Blair",
    "anio" : 1953
  },
  "CandidatoB" : {
    "nombre" : "William",
    "apellido": "Hague",
    "anio" : 1961
  },
  "CandidatoC" : {
    "nombre" : "Charles",
    "apellido": "Kennedy",
    "anio" : 1959
  }
}
print(Candidatos) 
print(Candidatos["CandidatoA"]["nombre"])
print(Candidatos["CandidatoB"]["anio"])
print(Candidatos["CandidatoC"]["apellido"])
print(Candidatos["CandidatoA"]["anio"])
if "CandidatoD" in Candidatos: 
    print("CandidatoD fue encontrado en el diccionario")
else: 
    print("CandidatoD no existe")
print(Candidatos["CandidatoD"]["nombre"])











# %%
