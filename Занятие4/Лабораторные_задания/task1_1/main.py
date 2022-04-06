def task(n, m):  # TODO записать функцию с аннотацией типов

    return [n**2 for n in range(n,m+1)]


if __name__ == "__main__":
    number_n = 10
    number_m = 20

    print(task(number_n, number_m))
