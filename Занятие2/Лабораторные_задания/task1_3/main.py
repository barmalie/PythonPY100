A = int(input())
B = int(input())
C = (A**2)+(B**2)
D = (A+B)**2
if D > C:
    print('квадрат суммы больше', D, ">", C)
elif C < D:
    print('сумма квадратов больше', C, "<", D)