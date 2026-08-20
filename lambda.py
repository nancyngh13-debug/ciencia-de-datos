#lambda es una función pequeña y anonima que puede tener muchos argumentos para solo una expresión

#sintaxis lambda argumentos: expresion

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a + b
# print(x(2,3)) #5



#NANCY_ING SOFTWARE 18/08/2026
def mifuncion(n):
    return lambda a : a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)
quintuplicador = mifuncion(5)

print(duplicador(5))#10
print(triplicador(5))#15
print(quintuplicador(5))#25