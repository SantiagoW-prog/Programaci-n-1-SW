
def cargar_titulos(titulos, ejemplares):
    for i in range(len(titulos)):  
        if titulos[i] == "":      
            titulo = input("Ingrese título/s (o 'fin' para terminar): ")
            if titulo == "fin":    
                break
            cantidad = int(input("Ingrese cantidad de ejemplares: "))
            titulos[i] = titulo
            ejemplares[i] = cantidad


    
    
