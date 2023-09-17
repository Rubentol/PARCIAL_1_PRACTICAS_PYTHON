#Capitulo 23: El condicional If elif else e input
edad = int(input('Cual es tu edad?\n'))

if edad <= 0:
    print("Nadie puede tener esa edad!!!")
elif edad >= 1 and edad < 18:
    print("Eres menor de edad!!!")
elif edad >= 18 and edad <= 45:
    print("Ponte a jalor PA")
elif edad >= 45 and edad <= 100:
    print("Eres mayor de edad!!!")
elif edad >= 100 and edad <= 120:
    print("Como te gusta sufrir!!!")
else:
    print("Edad no valida")