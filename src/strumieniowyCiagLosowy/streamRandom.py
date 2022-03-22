#!/usr/bin/python3
def generate_stream(l: int, init_array: list, polynomial: list):
    ret = []
    # polynomial.reverse()
    for i in range(l):
        print(f"i {i}")
        print(f"init_array {init_array}")
        ret.append(init_array[-1])
        new_bit = 0  # init_array[-1]  # możliwe wykorzystanie init_array[-2]
        print(f"  init_array[-1] {init_array[-1]}")
        for y in polynomial:
            print(f"    y {y}")
            print(f"    init_array[y] {init_array[y]}")
            print(f"    new_bit {new_bit}")
            print(f"    new_bit = xor(init_array[y], new_bit) {xor(init_array[y], new_bit)}")

            new_bit = xor(init_array[y], new_bit)
        print(f"  [new_bit, ] + init_array[:-1] {[new_bit, ] + init_array[:-1]}")

        init_array = [new_bit, ] + init_array[:-1]

    return ret


def xor(a, b):
    ret = 0
    if bool(a) != bool(b):
        ret = 1
    return ret


print(__name__)
if __name__ == "__main__":
    temp = [0, 1, 0, 1,1,1]

    print(generate_stream(10, temp, [1, 3]))
