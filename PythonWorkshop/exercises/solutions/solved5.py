def analyseFile(filename):

    dictionary = {}
    wordCount = 0

    analysisFile = open(filename, 'r', encoding="utf-8")

    for line in analysisFile:
        for word in line.split(" "):
            wordCount += 1
            if(word.strip(".,!?:;-_\n\t\"") in dictionary.keys()):
                dictionary[word.strip(".,!?:;-_\n\t\"")] += 1
            else:
                dictionary[word.strip(".,!?:;-_\n\t\"")] = 1

    # print(wordCount)
    # print(dictionary.items())

    analysisFile.close()

    resultFile = open("exercise5.txt", "w", encoding="utf-8")
    resultFile.write("%s\n" % wordCount)
    for k, v in dictionary.items():
        resultFile.write(k + ": " + str(v) + " occurences - " +
                         str(v / wordCount) + "%\n")

    resultFile.close()


analyseFile('../test.txt')
