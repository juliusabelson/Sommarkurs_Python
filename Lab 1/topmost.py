import wordfreq
import urllib.request
import sys


def main():
    stopwordsdir = open(sys.argv[1])

    wordsfiledir = sys.argv[2]

    if wordsfiledir [0:6] == "http://" or wordsfiledir [0:7] == "https://":
        response = urllib.request.urlopen(wordsfiledir)
        wordsfiledir = response.read().decode("utf8").splitlines()

    else:
        wordsfiledir = open(sys.argv[2])

    n = sys.argv[3]
    
    words = []
    for word in wordsfiledir:
        words.append(word)
    
    toknedWords = wordfreq.tokenize(words)

    words = []
    for word in stopwordsdir:
        words.append(word.strip('\n'))
    
    stopWords = words

    countedWords = wordfreq.countWords(toknedWords, stopWords)

    topWords = wordfreq.printTopMost(countedWords, n)

    print(topWords)



main()
