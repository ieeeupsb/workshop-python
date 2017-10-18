

"""Lists"""

aList = [0, 3.0, "totally a number", 1 + 2j, [1, 2]]
anotherList = [1, 2, 3, 4, 5]
yetAnotherList = [6, 6, 6] * 6 + [1, 1, 1]

fusionList = (aList + anotherList)

nestedList = aList[-1]

elementOfNestedList = aList[-1][0]  # same as nestedList[0]

anotherList[0] = "zero"  # lists, contrary to strings, are mutable
del anotherList[1:3]
print(anotherList)

evenNumberList = list(range(0, 201, 2))
oddNumberList = list(range(201, 0, -2))[::-1]


theList = [0, 1, 2, 3, 4, 5]
print(theList)  # [0, 1, 2, 3, 4, 5]

# add element to list
theList.append(6)
theList = theList + [7]
theList[len(theList):] = [8]
print(theList)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# concatenate two lists
theList.extend([9, 10, 11, 12])
theList = theList + [13, 14, 15, 16]
theList[len(theList):] = [17, 18, 19, 20]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(theList)

# inserts an object into the specified index
theList.insert(0, 'I\'m at the beginning! 8D')
print(theList)

# removes the first occurence of the specified value
theList.remove(3)
print(theList)

# removes the object from the end of the list
removedList = theList.pop()
print(theList)

# returns and removes the object at index 3
thirdElement = theList.pop(0)
print(theList)

# returns the number of elements in the list
len(theList)

# returns the number of occurences of the specified value
theList.count(4)

# returns the index at which the first occurence of the specified value is
theList.index(4)

# returns sorted list without changing the original one
theList = sorted(theList)

# can be passed a custom sorting function
theList.sort()
print(theList)

# returns reversed list without changing the original one
reversedList = reversed(theList)

# equivalent to theList = theList[::-1]
theList.reverse()
print(theList)

# erases all of the liss elements
theList.clear()
print(theList)  # []

# compreension Lists
squares = [x**2 for x in range(50)]

megaComprehensionList = [[x, y]
                         for x in [2, 3, 4] for y in [1, 2, 3] if x != y]

""" end of lists """

""" Tuples """
# tuple (id, name)
t = 201703123, "Some name"  # (201703123, "Some name")

print(t)
print(t[0])
print(t[::-1])  # indexing and slicing works as in lists

# empty the tuple
emptyTuple = ()
# notice the comma
singleTuple = "one is the loneliest number :'C",

# can't do this because, like strings, tuples are immutable
# t[0] = 3

singleTuple = [10, 20, 30],
print(singleTuple)  # ([10, 20, 30],)
# you can, however, manipulate the mutable contents of a tuple
singleTuple[-1][0] = 42  # the last element's first element is now 42
print(singleTuple)  # ([42, 20, 30],)

# tuple packing of heterogeneous values
t = 1, 2, "something", "number 9", [0, 1, 2, 3]

# tuple packing
coordinates = 0, 1, -3
# tuple unpacking - the number of variables must be the same on both sides
x, y, z = coordinates

""" end of Tuples """


""" Sets """

coolSet = {1, 2, 3, 4, 1, 2, 3, 4, 4, 4, 4}
anotherSet = set([1, 2, 3, 4, 1, 2, 3, 4])
yetAnotherSet = {x**3 for x in range(3, 70, 4)}

uniqueChars = set("supercalifragilisticexpialidocious")
otherUniqueChars = set("bibbidi bobbidi boo")

# set difference
print(uniqueChars - otherUniqueChars)
# set intersection
print(uniqueChars & otherUniqueChars)
# set union
print(uniqueChars | otherUniqueChars)
# set symetric difference
print(uniqueChars ^ otherUniqueChars)

""" end of Sets """


""" Dictionaries """

# keys must be unique and immutable
httpResponseCodes = {404: "Not found", 403: "Forbidden", 200: "OK",
                     201: "Created", 418: "I'm a teapot"}
print(httpResponseCodes[418])  # "I'm a teapot"

squareValues = {x: x**2 for x in range(101)}  # {0: 0, 1: 1, ..., 100: 10000}


print(list(httpResponseCodes.keys()))  # [404, 403, 200, 201, 418]
# [(404, 'Not found'), ..., (418, "I'm a teapot")]
print(list(httpResponseCodes.items()))

print("Available response codes: ")
for key, value in httpResponseCodes.items():
    print("{0} - {1}".format(key, value))

""" end of Dictionaries """
