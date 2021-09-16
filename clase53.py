# vectores y matrices

import numpy as np

vector = np.array([6,1,5,2,4])
matriza = np.array([[6,1,5],[4,5,6],[7,8,9]])
matrizb = np.array([[6,1,5],[4,5,6],[7,8,9]])

#print(vector.astype(str))
#print(vector.astype(float))

a = np.array([6,1,3,5,7])
b = np.array([6,1,5,8,3])

print(a+b)
print(a>b)

print(vector[3])
print(vector.min())
print(vector.argmax())

print(vector)
print(matriza + matrizb)

print('vector:' ,vector.size)
print('matriza:' ,matriza.size)