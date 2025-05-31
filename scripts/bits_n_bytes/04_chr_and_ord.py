# References:
# (1) chr: https://www.w3schools.com/python/ref_func_chr.asp
# (2) ord: https://www.programiz.com/python-programming/methods/built-in/ord
from constants.constants import GERMAN_LETTERS

if __name__ == "__main__":
    # chr: number ---> its ASCII / Unicode symbol
    # ord: symbol ---> its number in ASCII / Unicode
    for k in range(257):
        print(f"{k:03}: {chr(k)}, {ord(chr(k))}")

    for l in GERMAN_LETTERS:
        print(f"{l}: {ord(l):08}")
