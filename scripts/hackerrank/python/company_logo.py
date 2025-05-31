# Cf.: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter, defaultdict
from itertools import product


def find_key_letters(name: str):
    letters_counts = dict(Counter(name))
    letters_counts = list(zip(letters_counts.keys(), letters_counts.values()))
    letters_counts = sorted(letters_counts, key=lambda x: x[1], reverse=True)
    distinct_counts = [x[1] for x in letters_counts]
    count_to_letters = []
    for c in set(distinct_counts):
        count_to_letters.append((c, tuple((x[0] for x in letters_counts if x[1] == c))))
    count_to_letters = sorted(count_to_letters, key=lambda x: x[0], reverse=True)
    count_to_letters = [(p[0], sorted(p[1])) for p in count_to_letters]
    key_letters = [
        (y, x)
        for count, letters in count_to_letters
        for x, y in product([count], letters)
    ][:3]
    return key_letters


if __name__ == "__main__":

    company_name = "GOOGLE"

    # Counter(company_name)
    find_key_letters(name=company_name)