#Capitulo 39: Que es un self?

class Usuarios():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Mostrar_Datos(self):
        print("El nombre de usuario es: " + self.nombre, self.edad)

usuario1 = Usuarios("Ruben", 25)
usuario1.Mostrar_Datos()

usuario1.edad = 21
usuario1.Mostrar_Datos()