tupla1 =(1,2,3)
tupla2 = (4,5,6, 6)
tupla3 = tupla1 + tupla2
print(tupla3)

tupla = ("python", 5, True)
print(tupla * 2)

for item in tupla:
    print(item)

print("_______________________")

tuplaModificar = ("python", "Javascript", "Go")
listaComodin = list(tuplaModificar)
listaComodin.append("ReactJS")
tuplaModificar = tuple(listaComodin)
print(tuplaModificar)