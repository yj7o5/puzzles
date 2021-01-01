#!/usr/bin/env python3

import sys
import re
import random
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

# TODO: faster implementation using bitmaps 

def part_a(lines, instructions):
    total_lit = 0

    for i in range(1000):
        for j in range(1000):
            active = False

            for (action, d1, d2) in instructions:
                if i >= d1.x and i <= d2.x and j >= d1.y and j <= d2.y:
                    if action == "turn on":
                        active = True
                    elif action == "turn off":
                        active = False
                    else:
                        active = not active

            if active:
                total_lit += 1

    return total_lit

def part_b(lines, instructions):
    total_brightness = 0

    for i in range(1000):
        for j in range(1000):
            brightness = 0

            for (action, d1, d2) in instructions:
                if i >= d1.x and i <= d2.x and j >= d1.y and j <= d2.y:
                    if action == "turn on":
                        brightness += 1
                    elif action == "turn off":
                        brightness = max(0, brightness-1)
                    else:
                        brightness += 2

            total_brightness += brightness

    return total_brightness

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

with open(filename) as file:
    text = file.read().strip()
    lines = text.split("\n")

    regex = r"(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)"
    instructions = []

    for line in lines:
        match = re.findall(regex, line.strip())[0]

        action = match[0].strip()
        d1 = Point(int(match[1]), int(match[2]))
        d2 = Point(int(match[3]), int(match[4]))

        instructions.append((action, d1, d2))

    total_lit = part_a(lines, instructions)
    print(f'Total lit: {total_lit}')

    total_brightness = part_b(lines, instructions)
    print(f'Total brightness: {total_brightness}')
