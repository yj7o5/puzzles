#!/usr/bin/env python3

import sys
import functools
import re

part_a_constraints = {
    "([a-z])\\1": 1,
    "([aeiou])": 3,
    "(ab|cd|pq|xy)": 0
}

part_b_constraints = {
    "([a-z]{2})(?=[a-z]*\\1)": 1,
    "([a-z])[a-z]\\1": 1
}

class Solution:
    def check_all_constraints(self, text, constraints):
        matches = []
        for constraint in constraints.keys():
            count = constraints[constraint]
            match = re.findall(constraint, text)

            if count == 0:
                matches.append(len(match) == 0)
            else:
                matches.append(len(match) >= count)

        return all(matches)

    def solve_matches(self, text, constraints):
        lines = text.split("\n")
        count = 0
        for line in lines:
            count += int(self.check_all_constraints(line, constraints))

        return count

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

with open(filename) as file:
    text = file.read().strip()

    solution = Solution()

    print(solution.solve_matches(text, part_a_constraints))
    print(solution.solve_matches(text, part_b_constraints))
