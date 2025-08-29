def saludar(nombre_del_visitante):
    print(f"Hola {nombre_del_visitante}, bienvenido al parque de atracciones!")

def mostrar_atracciones():
    print("1.Montaña Rusa")
    print("2.Casa del Terror")
    print("3.Carrusel")

def puede_subir(edad):
   if edad < 6 :
    print("Solo podes subir al Carrusel.")
   elif edad < 12:
    print("No podes subir a la Montaña Rusa, pero podes usar la Casa del Terror y el Carrusel.")
   else:
      print("Podes acceder a todas las atracciones (Montaña Rusa, Casa del Terror y Carrusel).")




