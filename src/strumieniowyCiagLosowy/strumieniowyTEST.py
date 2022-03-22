import streamRandom as st

import numpy as np
from pylfsr import LFSR

n = 100000
state_len = 100

passed = 0
failed = 0


def main():
    global failed
    global passed
    for it in range(n):
        if it % 100 == 0:
            print(it)
        state = list(np.random.randint(0, 2, state_len))
        fpoly = list(np.random.permutation(state_len - 1) + 1)
        fpolyNumber = np.random.randint(2, state_len)
        fpoly = fpoly[:fpolyNumber]
        fpoly.sort()
        fpoly.reverse()

        b = brut(fpoly, state)
        w = np.array(wzorcowa(fpoly, state))

        if not np.array_equal(w, b):
            failed = failed + 1
            print(f'brut: {b}\t wz: {w}')
            print(f'fpoly {fpoly}')
            print(f'state {state}')
            print(f'number {failed + passed}')
            print("########")
        else:
            passed = passed + 1
    print(f'Passed: {passed / (passed + failed) * 100}% of {n} tests')


def brut(fpoly, state):
    L = LFSR(fpoly=fpoly, initstate=state)
    # L.info()
    tempseq = L.runKCycle(state_len)
    return tempseq


def wzorcowa(fpoly, state):
    tempseq = st.generate_stream(state_len, state, fpoly)
    return tempseq


if __name__ == "__main__":
    main()
