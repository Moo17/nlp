# bbcPath = 'bbc_small.txt'


# def load_corpus(fileName):
#     text = open(fileName, encoding='utf-8').read().split()
#     return text
#
#
# bbc = load_corpus(bbcPath)
#

# def countWords(wordList):
#     wordDict = {}
#     for word in wordList:
#         if word in wordDict:
#             wordDict[word] += 1
#         else:
#             wordDict[word] = 1
#     return wordDict
#
#
# bbc_count = countWords(bbc)
#
# sortedBbcCount = sorted([(v, k) for k, v in bbc_count.items()], reverse=True)
# print(sortedBbcCount[:10])


# for k, v in list(bbc_count.items())[:10]:
#     print('key: {}\t   value: {}'.format(k, v))
#     print('value: {}\t key: {}'.format(v, k))
#     print('------------------------------------')

# al_count = 0
# for word in words:
#     if word.startswith("ي"):
#         al_count += 1
# al_count




