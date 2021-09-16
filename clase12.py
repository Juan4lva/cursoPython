# tabla de multiplicar

n = int(input("Ingresa la tabla correspondiente que desea leer : " ))
i = 0
a = 10

#Accion

while i <= a: 

    r = n * i #cuenta

    print ("{} x {} = {}".format(n,i,r)) #Impresion
    i = i+1 #Acumulador

print('tabla de multiplicar del: ', n)