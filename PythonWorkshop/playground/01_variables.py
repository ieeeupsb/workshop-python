"""Numbers"""

# assigning 3 to an integer variable
anInt = 3
alsoAnInt = int(3.0)
yetAnotherInt = int("3")

# assigning 3 to a float variable
aFloat = 3.0
alsoAFloat = float(3)

# assigning 3 to a (int) and 4.1 to b (float)
a, b = 3, 4.1

# division operator always returns floats (unlike C or C++)
print(a / b)  # 0.7317073170731708

# floor division
print(a // b)  # 0.0

# 4.1 to the 3rd power
print(b**a)  # 68.9209999

# python has in-built complex numbers :D
unicorn = 1 + 2j

# print real part of complex number
print(unicorn.real)  # 1.0
# print imaginary part of complex number
print(unicorn.imag)  # 2.0

# most built-in operators support complex numbers

"""End of Numbers """

"""Strings"""

# assigning to a string variable
aChar = "3"  # this is actually just a one character long string
aString = "333333"
alsoAString = '3333333'
anotherString = str(3333333)
anotherString = str('3333333')


# normal string
normalString = "C:\numbers"  # treats backslashes as special charaters
# raw strings (notice the r before the string)
rawString = r"C:\numbers"  # ignores backslashes

# multiline strings
tripleQuotedString = """\
This kind of string can span multiple

lines
        and keeps its
            formatting!
"""


coolString = "The quick brown fox jumped over the lazy dog"

# get string length (number of characters)
length = len(coolString)  # 44

# python slices use [start:stop:step] [-startBackwards]

index0 = coolString[0]  # the letter 'T'
index5 = coolString[5]  # the letter 'u'

lastChar = coolString[len(coolString) - 1]  # the letter 'd'
alsoLastChar = coolString[-1]  # the letter 'd'

secondToLastChar = coolString[-2]  # the letter 'o'

firstChar = coolString[-len(coolString)]  # the letter 'T'

coolSlice = coolString[4:23]  # the string 'quick brown fox jum'

coolSliceFromStart = coolString[:23]  # the string 'The quick brown fox jum'

coolSliceToEnd = coolString[4:]  # 'quick brown fox jumped over the lazy dog'

pointlessSlice = coolString[::]  # the original string

jumpingSlice = coolString[4:23:2]  # 'qikbonfxjm'

gnirtSlooc = coolString[::-1]  # reversed version of original string

# negative steps need to on an extra slicing operation
gnirtSloocSlice = coolString[0:23][::-2]

# concatenation of strings
pp = "pen pineapple"
ap = "apple pen"
concatenation = pp + ap  # pen pineapple apple pen

repeatedString = "3" * 3  # string '333'

mixedTypeConcatenation = str(3) + "3"  # string '33'

# can't do the following because strings in python are immutable
# coolString[0] = "l"
# though you can just as easily create a new string
newString = "l" + coolString[1:]


""" End of Strings """

