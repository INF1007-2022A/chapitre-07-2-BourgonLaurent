#!/usr/bin/env python

from collections import deque
from typing import Iterator


def get_fibonacci_number(i: int) -> int:
    return (
        0
        if i == 0
        else 1
        if i == 1
        else get_fibonacci_number(i - 1) + get_fibonacci_number(i - 2)
    )


def get_fibonacci_sequence(n: int) -> list[int]:
    fib = [0, 1]

    if n <= 2:
        return fib[0:n]

    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib


def get_sorted_dict_by_decimals(d: dict[str, float]) -> dict[str, float]:
    return dict(sorted(d.items(), key=lambda x: x[1] % 1))


def fibonacci_numbers(n: int) -> Iterator[int]:
    previous = 0
    yield previous

    current = 1
    yield current

    succeeding = 0

    for _ in range(2, n):
        succeeding = previous + current
        previous, current = current, succeeding
        yield current


def build_recursive_sequence_generator(TODO):
    pass


if __name__ == "__main__":
    print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
    print([get_fibonacci_number(i) for i in range(10)])
    print()

    print(get_fibonacci_sequence(1))
    print(get_fibonacci_sequence(2))
    print(get_fibonacci_sequence(10))
    print()

    spam = {2: 2.1, 3: 3.3, 1: 1.4, 4: 4.2}
    eggs = {"foo": 42.6942, "bar": 42.9000, "qux": 69.4269, "yeet": 420.1337}
    print(get_sorted_dict_by_decimals(spam))
    print(get_sorted_dict_by_decimals(eggs))
    print()

    for fibo_num in fibonacci_numbers(10):
        print(fibo_num, end=" ")
    print("\n")

    # def fibo_def(last_elems):
    #     return last_elems[-1] + last_elems[-2]

    # fibo = build_recursive_sequence_generator([0, 1], fibo_def)
    # for fi in fibo(10):
    #     print(fi, end=" ")
    # print("\n")

    # lucas = build_recursive_sequence_generator(TODO)
    # print(f"Lucas : {[elem for elem in lucas(10)]}")
    # perrin = build_recursive_sequence_generator(TODO)
    # print(f"Perrin : {[elem for elem in perrin(10)]}")
    # hofstadter_q = build_recursive_sequence_generator(TODO)
    # print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
