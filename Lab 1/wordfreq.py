def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            
            if line[start].isspace():
                while line[start].isspace():
                    start += 1
                    if start == len(line):
                        return words
            
            end = start
            if line[end].isalpha():
                while line[end].isalpha():
                    end += 1
                    if end == len(line):
                        break


                word = line[start:end].lower()
                words.append(word)
                end = end - 1

            elif line[end].isdigit():
                while line[end].isdigit():
                    end += 1
                    if end == len(line):
                        break

                word = line[start:end]
                words.append(word)
                end = end - 1
                

            else:
                word = line[end]
                words.append(word)
            
            start = end + 1
    return words

def isWordInStopWords(word, stopWords):
    for stopWord in stopWords:
        if word == stopWord:
            return True

    return False

def isWordInDict(word, Dict):
    for dictWord in Dict:
        if word == dictWord:
            return True

    return False

def countWords(words, stopWords):
    resDict = {}
    for word in words:
        if isWordInStopWords(word, stopWords) == False and isWordInDict(word, resDict) == False:
            resDict[word] = 1
        elif isWordInStopWords(word, stopWords) == False and isWordInDict(word, resDict) == True:
            number = resDict.get(word)  
            resDict[word] = number + 1
    return resDict

def printTopMost(frequencies,n):
    retFreq = []
    for word,freq in frequencies.items():
        retFreq.append((word.ljust(20), freq))

    retFreq = sorted(retFreq, key=lambda x: -x[1])
    
    retFreq = retFreq[0:n]

    for things in retFreq:
        print(things[0] + str(things[1]).rjust(5))
