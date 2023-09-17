#Capitulo 25: Multiples condiciones IF

print("Saludos, que desea comprar?\n\n" +
      "Items disponibles:\n\n" +
      "1-Espada nivel 1... $150\n" +
      "2-Espada nivel 2... $1200\n" + 
      "Escudos:\n\n" +
      "3-Escudo nivel 1... $100\n" +
      "4-Escudo nivel 2... $750\n")
comprar = []
dinero = 1500
espadaLV1 =150
espadaLV2 = 1200
escudoLV1 = 100
escudoLV2 = 750

if 0 in comprar or comprar ==[]:
    print("Escifica un numero entre el 1 y 4: ")
if 1 in comprar:
    dinero = dinero - espadaLV1
if 2 in comprar:
    dinero = dinero - espadaLV2
if 3 in comprar:
    dinero = dinero - escudoLV1
if 4 in comprar:
    dinero = dinero - escudoLV2
else:
    print("El numero no es valido!!")
if dinero < 0:
    print("¡No te llega el dinero para todo eso!")
if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan: $" + str(dinero) + " Moneras de oro.")
    print("Se añadio el/los objeto/s a tu inventario.")