#!/usr/bin/env python3

import sys
import io
import json

def deep_sum(node, is_part_a):
    total = 0
    node_type = type(node)

    if node_type == dict:
        if is_part_a or "red" not in node.values():
            for k in node.keys():
                total += deep_sum(node[k], is_part_a)
    elif node_type == list:
        for item in node:
            total += deep_sum(item, is_part_a)
    elif node_type == int:
        total += node

    return total

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

with open(filename) as file:
    text = file.read()
    doc = json.load(io.StringIO(text))

    print("Part A: ", deep_sum(doc, True))
    print("Part B: ", deep_sum(doc, False))
