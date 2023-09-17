#Capitulo 14: Eliminar elementos con pop()
# variable = lista.pop(posicion)

colores = ["rojo", "azul", "verde", "amarillo", "marron", "lila", "negro", "rosa", "blanco", "naranja"]
eliminados = colores.pop(1) + " " + colores.pop(-2)
print(colores)
print("Los Elementos eliminados son: ", eliminados.title())