if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5
    for index, phrase in enumerate( phrase, start=initial_offset ):
        initial_offset += 1

        print(" "*index, phrase)
    # TODO чему равно начальное смещение?
    # TODO как использовать начальное смещение в команде enumerate?
