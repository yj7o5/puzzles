"""
'.' matches any single character
'*' matches zero or more of the preceding element

Uses Thompsons construction technique to generate the DFA.

Time: O(2^n)
Space: O(1)

NFA State Machine
"ab*c"
q0 -> E -> q1
q1 -> a -> q2
q2 -> b -> q2
q2 -> E -> q3
q3 -> c -> qf
"""

EPSILON = "EPSILON"
KLEENE_STAR = "*"

class Fragment:
    def __init__(self, accept=EPSILON):
        self.accept = accept
        self.out = None #State

    def accepts(self, input):
        return self.accept == input or (self.accept == "." and input != EPSILON)

class State:
    def __init__(self, end=False):
        self.end = end
        self.first_frag = None
        self.sec_frag = None

    def get_transitions(self):
        transitions = filter(lambda x: x is not None, list([self.first_frag, self.sec_frag]))

        return transitions

def nfa(pattern):
    f_state = l_state = State()
    f_state.first_frag = Fragment()

    i = 0
    n = len(pattern)

    while i < n:
        s = State()
        s.first_frag = Fragment(pattern[i])

        if (i+1) < n and pattern[i+1] == KLEENE_STAR:
            s.sec_frag = Fragment()
            i += 1

        if l_state.sec_frag is None:
            l_state.first_frag.out = s
        else:
            l_state.first_frag.out = l_state
            l_state.sec_frag.out = s

        l_state = s
        i += 1

    end = State(True)
    l_state.first_frag.out = end

    if l_state.sec_frag is not None:
        l_state.first_frag.out = l_state
        l_state.sec_frag.out = end

    return f_state

def match(state, input, i = 0):
    for t in state.get_transitions():
        if t.accepts(EPSILON) and match(t.out, input, i):
            return True

    if i < len(input):
        symbol = input[i]

        for t in state.get_transitions():
            if t.accepts(symbol) and match(t.out, input, i+1):
                return True

        return False
    else:
        return state.end

def test_match(input, pattern, expected):
    state = nfa(pattern)
    result = match(state, input)

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
    test_match("a", "ab*c*", True)
    test_match("a", "ab*.", False)
    test_match("aj", "ab*.", True)
    test_match("ab", ".*..", True)
