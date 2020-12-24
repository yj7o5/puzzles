#!/usr/bin/env python3

from sys import argv, maxsize
from hashlib import md5

class Solution:
    def find_hash(self, secret, criteria):
        for i in range(1, maxsize):
            key = f'{secret}{i}'
            digest = md5(key.encode()).hexdigest()

            if criteria(digest):
                return i

    def part_a(self, text):
        secret = text.split("\n")[0]
        prefix = '0'*5

        return self.find_hash(secret, lambda x: x.startswith(prefix))

    def part_b(self, text):
        secret = text.split("\n")[0]
        prefix = '0'*6

        return self.find_hash(secret, lambda x: x.startswith(prefix))

p_number = __file__.replace(".py", "").split("/")[-1]
s_file = f"./input/{p_number}.sample"
i_file = f"./input/{p_number}.input"
filename = s_file if len(argv) > 1 and argv[1] == "-s" else i_file

s = Solution()
with open(filename) as file:
    text = file.read().strip()
    print(s.part_a(text))
    print(s.part_b(text))
