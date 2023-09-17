#Capitulo 38: El metodo _init_de Python

class Usuarios():

    def __init__(self, nombre, pin):
        self.nombre = nombre
        self.pin = pin

    def saludo(self):
        print("Saludos " + self.nombre + ". Iniciaste sesion correctamente.")

    def despedida(self):
        print(self.nombre + ", cerraste la seccion.")

usuario1 = Usuarios("Ruben", "1234")
usuario2 = Usuarios("Nicolle", "1301")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()