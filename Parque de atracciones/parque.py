nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cantidad = int(input("¿Cuántas atracciones desea usar? (máx. 3): "))

AptoCarrusel = False
LaCasaDelTerror = False
MontanaRusa = False

if edad < 6:
    AptoCarrusel = True
elif edad <= 12:
    LaCasaDelTerror = True
    AptoCarrusel = True
else:
    AptoCarrusel = True
    LaCasaDelTerror = True
    MontanaRusa = True

precios = {"Carrusel": 800, "Casa del Terror": 1200, "Montaña Rusa": 1500}

# Procesar atracciones
elegidas = ""
usadas = ""
total = 0

for i in range(cantidad):
    atr = input("Ingrese el nombre de la atracción: ")

elegidas += (" " if elegidas != "" else "") + atr


if atr == "Carrusel" and AptoCarrusel:
        usadas += ("Carrusel, " if usadas != "" else "Carrusel")
        total += precios["Carrusel"]
elif atr == "Casa del Terror" and LaCasaDelTerror:
        usadas += ("Casa del Terror, " if usadas != "" else "Casa del Terror")
        total += precios["Casa del Terror"]
elif atr == "Montaña Rusa" and MontanaRusa:
        usadas += ("Montaña Rusa, " if usadas != "" else "Montaña Rusa")
        total += precios["Montaña Rusa"]
else:
        print("No puede subir a", atr, "por su edad.")

# Resumen
print("\n--- Resumen ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Atracciones elegidas:", elegidas)
print("Atracciones que pudo usar:", usadas)
print("Total a pagar: $", total)

