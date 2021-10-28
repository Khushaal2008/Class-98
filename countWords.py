def countWords():
    name = input("Enter a file name: ")
    words = 0
    fileOpen = open(name, 'r')
    for i in fileOpen:
        wordSplit = i.split()
        words = words + len(wordSplit)
        length = len(wordSplit)
        
    print(wordSplit)
    print("Length of the word:",length)
    print("Number of words:", words)
        
       #print(length)
countWords()
    
