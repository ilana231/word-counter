def countWordsFromFile():
    #fileName = input("enter the file name: ")
    fileName = "./temp.txt"
    print(fileName)
    numberOfWords = 0

    file = open(fileName,"r")

    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)

    print(numberOfWords)

countWordsFromFile()