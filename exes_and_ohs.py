"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


def xo(s=""):
    return len([x for x in s.lower() if x == "x"]) == len(
        [o for o in s.lower() if o == "o"]
    )


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
