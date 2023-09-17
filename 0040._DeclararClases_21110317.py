#Capitulo 40: Como declar clases vacias con pass y eliminar objetos

class nombreClase():
    pass

class Usuarios():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Mostrar_Datos(self):
        print("El nombre de usuario es: " + self.nombre, self.edad)

usuario1 = Usuarios("Ruben", 21)
usuario1.Mostrar_Datos()

del usuario1                       #Eliminar clase o para eliminar un obejto es: del usuario1.edad