#!/usr/bin/env python3

import sys
import re

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

def dfs(seatings, first_person, person, taken):
    taken.append(person)

    left_people = [seat for seat in seatings[person] if seat not in taken]

    if len(left_people) == 0:
        return seatings[person][first_person] + seatings[first_person][person]

    total = 0
    for next_person in left_people:
        curr = dfs(seatings, first_person, next_person, taken)
        curr += seatings[person][next_person]

        if seatings[next_person][person]:
            curr += seatings[next_person][person]

        if curr > total:
            total = curr

        taken.remove(next_person)

    return total

def find_total_change(seatings):
    start = next(iter(seatings))

    return dfs(seatings, start, start, list())

regex = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."

with open(filename) as file:
    lines = file.readlines()

    seatings = dict()

    for line in lines:
        match = re.match(regex, line)
        (person, gain_or_lose, happiness, other_person) = match.groups()

        happiness = int(happiness)
        if gain_or_lose == "lose":
            happiness = -happiness

        if seatings.get(person) == None:
            seatings[person] = dict()

        seatings[person][other_person] = happiness

    print("Part A: ", find_total_change(seatings))
    print("Part B: ", find_total_change(seatings))
