import funciones as fn


while True:
    print("----Menu Princiapal----")
    print("1. Registrar turno")
    print("2. Calcular pago")
    print("3. Mostrar mensaje de agradecimiento")
    print("4. Salida")

    opcion = input(("Elegir opcion: "))

    if opcion == "1":
        nombre, turno = fn.pedir_turno()
        print(fn.registrar_turno(nombre, turno))
    elif opcion == "2":
        horas, turno = fn.pedir_pago()
        print(fn.calcular_pago(horas, turno))
    elif opcion == "3":
        fn.mensaje_agradecimiento()
    elif opcion == "4":
        print("Nos vemos")
        break
    else:
        print("Opción inválida, ingresar de nuevo: ")
