def analyseFile(filename):

    dictionary = {}
    wordCount = 0

    analysisFile = open(filename, 'r')

    for line in analysisFile:
        for word in line.split(" "):
            wordCount += 1
            if(word.strip(".,!?:;-_\n\t\"") in dictionary.keys()):
                dictionary[word.strip(".,!?:;-_\n\t\"")] += 1
            else:
                dictionary[word.strip(".,!?:;-_\n\t\"")] = 1

    #print(wordCount)
    #print(dictionary.items())

    analysisFile.close()

    resultFile = open("results.txt", "w")

    for k, v in dictionary.items():
        resultFile.write(k + ": " + str(v) + " occurences - " + str(v/wordCount) + "%\n")

    resultFile.close()

analyseFile('test.txt')
