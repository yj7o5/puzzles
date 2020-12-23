#!/usr/bin/env python3

from sys import argv

updown = { '^': 1, '<': 0, '>': 0, 'v': -1 }
leftright = { '^': 0, '<': -1, '>': 1, 'v': 0 }

class Solution:
    def read(self, lines):
        for i in range(len(lines)):
            yield (i, lines[i])

    def part_a(self, text):
        x, y = 0, 0
        delivered = set([(x, y)])

        for line in text:
            for c in line:
                x += leftright[c]
                y += updown[c]
                delivered.add((x,y))

        return len(delivered)

    def part_b(self, text):
        x1, y1 = 0, 0
        x2, y2 = 0, 0

        delivered = set([(x1, y1)])

        s_turn = False
        for c in text:
            if s_turn:
                s_turn = False
                x1 += leftright[c]
                y1 += updown[c]
                delivered.add((x1, y1))
            else:
                s_turn = True
                x2 += leftright[c]
                y2 += updown[c]
                delivered.add((x2, y2))

        return len(delivered)

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(argv) > 1 and argv[1] == "-s" else i_file

s = Solution()
with open(filename) as file:
    text = file.read().strip()
    print(s.part_a(text))
    print(s.part_b(text))
