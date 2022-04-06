def task(num: int):
    new_list = [int(num) for num in str(num)]  # TODO сформировать список цифр

    if (4 in new_list and 8 in new_list) or 9 in new_list:

        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
