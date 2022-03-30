def factorial(n):
    f0, f1 = 0, 1
    f = [1]*n

    for i in range(1, n):
        f[i] = f0 + f1
        f0, f1 = f1, f[i]

    return f



if __name__ == "__main__":
    factorial(5)
    print(factorial(5))
    # TODO распечатать результат выполнения функции factorial от числа 5
