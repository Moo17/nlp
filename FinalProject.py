import regex
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tkinter import *

top = Tk()
top.title("Final Project -NLP-")
top.minsize(500, 500)


russiaFile = 'russia.txt'
ukraineFile = 'Ukraine.txt'
footballFile = 'football.txt'


def load_corpus(fileName):
    text = open(fileName, encoding='utf-8').read().split()
    return text


russia = load_corpus(russiaFile)
ukraine = load_corpus(ukraineFile)
football = load_corpus(footballFile)


# print(russia[:10])

# Function filling the dictionary
def countWords(wordList):
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1  # update becuase key is exist
        else:
            wordDict[word] = 1  # adding becuase key is not exist
    return wordDict


# Creating a dictionary for each corpus by calling countWords function
russia_count = countWords(russia)
ukraine_count = countWords(ukraine)
football_count = countWords(football)

print("------------------------------Question 2---------------------------------------")


def MostLeastFreq():
    print("------------------------------------------------------------")
    print("the Most frequent of characters in Russia File :")
    sortedRussiaCountMost = sorted([(v, k) for k, v in russia_count.items()], reverse=True)
    print(sortedRussiaCountMost[:10])
    print("the Least frequent of characters in Russia File :")
    sortedRussiaCountLeast = sorted([(v, k) for k, v in russia_count.items()], reverse=False)
    print(sortedRussiaCountLeast[:10])
    print("------------------------------------------------------------")
    print("the Most frequent of characters in Ukraine File :")
    sortedUkraineCountMost = sorted([(v, k) for k, v in ukraine_count.items()], reverse=True)
    print(sortedUkraineCountMost[:10])
    print("the Least frequent of characters in Ukraine File :")
    sortedUkraineCountLeast = sorted([(v, k) for k, v in ukraine_count.items()], reverse=False)
    print(sortedUkraineCountLeast[:10])
    print("------------------------------------------------------------")
    print("the Most frequent of characters in Football File :")
    sortedFootballCountMost = sorted([(v, k) for k, v in football_count.items()], reverse=True)
    print(sortedFootballCountMost[:10])
    print("the Least frequent of characters in Football File :")
    sortedFootballCountLeast = sorted([(v, k) for k, v in football_count.items()], reverse=False)
    print(sortedFootballCountLeast[:10])
    print("------------------------------------------------------------")


# def buClick():
#     print(MostLeastFreq.get())
#     MostLeastFreq.delete(0, END)

butt = Button(text="Find the Most and Least Frequent ", command=MostLeastFreq, bg='green')
butt.pack()
butt.place(x=150, y=50)
# res = MostLeastFreq()
# resultLabel = Label(text="The result :: " + str(res))
# resultLabel.pack()


print("------------------------------Question 3---------------------------------------")


# Normalization = regex.sub(r"([_.؟!])", r" \1 ", news)
# Normalization.split().count('ukraine')

def Max():
    print("------------------------------------------------------------")
    print('Number of tokens at Russia File is :: ', len(russia), '\nNumber of vocabularies at Russia File is :: ',
          len(set(russia)))
    print("------------------------------------------------------------")
    print('Number of tokens at Ukraine File is :: ', len(ukraine), '\nNumber of vocabularies at Ukraine File is :: ',
          len(set(ukraine)))
    print("------------------------------------------------------------")
    print('Number of tokens at Football File is :: ', len(football), '\nNumber of vocabularies at Football File is :: ',
          len(set(football)))
    print("------------------------------------------------------------")
    MAX = max(len(russia), len(ukraine), len(football))
    print("The Most one that is linguistically rich in chars and words is :::  ", MAX)
    print("------------------------------------------------------------")
    # resultLabel = Label(text="The Most one that is linguistically rich in chars and words is ::: " + str(Max))
    # resultLabel.pack()


butt = Button(text="Find the Most one that is linguistically rich in chars and words ", command=Max, bg='green')
butt.pack()
butt.place(x=100, y=100)
print("------------------------------Question 4---------------------------------------")

print("--------------------- Stemming -------------------------------")


def stemmer():
    stemmer = PorterStemmer()

    string_for_stemming = """
    ... Ukraine foreign minister discussed arms supply and EU status with Dutch counterpart
    ... Ukraine's Foreign Minister Dmytro Kuleba discussed arms supplies, new sanctions 
    ... against Russia and granting Ukraine European Union candidate status during a meeting with his Dutch counterpart 
    ... Wopke Hoekstra in The Hague on Tuesday,
    ... "Met with my colleague and friend Wopke Hoekstra at the beginning of my visit to The Hague. Commended him and the 
    ... Dutch government for their efforts to defend peace in Ukraine and Europe. We focused on further arms supplies, 
    ... new sanctions on Russia, and Ukraine’s EU candidate status," Kuleba said. Putin: Some European countries cannot "give up" on Russian oil. """

    words = word_tokenize(string_for_stemming)
    print("The Separate Words :: ", words)

    stemmed_words = [stemmer.stem(word) for word in words]
    print("The Stemmed Words :: ", stemmed_words)
    print("--------------------- Stemming -------------------------------")


butt = Button(text="Find The Stemmer ", command=stemmer, bg='green')
butt.pack()
butt.place(x=190, y=150)

print("---------------------------------------------------------------")
print("-------------------- Lemmatization ----------------------------")


def lemmatizer():
    lemmatizer = WordNetLemmatizer()

    string_for_lemmatizing = """
    ... Ukraine foreign minister discussed arms supply and EU status with Dutch counterpart
    ... Ukraine's Foreign Minister Dmytro Kuleba discussed arms supplies, new sanctions 
    ... against Russia and granting Ukraine European Union candidate status during a meeting with his Dutch counterpart 
    ... Wopke Hoekstra in The Hague on Tuesday,
    ... "Met with my colleague and friend Wopke Hoekstra at the beginning of my visit to The Hague. Commended him and the 
    ... Dutch government for their efforts to defend peace in Ukraine and Europe. We focused on further arms supplies, 
    ... new sanctions on Russia, and Ukraine’s EU candidate status," Kuleba said. Putin: Some European countries cannot "give up" on Russian oil. """

    words = word_tokenize(string_for_lemmatizing)
    print("The Separate Words :: ", words)

    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    print("The Lemmatized Words :: ", lemmatized_words)
    print("-------------------- Lemmatization ----------------------------")


butt = Button(text="Find The lemmatizer ", command=lemmatizer, bg='green')
butt.pack()
butt.place(x=180, y=200)

top.mainloop()
