def fact(num):
    """
    Input: An integer num >= 0
    Output: Factorial value 
    """
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

for idx in range(0, 11):
    print("Current input: " + str(idx))
    print("Factorial value: " + str(fact(idx)))
    print("---------------------------------")

