if __name__ == "__main__":
    number = 123456789

    list_digits = [int(d) for d in str(number)]  # TODO c помощью list comprehension получить список цифр числа
    print(list_digits)

    print(sum(list_digits))  # TODO найти сумму цифр числа

    print(sum([d for d in list_digits if d%2 ==0]))  # TODO найти сумму всех четных чисел #немного не додумал где sum поставить

    print(len(list_digits))  # TODO найти количество цифр

    print(min(list_digits))  # TODO найти минимальную цифру

    print(list_digits[0::2])  # TODO все цифры стоящие на нечетных местах

    print(list_digits[0]-list_digits[8])
