#Capitulo 41: Que es una herencia de clases?

class Usuarios():                                   #Clase padre

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Mostrar_Datos(self):
        print("El nombre de usuario es: " + self.nombre, " y tiene ", self.edad)

usuario1 = Usuarios("Ruben", 21)
usuario1.Mostrar_Datos()

class Usuarios_premium(Usuarios):                    #Clase hijo
    pass

usuario2 = Usuarios_premium("Ruben dios", 22)
usuario2.Mostrar_Datos()