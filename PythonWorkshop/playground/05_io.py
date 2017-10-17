"""The many styles of string formatting in python"""

# using concatenation. str is meant to give a user-friendly string representation of the object
print("1 + 1 = " + str(1 + 1))
# print("1 + 1 = " + repr(1+1)) #repr is the basically the same as str. It's meant to overriden on classes to give a interpreter-friendly string representation of the object
print("1 + 1 = {}".format(1 + 1))  # using the string's format method()
print("1 + 1 = %d" % (1 + 1))  # C-like

from math import pi
from math import e
print("pi = {1}\ne = {0}".format(e, pi))
print("pi = {1:.15f}\ne = {0:.15f}".format(e, pi))
print("pi = {pi:.15f}\ne = {nepper:.15f}".format(pi=pi, nepper=e))

""" end of string formatting """

#name = input("What's your name? ")
#print("Hello, {}!".format(name))

"""console Input"""
# input() is used for everything
number = input()
print(number)

string = str(input())
print(string)

myList = input().split(" ")
print(myList)

"""end ofconsole I/O"""


"""file I/O"""
# available modes: r, w, r+, a, rb, wb, rb+, ab
textFile = open("exampleFile.txt", "r", encoding="utf-8") # "utf-8" is useful for portugues chars
print(textFile.read())  # reads everythig
textFile.seek(0)  # goes back to the file start
print(textFile.read(15))  # "Hello, how are
textFile.seek(0)
print(textFile.readline())  # "Hello, how are you?"

textFile.seek(0)
for line in textFile:
    # optional argument end determines what the character at the end of a print will be. By default it is \n
    print(line, end="")

# should be closed afterwards to avoid wasting resources
textFile.close()

textFile = open("newTextFile.txt", "r+")
aTranscript = """\
As Ethel descended the wooden staircase with her two puppies in pursuit, her grandmother called from the living room.

"Ethel, dear! Dinner is ready!"

"I'm coming grandma!" she replied
"""
textFile.write(aTranscript)

textFile.seek(0)

print(textFile.read())

textFile.close()

""" end of file I/O """

""" Error handling """

try:
    10 / 0
except ZeroDivisionError:
    print("Please don't divide by zero. Computers don't enjoy that.")
finally:
    print("Whatever you did, we're out of here")


option = 0
while True:
    try:
        option = int(input("Choose an option"))
        break
    except ValueError:
        print("Please type in a number!")
    finally:
        print("You'll see me at the end of every loop")

""" end error handling """
