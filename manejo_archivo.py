# open(nombre, modo)
# R (read) Lectura
# w (write) Escritura
# x (Crea archivo nuevo)

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("Archivo no encontrado")

try:
    with open ("archivo.txt", "a") as f:
        f.write('/n')
        f.write("Hola munto desde el write en el with")
        with open("archivo.txt", "r", encoding="utf-8") as f:
            print(f.read())
except FileNotFoundError:
    print("Archivo no encontrado")
