#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci_seq = [0, 1] if length > 1 else [0] if length == 1 else []
    while len(fibonacci_seq) < length:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    print(fibonacci_seq)
