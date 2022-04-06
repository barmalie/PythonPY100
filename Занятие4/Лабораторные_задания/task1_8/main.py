def task(src_list: list) -> list:  # TODO записать решение в виде функции
    #return [i**3 for i in src_list if i >= 0 ] #[64, 1000, 27, 512, 216, 729]
    return [i**3 if i >0 else 0 for i in src_list]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    new_list = task(list_)
    print(new_list)
