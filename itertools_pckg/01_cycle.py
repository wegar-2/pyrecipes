from itertools import cycle

from constants.constants import GERMAN_LETTERS

if __name__ == "__main__":

    for i, l, in enumerate(cycle(GERMAN_LETTERS)):
        if i > 100:
            break
        print(f"{i}: {l}")
        