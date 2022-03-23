if __name__ == '__main__':
    A = int(input())
    B = int(input())
    word_a = A % 2 == 1
    word_b = B % 2 == 1
    if word_a == 1 and word_b == 1:
        print ("нечетные A и B")