def remove_whitespace(str_):
    words_list = str_with_space.split() # TODO разделить строку по пробелам
    print(words_list)

   #  words_list_without_empty_string = []
   #  for word in words_list:
   #      words_list_without_empty_string.append(word)
   # #words_list_without_empty_string = " ".join(words_list)
   #  print(words_list_without_empty_string)

   # return " ".join(words_list_without_empty_string)  # TODO соединить список слов в строку
    return " ".join(words_list)  # TODO соединить список слов в строку

if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
