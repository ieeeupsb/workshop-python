
''' IF STATEMENTS'''

x = 10
if(x < 0):  # parenthesis are optional
    print("smaller than zero")  # indentation is required
elif(x == 0):  # else if
    # commands can be written in the same line as long as they are separated by ;
    print("zerooooooo")
    print("oooooooooo")
else:
    print("bigger than", 0)
    print("I'm still within the else clause!")

print("They kicked me out of the clause :'(")

''' FOR STATEMENTS'''

IWantYouBack = ["ABC", "It's easy as 1 2 3", "As simple as do re mi"]

for i in IWantYouBack:
    print(i, len(i))

# bad idea to insert/remove things on the iterable you are iterating through, so we make a copy
for i in IWantYouBack[:]:
    IWantYouBack.insert(0, "I want you back")

for i in range(5):  # i = 0, 1, 2, 3, 4 -> [0, 5[
    print(i)

for i in range(10, 50, 10):  # i = 10, 20, 30, 40
    print(i)


# strange concatenation example
people = ["Person"] * 3 + ["Killer"] + ["Not"] * 2
print(people)  # ['Person', 'Person', 'Person', 'Killer', 'Not', 'Not']

for p in people:
    if(p == "Killer"):
        print("Found the killer!")
        break  # exits the loop
    else:  # useless in this case, just wanted to show off the continue statement
        continue
else:  # this branch runs when no break happens in the for loop
    print("No killer was found")


# enumerate returns the index and the value
for i, v in enumerate(people):
    if(v == "Killer"):
        print("Found the killer at position {0}".format(i))
        #print("Found the killer at position %d" % i)
        break
else:
    print("No killer was found")

''' WHILE STATEMENTS'''

from random import randrange

bird = "duck"
while bird != "goose":
    print("waiting...")
    if(randrange(0, 101) < 30):
        bird = "goose"
print("I'm a goose!")

from random import randrange
i = 0
while i < 100:
    i += randrange(0, 8)
    if i % 10 == 0:
        print("multiple of 10: %d" % i)
        break
else:
    print("No multiple of 10...")
