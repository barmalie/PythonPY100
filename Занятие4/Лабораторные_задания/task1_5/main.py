if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    # for i in list_:
    #     if i%2 ==0:
    #         print(end = " ")
    #     elif i%2 == 1:
    #         print(end=" ")
    #         if len(1)>len(2):
    #             print("четных больше")
    #         else:
    #             print("количество чисел одинаково")
    num_1 = [num for num in list_ if num%2 == 0]
    num_2 = [num for num in list_ if num % 2 == 1]
    list_1 =len(num_1)
    list_2 =len(num_2)
    if len(num_1) > len(num_2):
                    print("четных больше")
    else:
                    print("количество чисел одинаково")
            # TODO получить два списка четных и нечетных чисел

    ...  # TODO найти длины этих списков

    ...  # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
