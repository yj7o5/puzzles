"""
DP implementation

'.' matches any single character
'*' matches zero or more of the preceding element
"""

def is_match(input, pattern):
    if len(pattern)==0:
        return len(input)==0

    if len(pattern)>1 and pattern[1] == "*":
        return is_match(input, pattern[2:]) or (len(input)!=0 and (pattern[0]=="." or pattern[0]==input[0]) and is_match(input[1:], pattern))
    else:
        return len(input)!=0 and (pattern[0]=="." or pattern[0]==input[0]) and is_match(input[1:], pattern[1:])

def test_match(input, pattern, expected):
    result = is_match(input, pattern)

    if result != expected:
        print("input={} pattern={} match={} expected={}".format(input, pattern, result, expected))

    return result

if __name__ == "__main__":
    test_match("aa", "a*",True)
    test_match("aa", "a", False)
    test_match("aab", "c*a*b", True)
    test_match("aab", "c*x*b*a", False)
    test_match("ab", ".*", True)
    test_match("aab", "c*x*a*b", True)
    test_match("mississippi", "mis*is*p*.", False)
    test_match("ab", ".*c", False)
    test_match("aaa", "a*a", True)
    test_match("mississippi", "mis*is*ip*.", True)
    test_match("a", "ab*.", False)
    test_match("aj", "ab*.", True)
    test_match("ab", ".*..", True)
    test_match("a", "ab*c*", True)
