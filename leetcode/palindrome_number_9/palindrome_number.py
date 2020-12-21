"""
# slow but simple
def ispalindrome(input):
    input = str(input)
    return input == input[::-1]
"""

def ispalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    rev = 0

    while(x > rev):
        p = x % 10
        x = int(x / 10)
        rev = rev * 10 + p

    return rev == x or rev/10 == x

if __name__ == '__main__':
    print("121=True", ispalindrome(121))
    print("12321=True", ispalindrome(12321))
    print("123212=False", ispalindrome(123212))
    print("1221=True", ispalindrome(1221))
    print("10=False", ispalindrome(10))
    print("100=False", ispalindrome(100))
    print("1001=True", ispalindrome(1001))
