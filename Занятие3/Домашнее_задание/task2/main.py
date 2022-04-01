def check_string(str_):
    list_words = str_.lower().split()
    new_str = "".join(list_words)
    print(new_str)
    if include.str_("1","0") in list_words:
        print(list_words)

if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
