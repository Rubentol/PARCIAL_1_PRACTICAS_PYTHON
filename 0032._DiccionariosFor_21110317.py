#Capitulo 32: Como usar diccionarios con el bucle for

teclado1 = {
    "Categoria": "Teclados", 
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
    }
teclado2 = {
    "Categoria": "Teclados", 
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }

for x in teclado1.values():
    print(x)
for x, y in teclado2.items():
    print(x,":", y)
print("\n---------------------------------------------------\n")
for x, y in teclado1.items():
    print(x,"=",y)