#Realizar un pequeno sistema de gestion en consola para que una 
#concecionaria pueda cargar ventas, la misma se detiene se ingresa 
# 0. El programa debe informar al finaliar:
#        1. La venta mayor
#        2. La venta menor
#        3. Cantidades de ventas realizadas
#        4. El total de ventas

#Inicializacion de variables
Total_ventas = 0 #acumulador (incrementar por montos de venta)
cantidad_ventas = 0 #contador (inrementar de a uno)
venta_mayor = None #Se va a guardar la venta de mayor monto
venta_menor = None #Se va a guardar la venta de menor monto

while True:
    #(ENTRADA) Ingreso de ventas
    venta = float(input("Ingresar venta (Para finalizar ingresar 0): "))
    #corte de ciclo
    if venta == 0:
        break

    #Procesos. Acumulamos ventas y contamos
    Total_ventas += venta
    cantidad_ventas += 1

    #Proceso. Buscamos mayor y menor

    if cantidad_ventas == 1: # Condicionala que inicia
        venta_mayor = venta
        venta_menor = venta
    else:
        # condicional interno que compara mayores
        if venta > venta_mayor:
            venta_mayor = venta
        # condicional interno que compara menores
        if venta < venta_menor:
            venta_menor = venta
    
#(PROCESO)calculamos promedio de ventas 

promedio_ventas = Total_ventas / cantidad_ventas

# (SALIDA) Se muestran los valores
print(f"Total de ventas realizadas {cantidad_ventas} con un monto total de:  {Total_ventas}")

if cantidad_ventas > 0:
    print(f"Venta mayor: {venta_mayor}")
    print(f"Venta menor: {venta_menor}")
    print(f"El promedio de ventas es: {promedio_ventas}")
else:
    print("No se realizaron ventas mayores o menores...")


        