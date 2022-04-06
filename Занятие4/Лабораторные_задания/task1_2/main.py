def task(n: int, m: int) -> list:  # TODO указать аннотацию типов
    return [n**2 for n in range(n, m+1) if n%2 == 1]
if __name__ == "__main__":
    number_n = 5
    number_m = 37
    print(task(5, 37))
