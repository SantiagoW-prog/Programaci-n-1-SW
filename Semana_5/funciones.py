
def cargar_titulos(titulos, ejemplares):
    for i in range(len(titulos)):  
        if titulos[i] == "":      
            titulo = input("Ingrese título/s (o 'fin' para terminar): ")
            if titulo == "fin":    
                break
            cantidad = int(input("Ingrese cantidad de ejemplares: "))
            titulos[i] = titulo
            ejemplares[i] = cantidad

def mostrar_catalogo(titulos, ejemplares):
    print("+--- Catálogo completo ---")
    hay_titulos = False
    for i in range(len(titulos)):
        if titulos[i] != "":  
            print(f"{titulos[i]} hay {ejemplares[i]} copias")
            hay_titulos = True

    if not hay_titulos:
        print("El catálogo está vacío.")

def disponibilidad(titulos, ejemplares):
    titulo_buscar = input("Ingrese el título a consultar: ")
    encontrado = False
    for i in range(len(titulos)):
        if titulos[i] == titulo_buscar:
            print(f"{titulos[i]} hay {ejemplares[i]} copias")
            encontrado = True
            break  

    if not encontrado:
        print("Ese título no existe en el catálogo.")


def listar_agotados(titulos, ejemplares):
    print("\n--- Títulos agotados ---")
    hay_agotados = False
    for i in range(len(titulos)):
        if titulos[i] != "" and ejemplares[i] == 0:
            print(f"{titulos[i]}  AGOTADO")
            hay_agotados = True
    if not hay_agotados:
        print("No hay títulos agotados.")
    
    
