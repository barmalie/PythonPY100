def task(num: int) -> bool:  # TODO добавить аннотацию типов
    digits_list = [int(d) for d in str(num)]
    sum_ = sum(digits_list)
    join_num = "".join([str(d) for d in digits_list])
if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
