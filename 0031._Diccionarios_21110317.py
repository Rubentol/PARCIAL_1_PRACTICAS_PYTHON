#Capitulo 31: Que son los diccionarios de Python

teclado1 = {
    "Categoria": "Teclados", 
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "899,99"
    }
teclado2 = {
    "Categoria": "Teclados", 
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }
consulta = teclado1["Modelo"], teclado1["Precio"], teclado2["Modelo"], teclado2["Precio"]
print(consulta)

muestraTeclado = dict(teclado1) 
print(muestraTeclado)

consulta2 = "El modelo " + str(teclado2["Modelo"]) + " Cuesta: $" + str(teclado2["Precio"])
print(consulta2)