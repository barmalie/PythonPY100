# Пусть функция принимает два числа, складывает их и возвращает результат
def add_func(a, b):
    # a и b аргументы, которые принимает функция
    # эти аргументы будут не доступны вне тела функции
    add = a + b

    # чтобы вернуть результат нужно использовать ключевое слово return
    return add


if __name__ == "__main__":
    result =add_func(2,3)  # TODO вызвать функцию add_func

    print(result)
