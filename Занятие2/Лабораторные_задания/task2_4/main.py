if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 1
    for index, word in enumerate(phrase, start=5):
        print(" "*index, word)
