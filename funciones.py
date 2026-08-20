#función es un bloque de codigo que solo se ejecuta cuando lo llamamos permite organizar y modularizar rl codigo

def saludar(nombre, apellido=""): #Argumentos
    print("Hola", nombre, apellido)
    
# saludar("pedro", "Sanchez") #parametros
# saludar("Maria")

def sumar(a,b):
    return a + b

resultado = sumar(2,3)
print(resultado)

def funcion():
    pass

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a/b
resultado = multiplicar(7,4)
resultado = dividir(6,2)
resultado = resta(5,3)
print(resultado)