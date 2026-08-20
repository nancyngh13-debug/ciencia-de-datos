# try:
#     print("intentamos algo")
# except:
#     print("captura error")
    
try:
    numero = 10/0
except ZeroDivisionError:
    print("captura error")
    
x = 1

try :
    print(x)
    
except NameError:
    print("Esta variable no ah sido definida")
finally:
    print("Esto sera ejecutado exitosamente")
    