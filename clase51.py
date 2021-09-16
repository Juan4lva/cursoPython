# arreglos

# ejemplo:
# [1,5,8,9,30,9,13]
# imprimir por pantalla los numeros impares

a = [1,5,8,9,30,9,13]
b = []
for i in a:
    if i > 3 and i % 2 != 0:
        b.append(i)
print(b)