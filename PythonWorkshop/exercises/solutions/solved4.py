from math import sqrt

currPosition = [0, 0]

directions = open("directions.txt", "r")

for dir in directions:
    dirList = dir.split(" ")
    if(dirList[0] == "UP"):
        currPosition[1] += int(dirList[1])
    elif(dirList[0] == "DOWN"):
        currPosition[1] -= int(dirList[1])
    elif(dirList[0] == "LEFT"):
        currPosition[0] -= int(dirList[1])
    elif(dirList[0] == "RIGHT"):
        currPosition[0] += int(dirList[1])

print(int(sqrt(currPosition[0]**2 + currPosition[1]**2)))

directions.close()
