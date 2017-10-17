# all arguments after one with a default value must also have a default argument
def aFunction(arg0, arg1, arg2="DefaultValue"):
    print(arg0, arg1, arg2)


aFunction("value", "value1")
aFunction("value", "anotherValue", "yetAnotherValue")
aFunction("val", "value", arg2="lots of values")
aFunction("value", arg1="value")
aFunction("value", arg2="val", arg1="val1")
# if the call doesn't respect the positional argument order then all arguments after the first must be keyword arguments
aFunction(arg0="so many values", arg2="lots of values",
          arg1="even more values")
#this is invalid!!
aFunction(arg1="val", "value", arg3="val1")


defaultOption = 3
def startMenu(option=defaultOption):
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        print("Three")
    elif option == 4:
        print("Four")

startMenu() # Three
defaultOption = 4
startMenu() # Also Three!!!


def isOdd(number):
    """I'm a docstring!"""
    if number % 2 != 0:
        return True
    return False


""" LAMBDAS """

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2


# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )

# hardcore example
nums = range(1, 51)
print(list(nums))
for i in range(2, 8):
	#filter from nums those that match i + 1 or that are multiple of i
	filtered = filter(lambda x: x == i + 1 or x % i == 0, nums)
	print("i: %d     -> %s" % (i, list(filtered)))

""" end of LAMBDAS """