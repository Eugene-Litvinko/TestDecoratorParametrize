

def sum_integers(first_integer, second_integer):
    return first_integer + second_integer

if __name__ == '__main__':

    print(sum_integers(12, 1))

    x = 99
    x1 = str(x)
    x2 = list(x1)
    x3 = map(int, x2)
    print(sum(x3))