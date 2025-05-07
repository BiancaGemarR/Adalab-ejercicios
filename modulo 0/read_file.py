#Leer archivo linea por linea
with open("cuento.txt", "r") as file:
    for lineas in file:
        print(lineas.strip())

#leer todas las lineas en una lista
with open("cuento.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open("cuento.txt", "r") as file:
    file.write("\n\nBy:IA")

