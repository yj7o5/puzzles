#!/usr/bin/env python3

from sys import argv

class Solution:
    def read(self, lines):
        for i in range(len(lines)):
            yield (i, lines[i])

    def part_a(self, text):
        lines = text.split("\n")
        dimensions = []
        for line in lines:
            l,w,h = map(int, line.split("x"))
            dimensions.append(2*(l*w + w*h + h*l) + min(l*w, w*h, l*h))

        return sum(dimensions)

    def part_b(self, text):
        lines = text.split("\n")
        dimensions = []
        for line in lines:
            l,w,h = map(int, line.split("x"))
            smallest_param = sum(sorted([l,w,h])[:-1])
            dimensions.append(2 * smallest_param + l*w*h)

        return sum(dimensions)

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(argv) > 1 and argv[1] == "-s" else i_file

s = Solution()
with open(filename) as file:
    text = file.read().strip()
    print(s.part_a(text))
    print(s.part_b(text))
