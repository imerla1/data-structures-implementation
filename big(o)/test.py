def check_even_or_odd(num: int):
    # least significant bit
    lsb = bin(num)[-1]
    if int(lsb):
        return "odd"
    return "even"

def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

    