#Capitulo 36: **kwargs-Diccionarios arbitrarios

def colores(color1, color2, color3, color4):
    print("Este es un color: " + color1 + ".")

colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")

def colores(**kwargs):
    print("Este es el color: " + kwargs["color1"] + ".")

colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")
print("\n")
def suma(x,y):
    return x + y

total = suma(10,10)
print("El resultado de la suma es: " + str(total))

def resta(x,y):
    return x - y

total = resta(10,10)
print("El resultado de la resta es: " + str(total))

def multi(x,y):
    return x * y

total = multi(10,10)
print("El resultado de la mulriplicacion es: " + str(total))

def division(x,y):
    return x / y

total = division(10,10)
print("El resultado de la division es: " + str(total))

def colores():
    pass

def colores1(color="rojo"):
    print("mi color favorito es el: " + color)
print("\n")
colores1("azul")
colores1()
colores1("verde")