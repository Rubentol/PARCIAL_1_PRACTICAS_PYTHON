#Capitulo 34: Crear y llamar funciones en Python

def sadulo():
    print("Bienvenido a programacion")
#sadulo()

#Funciones con argumentos 
#print("La familia Simpson\n")

def familia(nombre, parent):
    print(nombre + " Simson " + parent)

#amilia("Homer", "Padre")
#familia("Marge", "Madre")
#familia("Lisa", "Hija")
#familia("Bart", "Hijo")
#familia("Maggie", "Hija")

def suma(num1, num2):
    res = num1 + num2
    print("El resultado de la suma es: " + str(res))

suma(10, 20)
suma(20, 30)
suma(50000, 7000)