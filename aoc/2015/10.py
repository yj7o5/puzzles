#!/usr/bin/env python3

"""
Look-and-say sequence
"""

def next_number(number):
    i, n = 0, len(number)
    new_number = ""

    while i < n:
        j = i + 1
        c = number[i]
        digits = c

        while j < n and number[j] == c:
            digits += c
            j += 1

        count = len(digits)
        digit = int(c)
        new_number += f"{count}{digit}"

        i = j

    return new_number

def sequence(number, count):
    i = 0

    number = str(number)
    while i < count:
        number = next_number(number)

        yield (i+1, number)
        i += 1

part_a = None
part_b = None
for (sq, value) in sequence("3113322113", 50):
    if sq == 40:
        part_a = len(value)
    if sq == 50:
        part_b = len(value)

print(f"Part A: {part_a}")
print(f"Part B: {part_b}")
