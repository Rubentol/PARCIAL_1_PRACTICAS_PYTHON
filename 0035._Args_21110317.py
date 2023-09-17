#Capitulo 35: Explicacion de *args con ejemplos

def alumnos(*args):
    print("El ultimo alumno es: " + args[3] + " y el primero es: " + args[0] + ".")

#alumnos("Andre", "Ruben", "Armando", "Pedro")

def alumnos_prof(profesor, sustituto, *args):
    print("Profesor: " + profesor)
    print("Sustituto: " + sustituto)
    for x in args:
        print("Alumno: " + x)

lista_alumno = ["Andres", "Ruben", "Armando", "Pedro"]
#alumnos_prof("Antonio", "Amador", *lista_alumno)

def colores(*args):
    print("El color " + args[1] + " es mi favorito. " + "El color " + args[0] + " tampoco esta mal.\n")

def suma(*args):
    res = args[0] + args[1] + args[2] + args[3] + args[4]
    print("El resultado es: ", res)

colores("rojo", "azul", "verde", "amarillo")
colores("lila", "negro", "rojo")
colores("rosa", "blanco")
colores("marron", "naranja")
suma(10,15,2001,6,12)
