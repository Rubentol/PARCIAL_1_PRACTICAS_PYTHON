#Capitulo 26: tips para condicionales Python

x = 100
y = 200
z = 300
if x < y:
    print("X es menor que Y")
if x < y: print("X es menor que Y")
print("Se ejecuta If") if x > y else print("se ejecuta el else")
if x < y and z > y: 
    print("Se cumple las 2 condiciones!!")
else: 
    print("No se cumple alguna de las condiciones!!")
if x < y or z > y: print("Se cumple una de las condiciones!!")
else: print("No se cumple ninguna condicion!!")
if x < y:
    pass