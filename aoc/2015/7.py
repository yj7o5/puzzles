#!/usr/bin/env python3

import sys
import re

from collections import defaultdict

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(sys.argv) > 1 and sys.argv[1] == "-s" else i_file

class Evaluation:
    def __init__(self, statements):
        self.statements = statements
        self.variables = defaultdict()

    def solve(self):
        for (variable, statement) in self.statements.items():
            self.variables[variable] = self.resolve(variable, statement)

    def resolve(self, variable, statement):
        if variable in self.variables:
            return self.variables[variable]

        op = statement[0]

        if op == "assignment":
            return self.resolve_assignment(statement)
        elif op == "binary":
            return self.resolve_binary(variable, statement)
        elif op == "unary":
            return self.resolve_unary(variable, statement)
        else:
            raise Exception(f"operation={op} not supported")

    def resolve_assignment(self, statement):
        value = statement[2]
        value = self.resolve_numeric(value)

        return value if value != None else self.resolve(value, self.statements[value])

    def resolve_binary(self, variable, statement):
        _, operation, lhs, rhs = statement

        lhs_value = self.resolve_numeric(lhs)
        lhs_value = lhs_value if lhs_value else self.resolve(lhs, self.statements[lhs])

        rhs_value = self.resolve_numeric(rhs)
        rhs_value = rhs_value if rhs_value else self.resolve(rhs, self.statements[rhs])

        if operation == "AND":
            self.variables[variable] = (lhs_value & rhs_value) & 0xFFFF
        elif operation == "OR":
            self.variables[variable] = lhs_value | rhs_value
        elif operation == "LSHIFT":
            self.variables[variable] = (lhs_value << rhs_value) & 0xFFFF
        elif operation == "RSHIFT":
            self.variables[variable] = lhs_value >> rhs_value
        else:
            raise Exception(f'{operation} not supported equation={statement}')

        return self.variables[variable]

    def resolve_unary(self, variable, statement):
        _, operation, inp = statement

        if operation == "NOT":
            value = self.resolve_numeric(inp)
            value = value if value != None else self.resolve(inp, self.statements[inp])

            self.variables[variable] = (65535 - value)
        else:
            raise Exception(f"{operation} not supported equation={statement}")

        return self.variables[variable]

    def resolve_numeric(self, maybe_value):
        return int(maybe_value) if maybe_value.isnumeric() else self.variables.get(maybe_value)

    def print_result(self):
        for var, value in self.variables.items():
            print(f'{var}={value}')

class Operations:
    binary = re.compile(r"^(\w+) (\w+) (\w+) -> (\w+)$")
    unary = re.compile(r"^(\w+) (\w+) -> (\w+)$")
    assignment = re.compile(r"^(\d+|\w+) -> (\w+)$")

with open(filename) as file:
    text = file.read().strip()
    lines = text.split("\n")

    statements = defaultdict()

    for line in lines:
        if (p := Operations.binary.match(line)):
            lhs, op, rhs, variable = p.groups()

            statements[variable] = ("binary", op, lhs, rhs)

        if (p := Operations.unary.match(line)):
            op, ipt, variable = p.groups()

            statements[variable] = ("unary", op, ipt)

        if (p := Operations.assignment.match(line)):
            value, variable = p.groups()

            statements[variable] = ("assignment", variable, value)

    evaluation = Evaluation(statements)

    evaluation.solve()

    evaluation.print_result()
