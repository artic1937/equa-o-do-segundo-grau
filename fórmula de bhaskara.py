#isso é a fórmula de bhaskara 
from cmath import sqrt
A=input('qual a variável a ? ')
B=input('qual a variavel b ? ')
C=input('qual a variável c ? ')
A=int(A)
B=int(B)
C=int(C)

Delta = B**2 - 4*A*C
print(f'delta é igual a {Delta}')
x1 = (-B + sqrt(Delta))/(2*A)
x2 = (-B - sqrt(Delta))/(2*A)
print(x1, x2)