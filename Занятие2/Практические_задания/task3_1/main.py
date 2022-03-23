number = 13

cond_1 =number%2 ==0
cond_2 =number%3 ==0

if cond_2 == 0 or cond_1:
    print('Число number кратно 2 или 3')
else:
    print("число не кратно 2 или 3")
