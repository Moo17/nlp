import re
import regex

bbcPath = 'bbc_small.txt'




def load_corpus(fileName):
    text = open(fileName, encoding='utf-8').read().split()
    return text


bbc = load_corpus(bbcPath)


def countWords(wordList):
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict


bbc_count = countWords(bbc)

keys = ['في', 'إلى', 'على', 'من']
line = {x: bbc_count[x] for x in keys}
print(type(line))


sortedBbcPrepositions = sorted([(v, k) for k, v in line.items()], reverse=True)
print(sortedBbcPrepositions)
