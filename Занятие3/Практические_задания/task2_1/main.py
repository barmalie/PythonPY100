def get_year_count(first_money, inflation):
    current_money = first_money  # TODO установить текущую сумму, которая будет с каждым годом уменьшаться
    count_years = 0

    while True:
        current_money = (current_money*(1 - inflation))
        count_years += 1
        if current_money < (first_money/2):
            break

    return count_years


if __name__ == "__main__":
    print(get_year_count(10000, 0.2))
