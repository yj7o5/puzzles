#!/usr/bin/env python3

from sys import argv

parens = { "(": 1, ")": -1 }

class Solution:
    def read(self, lines):
        for i in range(len(lines)):
            yield (i, lines[i])

    def part_a(self, text):
        return sum([parens[c] for _, c in self.read(text)])

    def part_b(self, text):
        total = 0
        for i, c in self.read(text):
            total += parens[c]
            if total == -1:
                return i+1

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(argv) > 1 and argv[1] == "-s" else i_file

s = Solution()
with open(filename) as file:
    text = file.read().strip()
    print(s.part_a(text))
    print(s.part_b(text))
