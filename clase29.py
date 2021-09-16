# continue
n = int(input('ingrese un numero: '))
for i in range(1,n+1):
    if i % 2 == 0:
        continue # salta a la siguiente instruccion (no sea par)
        print(i)
    else:
        print(i)
