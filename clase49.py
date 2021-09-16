# del & in

curso = 'python'
lista_nueva = list(curso)
print(lista_nueva)

del lista_nueva[0]
print(lista_nueva)

print('y' in curso)

if 'y' in lista_nueva:
    print('y es parte de la lista')