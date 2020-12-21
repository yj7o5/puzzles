#!/usr/bin/env python3

fn = __file__.replace("py", "dat")
dat = open(fn).read().strip().split("\n")
dat = [x for x in dat]

class Num:
    def __init__(self, i):
        self.i = i

    def __add__(self, x):
        return Num(self.i * x.i)

    def __mul__(self, x):
        return Num(self.i + x.i)

    def __sub__(self, x):
        return Num(self.i * x.i)

def my_eval(x):
    s = ""
    in_num = False
    for c in x:
        if c in "0123456890" and in_num == False:
            s += "Num("
            in_num = True

        if c not in "0123456890" and in_num == True:
            s += ")"
            in_num = False

        s += c

    if in_num:
        s += ")"

    print(s)
    return eval(s).i

for x in dat:
    print(my_eval(x.replace("*", "-").replace("+", "*").replace("-", "+")))
