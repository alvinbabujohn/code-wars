"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(string, markers=[]):
    for mark in markers:
        string = "\n".join(
            "".join(s.split(mark)[:1]).rstrip() for s in string.splitlines()
        )
    return string


print(
    repr(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])),
    repr("apples, pears\ngrapes\nbananas"),
)
print(repr(solution("a #b\nc\nd $e f g", ["#", "$"])), repr("a\nc\nd"))
