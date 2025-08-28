
#PUNTO 1
def saludar(nombre):
    print("Bienvenido ", nombre)
nombre = input("¿Cual es tu nombre? ")
saludar(nombre)

#PUNTO 2
def operaciones(num1, num2):
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operaciones(num1, num2)

#PUNTO 3

def area_triangulo(base, altura)-> float:
    return (base * altura) / 2
base1 = float(input("Ingrese la base del triángulo: "))
altura1 = float(input("Ingrese la altura del triángulo: "))
    
area = area_triangulo(base1, altura1)
print(f"El area del triangulo es {area}")


#PUNTO 5

def es_par(numero):
    return numero % 2 == 0 

numero1= int(input("Ingrese un número: "))

if es_par(numero1):
    print(f"El número {numero1} es par.")
else:
    print(f"El número {numero1} es impar.")

#PUNTO 6
def convertir_minutos(minutos):
    horas = minutos // 60       
    minutos_sobra = minutos % 60  
    return horas, minutos_sobra

 
minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas, minutos_sobra = convertir_minutos(minutos_totales)
print(f"{minutos_totales} minutos son {horas} horas y {minutos_sobra} minutos.")

#PUNTO 7

def verificar_acceso(edad):
    return edad >= 18

edad1 = int(input("Ingrese su edad: "))

if verificar_acceso(edad1):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")