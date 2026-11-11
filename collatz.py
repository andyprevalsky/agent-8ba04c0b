#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and its total number of steps.

Rule: if n is even, n -> n // 2; if n is odd, n -> 3n + 1. Repeat until n == 1.
The step count is the number of transformations applied, which is one less
than the number of terms printed.
"""

START = 27


def collatz_sequence(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    if n < 1:
        raise ValueError("start must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(START)
    for number in sequence:
        print(number)
    steps = len(sequence) - 1
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
