#Capitulo 42: Como heredar propiedades _init_

class Usuarios():                                   #Clase padre

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Mostrar_Datos(self):
        print("El nombre de usuario es: " + self.nombre, " y tiene ", self.edad)

usuario1 = Usuarios("Ruben", 21)
usuario1.Mostrar_Datos()

class Usuarios_premium(Usuarios):                    #Clase hijo
    
    def _init_(self, nombre, edad, instagram):
        Usuarios.__init__(self, nombre, edad)
        self.instagram = instagram

    def Mostrar_Datos_Premium(self):
        print("El nombre de usuario es: " + self.nombre, " y tiene ", self.edad, " años. su Instagram es: ", self.instagram)

usuario2 = Usuarios_premium("Ruben Dios", 18, "ruben_tol")
usuario2.Mostrar_Datos_Premium()