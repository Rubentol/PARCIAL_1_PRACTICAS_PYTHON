#Capitulo 28: El bucle while con condiciones if

x = 0
while x < 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print("Se salto el valor: " + str(x) )
        continue
    if x == 15:
        print("Se rompe la ejecucion del bucle cuando el valor es " + str(x) + " en X...")
        break
    print(x)
