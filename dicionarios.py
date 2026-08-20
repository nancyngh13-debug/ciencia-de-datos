# coleción de pares clave valor (ordenada apartir de python 3.7)

auto = {"marca": "renault", "modelo": "clio", "año": 2025}
print(auto)
print(auto["marca"])
print(auto.get("marca"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("marca es una de las propiedades de este dicionario")

auto["año"] = 2020
print(auto)

auto["color"] = "verde"
print(auto)

auto.update({"año": 2022, "puertas": 4})
print(auto)

# auto.pop("puertas")
# print(auto)

# auto.popitem()
# print(auto)

# auto.clear()
# print(auto)

for k in auto:
    print(k)
print("_____________")
for v in auto.values():  # values
    print(v)
print("___________")

for k, v in auto.items():  # keys, value
    print(k, v)

familia = {
    "hijo1": {"nombre": "Pedro", "edad": "8"},
    "hijo2": {"nombre": "Ana", "edad": "7"},
    "hijo3": {"nombre": "Marcelo", "edad": "6"},
}
print(familia["hijo1"]["nombre"])
