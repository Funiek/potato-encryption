#!/usr/bin/python3
def generate_stream(l: int, init_array: list, polynomial: list):
    ret = []
    polynomial.reverse()
    for i in range(l):
        ret.append(init_array[-1])
        new_bit = xor(1,init_array[-1])  # możliwe wykorzystanie init_array[-2]

        for y in polynomial:
            new_bit = xor(init_array[y], new_bit)
        init_array = [new_bit, ] + init_array[:-1]

    return ret


def xor(a, b):
    ret = 0
    if bool(a) != bool(b):
        ret = 1
    return ret


print(__name__)
if __name__ == "__main__":
    print(generate_stream(10, [0, 1, 1, 0], [0, 1]))
