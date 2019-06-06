def countdown_print(num):
    print(num)
    if num <= 1:
        return
    else:
        return countdown_print(num-1)

countdown_print(10)