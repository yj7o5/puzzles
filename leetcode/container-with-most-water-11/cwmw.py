"""
area = length of shorter vertical line * distance between lines

Time: O(N)
Space: O(1)

"""

def maxarea(height):
    area = 0
    low, high = 0, len(height) - 1

    while low < high:
        area = max(area, (high-low)*min(height[low], height[high]))

        if height[low] >= height[high]:
            high -= 1
        else:
            low += 1

    return area

def test_match(input, expected):
    actual = maxarea(input)

    print("input={} actual={} expected={}".format(input, actual, expected))

if __name__ == "__main__":
    test_match([1,8,6,2,5,4,8,3,7], 49)
    test_match([4,3,2,1,4], 16)
    test_match([1,2,1], 2)
    test_match([1,1], 1)
    test_match([2,3,4,5,18,17,6], 17)
