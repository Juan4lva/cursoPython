# serie fibonacci
'''
ejemplo:
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
'''
n = int(input('ingrese un numero: '))
w1 = 1
w2 = 2
s = 0
c = 0
if n <= 0:
    print('error')
elif n == 1:
    n == 1
    print(w1)
else:
    while c < n:
        print(w1)
        s = w1 + w2
        # actualizar los datos
        w1 = w2
        w2 = s
        c += 1