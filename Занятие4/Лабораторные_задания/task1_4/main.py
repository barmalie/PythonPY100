def more_than_mean(list_numbers: list):
    averange = sum(list_numbers)/len(list_numbers)
    #return [i for i in more_than_mean if i > averange]
    return [i for i in list_numbers if i > averange]
    ...  # TODO найти среднее арифметическое списка
    ...  # TODO с помощью list comprehension вернуть новый список


if __name__ == "__main__":
    print(more_than_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
