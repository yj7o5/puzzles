#!/usr/bin/env python3

class PasswordGenerator:
    def __init__(self, pwd):
        self._seed = pwd
        self._criterias = []

    def next(self):
        pwd = self._seed
        while True:
            pwd = self._increment(pwd)
            if self._passes_criterias(pwd):
                break

        self._seed = pwd
        return pwd

    def set_criteria(self, criteria):
        self._criterias.append(criteria)

    def _increment(self, pwd):
        next_pwd = list(pwd)
        flip = False

        for i in range(len(pwd)-1, -1, -1):
            letter = pwd[i]
            flip = ord(letter)+1 > ord('z')
            next_pwd[i] = chr(((ord(letter)-97 + 1) % 26)+97)

            if not flip:
                break

        return "".join(next_pwd)

    def _passes_criterias(self, s):
        return all([c(s) for c in self._criterias])

gen = PasswordGenerator("hxbxwxba")

def n_consecutive_letters(pwd, i):
    return ord(pwd[i])+1 == ord(pwd[i+1]) and ord(pwd[i+1])+1 == ord(pwd[i+2])

gen.set_criteria(lambda pwd: any([n_consecutive_letters(pwd, i) for i in range(len(pwd)-2)]))
gen.set_criteria(lambda pwd: all([i not in pwd for i in "iol"]))
gen.set_criteria(lambda pwd: len(set(filter(lambda p: p[0]==p[1], zip(pwd, pwd[1:])))) > 1)

print("Part A: ", gen.next())
print("Part B: ", gen.next())

