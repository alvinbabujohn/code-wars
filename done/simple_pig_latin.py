"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    return " ".join(
        f"{t[1:]}{t[:1]}ay" if t and ord(t[:1]) > 64 and ord(t[:1]) < 123 else t
        for t in text.split(" ")
    )


print(pig_it("Pig latin is cool") == "igPay atinlay siay oolcay")
print(pig_it("This is my string") == "hisTay siay ymay tringsay")
