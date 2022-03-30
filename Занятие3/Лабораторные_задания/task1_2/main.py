def factorial(n):
    current_n = 1
    while current_n < n:
        current_n *= n
        return current_n



if __name__ == "__main__":
    factorial(5)
    print(factorial(5))
    # TODO распечатать результат выполнения функции factorial от числа 5
