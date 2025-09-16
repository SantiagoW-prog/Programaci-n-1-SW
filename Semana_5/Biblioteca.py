import funciones as fn

titulos = [""] * 20

ejemplares = [0] * 20

while True:
    print("--- MENÚ BIBLIOTECA ---")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (préstamo / devolución)")
    print("7. Salir")

    opcion = input("Elegi la opcion que quieras: ")

    if opcion == "1":
        fn.cargar_titulos(titulos, ejemplares)

    if opcion == "2":
        fn.mostrar_catalogo(titulos, ejemplares)
    
    if opcion == "3":
        fn.disponibilidad(titulos, ejemplares)
    
    if opcion == "4":
        fn.listar_agotados(titulos, ejemplares)