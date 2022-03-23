mount = int(input("Месяц: "))

if mount == 3 \
        or mount == 4 \
        or mount == 5:
    print("Весна")
elif mount in [6,7,8]:  # TODO проверить вхождение месяца в список месяцев лета
    print("Лето")
elif mount in (9,10,11):  # TODO проверить вхождение месяца в кортеж месяцев осени
    print("Осень")
elif mount in {12,1,2}:  # TODO проверить вхождение месяца в множество месяцев лета
    print("Зима")
else:
    print("неравильный месяц")

