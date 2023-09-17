#Capitulo 33: Metodos con diccionarios

#teclados = {
teclado1 = {
    "Categoria": "Teclados", 
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99",
    "ID" : "001"
    },
teclado2 = {
    "Categoria": "Teclados", 
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }
#}
#print(len(teclado1) + len(teclado2))     #mostrar longitud de diccionario

teclado2.pop("Categoria")                #Eliminar elementos
teclado2.pop("Precio")
print(teclado2) 

del teclado1                             #Eliminar todo un diccionario o clave: teclado1["Categoria"]

#teclado1.clear()                          #Otra forma de vaciar un diccionario

#teclado1["Color"] = "Negro"                #Agregar elemento a diccionario

#tecladoCopia = teclado1.copy()             #Copiar un diccionario o tambien:  tecladoCopia = dic(teclado1)

#teclado3 = dict(categoria = "Teclado",             #Crear un nuevo diccionario
#               Modelo = "Razer Cynosa Chroma",
#               Precio = "59,99")

#teclado3 = ("categoria", "Modelo", "Precio")
#teclado3 = dict.fromkeys(teclado3, "vacio")

#vistaTeclado = teclado1.keys()                   #Imprimir las claves de diccionario

#teclado1.update({"Color" : "Negro"})              #Agregar nueva claves 

#if "ID" in teclado2:                               #Buscar elementos 
    #print("El producto tiene un ID especificado.")
#else:
    #print("El producto no tiene ID especificado. Por favor introduce un ID")

#print(teclados)