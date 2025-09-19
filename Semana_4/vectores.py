# Punto 1

vec_enteros = [0] * 5

for entero in range(len(vec_enteros)): 

   vec_enteros[entero] = int(input(f"Ingrese el entero {entero + 1}: "))


for entero in range(len(vec_enteros)):
    print(f"enteros: {entero + 1}: {vec_enteros[entero]}")



#Punto 2

vec_enteros1 = [0] * 10


for entero1 in range(len(vec_enteros1)):

    vec_enteros1[entero1] = int(input(f"Ingrese el entero {entero1 + 1}: "))

suma = 0

for entero1 in range(len(vec_enteros1)):
    suma += vec_enteros1[entero1]

print(f"La suma de los enteros es {suma}")





# Punto 3 

vec_float = [0] * 6

for float1 in range(len(vec_float)):
    vec_float[float1] = float(input(f"Ingrese el numero {float1 + 1}: "))

promedio = 0
suma = 0

for float in range(len(vec_float)):
    suma += vec_float[float1]
    promedio = suma / 6

print(f"El promedio es: {promedio}")




# Punto 4


enteros2 = [0] * 8  


for mayor in range(8):
    enteros2[mayor] = int(input(f"Ingrese el número {mayor+1}: "))


contador = 0

for mayor in range(8):
    if enteros2[mayor] > 100:
       contador += 1


print(f"Cantidad de números mayores a 100:{contador}")





# Punto 5

ent3 = [0] * 10

for i in range(10):
    ent3[i] = int(input(f"Ingrese el número {i+1}: "))

numero_buscado = int(input("Ingrese el número que desea buscar: "))

encontrado = False
for i in range(10):
    if ent3[i] == numero_buscado:
        print(f"El número {numero_buscado} se encuentra en la posición {i}")
        encontrado = True
        break  

if not encontrado:
    print(f"El número {numero_buscado} no se encuentra en el array.")






# Punto 6

numeros10 = [0] * 7

for i in range(7):
    numeros10[i] = int(input(f"Ingrese el número {i+1}: "))

mayor = numeros10[0]
posicion = 0

for i in range(1, 7):
    if numeros10[i] > mayor:
        mayor = numeros10[i]
        posicion = i

print(f"El valor más alto es {mayor} y se encuentra en la posición {posicion+1}")




#Punto 7


numeros = [0] * 6


for i in range(6):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))


print("El array invertido es:")

for i in range(5, -1, -1):  
    print(numeros[i])

#punto 8







#punto 9

numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))

for i in range(10):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print(f"El resultado es", numeros)