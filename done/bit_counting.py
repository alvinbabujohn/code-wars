"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""


def count_bits(n):
    return len("{0:b}".format(n).replace("0", ""))


print(count_bits(0), 0)
print(count_bits(4), 1)
print(count_bits(7), 3)
print(count_bits(9), 2)
print(count_bits(10), 2)
