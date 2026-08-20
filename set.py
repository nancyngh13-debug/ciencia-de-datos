conjunto (set) coleción no ordenada

frutas = {"manzana", "banana", "cereza", "banana"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("manzana" in frutas)
print("pera" not in  frutas)
frutas.add("pera")
print(frutas)
#update
frutasTropicales = {"mango", "piña", "papaya"}#Agregar listas, tuplas, conjuntos  
frutas.update(frutasTropicales)
print(frutas)

frutas.remove("mango")
print(frutas)

frutas.discard("pera")
print(frutas)

frutas.pop()
print(frutas)

frutas.clear()
print(frutas)

a = {"a", "b", "c"}
b = {"c", "d", "e"}
#union  

c = a.union(b)
print(c)

i = a.intersection(b)
print(i)
diferencia = a.difference(b)
print(diferencia)


conjuntos =("Python", 156, True)
print(conjuntos)
print(type(conjuntos))

for item in conjuntos:
    print(item)
    