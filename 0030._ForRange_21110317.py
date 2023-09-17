#Capitulo 30: El bucle for con range()

for x in range(7,700,100):
    print(x)
 
print("\nLista de numeros:\n")
numeros = [2,4,8,16,32,64,128]
for x in range(len(numeros)):
    print("Numero de operacion -> ", x, "Multiplicado: -> ", numeros[x], "Resultado: -> ", numeros[x]*numeros[x], "\n")

for x in range(10):
    print(x)
else: 
    print("Se rompe el bucle!!\n")
         
num1 = ["1", "2", "3", "4", "5"]
num2 = "0"
for x in num1:
    for y in num2:
        print(x + y)