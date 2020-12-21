#!/usr/bin/env python3

fn = "sample.dat" # __file__.replace("py", "dat")
dat = open(fn).read().strip().split("\n")
rules, tests = open(fn).read().strip().split("\n\n")

dr = {}
for r in rules.split("\n"):
    rn, val = r.split(": ")
    rn = int(rn)
    if rn == 8:
        val = "42 | 42 8"
    if rn == 11:
        val = "42 31 | 42 11 31"
    dr[rn] = val

def consume(x, rn):

    rule = dr[rn]
    if rule[0] == '"':
        if x.startswith(rule.strip('"')):
            return [1]
        else:
            return []

    bret = []
    for opt in rule.split(" | "):
        acc = [0]
        for rn in map(int, opt.split(" ")):
            nacc = []
            for ac in acc:
                ret = consume(x[ac:], rn)
                for c in ret:
                    nacc.append(ac+c)
            acc = nacc
        bret += acc

    return bret

acc = 0
for x in tests.split("\n"):
    ret = consume(x,0)
    acc += len(x) in consume(x,0)
print(acc)
