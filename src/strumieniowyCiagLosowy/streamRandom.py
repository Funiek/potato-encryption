#!/usr/bin/python3
DEBUG = False


def generate_stream(l: int, init_array: list, polynomial: list):
    ret = []
    # polynomial.reverse()
    for i in range(l):
        Dprint(f"i {i}")
        Dprint(f"init_array {init_array}")
        ret.append(init_array[-1])
        new_bit = 0  # init_array[-1]  # możliwe wykorzystanie init_array[-2]
        Dprint(f"  init_array[-1] {init_array[-1]}")
        for y in polynomial:
            Dprint(f"    y {y}")
            Dprint(f"    init_array[y] {init_array[y]}")
            Dprint(f"    new_bit {new_bit}")
            Dprint(f"    new_bit = xor(init_array[y], new_bit) {xor(init_array[y], new_bit)}")

            new_bit = xor(init_array[y], new_bit)
        Dprint(f"  [new_bit, ] + init_array[:-1] {[new_bit, ] + init_array[:-1]}")

        init_array = [new_bit, ] + init_array[:-1]

    return ret


def xor(a, b):
    ret = 0
    if bool(a) != bool(b):
        ret = 1
    return ret


def Dprint(s):
    if DEBUG:
        print(s)


if __name__ == "__main__":
    temp = [0, 1, 0, 1, 1, 1]

    print(generate_stream(10, temp, [1, 3]))
