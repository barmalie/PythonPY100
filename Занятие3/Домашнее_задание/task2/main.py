def check_string(str_):
    if not str_:# Просмотреть про оператор if not
        return False

    base = set("01")
    for i in set(str_):
        if not i in base:
            return False
    return True


if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
