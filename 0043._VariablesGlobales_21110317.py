#Capitulo 43: Variables globales, locales y funciones anidadas

def funcion1():
    variable1 = "Variable dentro de la funcion."
    print(variable1)

#funcion1()

def funcion1():
    variable1 = "Variable dentro de la funcion1."
    print(variable1)
    def funcion2():
        variable1 = "He cambiado de funcion."
        print(variable1)
    funcion2()

#funcion1()

variable = "Variable Fuera de la funcion."

def funcion3():
    print(variable)

#funcion3()

num1 = 10
def globa():
    global num1
    num1 = 15

globa()
print(num1)
