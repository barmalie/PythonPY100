def get_unique_words(str_words: str):
    list_words = str_words.lower().split()
    new_str = " ".join(list_words)


    ...  # TODO вывести множество уникальных слов


if __name__ == "__main__":
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
