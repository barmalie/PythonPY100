if __name__ == "__main__":
    list_ = [1, 4, 3, 5, 2, 53, 4]
    print(list_)
    print(max(list_))
    list_[0], list_[5] = list_[5], list_[0]
    print(list_)
    for index, list_ in enumerate(list_):
        print(list_, index)


# list_ = [1, 4, 3, 5, 2, 53, 4]
# x = max(list_)
# list_[0], x = x, list_[0]
# print(list_)
