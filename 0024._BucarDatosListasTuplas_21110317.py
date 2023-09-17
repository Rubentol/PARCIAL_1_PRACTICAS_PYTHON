#Capitulo 24: Bucar datos en listas y tuplas 

colores = ('azul', 'blanco', 'negro', 'rojo', 'verde', 'rosa', 'amarillo', 'naranja')
entrada = input("Introduce el color que buscas:\n")
if entrada in colores[0]:
    print("El color azul esta admitido!!")
elif entrada in colores[1]:
    print("El color blanco esta admitido!!")
elif entrada in colores[2]:
    print("El color negro esta admitido!!")
elif entrada in colores[3]:
    print("El color rojo esta admitido!!")
elif entrada in colores[4]:
    print("El color verde esta admitido!!")
elif entrada in colores[5]:
    print("El color rosa esta admitido!!")
elif entrada in colores[6]:
    print("El color amarillo esta admitido!!")
elif entrada in colores[7]:
    print("El color naranja esta admitido!!")
else:
    print("El color no esta admitido!!")