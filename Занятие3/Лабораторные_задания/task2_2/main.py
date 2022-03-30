def is_palindrome(str_: str):
    list_words = str_.lower().split()
    new_str = "".join(list_words)
    print(list_words)
    print(list_words[::-1])
    print(new_str)
    print(new_str[::-1])


    if new_str == new_str[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
