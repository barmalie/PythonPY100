def input_numbers():
    num_lisst =[]
    while True:
        num_ = int(input())
        if 3<=num_<=13:
            num_lisst.append(num_)
        if num_<0:
            break
    return num_lisst



if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
