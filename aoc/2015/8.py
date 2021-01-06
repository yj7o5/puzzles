#!/usr/bin/env python3

import sys

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

def part_a(lines):

    def unescape(line):
        scheme = "unicode_escape"
        return line.encode().decode(scheme)

    total = 0
    for line in lines:
        char_num = max(len(line), 2)
        escape_char_num = len(unescape(line)) - 2

        total += char_num - escape_char_num

    return total

def part_b(lines):
    def escape(line):
        escape_line = "\""
        for c in line:
            if c == '"':
                escape_line += "\\\""
            elif c == '\\':
                escape_line += "\\\\"
            else:
                escape_line += c
        escape_line += "\""

        return escape_line

    total = 0
    for line in lines:
        char_num = len(line)
        escape_char_num = len(escape(line))

        total += escape_char_num - char_num

    return total

with open(filename) as file:
    text = file.read().strip()
    lines = text.split("\n")

    print(f"Part a: {part_a(lines)}")
    print(f"Part b: {part_b(lines)}")
