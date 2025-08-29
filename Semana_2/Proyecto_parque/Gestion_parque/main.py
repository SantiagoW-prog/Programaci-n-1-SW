import parque    


nombre_del_visitante = input("Ingrese su nombre: ")
parque.saludar(nombre_del_visitante)



print(" --Menú de Atracciones-- ")
parque.mostrar_atracciones()


visita_atraccion = int(input("¿Cuantos años tenes?"))
parque.puede_subir(visita_atraccion)


