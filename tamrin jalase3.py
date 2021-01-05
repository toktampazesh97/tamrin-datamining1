from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from multi_rake import Rake
import math
from collections import Counter


def Read(path):
    file = open(path , "r")
    text=file.read()
    return text

def Sentence():
    for i in range(1, 11):
        arr = nltk.sent_tokenize(Read(f"data/{i}.txt"))
    return arr


def WordTok(text):
    arr = text.split(" ")
    return arr


def Remove(text):
    arr = []
    for i in range(0, len(text)):
        if (text[i] != "stop" and len(text[i]) != 1 and len(text[i]) != 0):
            arr.append(text[i])
    return arr


def Stem(text):
    arr = []
    for i in range(0, len(text)):
        arr.append(PorterStemmer().stem(text[i]))
    return arr


def ResultTok():
    arr = Sentence()
    all = []
    for i in range(0, len(arr)):
        txt = list(arr[i])
        text = ""
        for i in range(0, len(txt)):
           if 64 < ord(txt[i]) or ord(txt[i]) < 48 and txt[i] != '<' and txt[i] != '>':
             text += txt[i]
        text = WordTok(text)
        text = Remove(text)
        text = Stem(text)
        all.append(text)
    return all



def ResultWordCloude(path):
    text = open(path).read()

    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def Find(text):
    rake = Rake()
    keywords = rake.apply(text)
    return (keywords[:10])

def ResultWords():
    arr=[]
    for i in range(1 , 11):
        path = f"data/{i}.txt"
        text = Read(path)
        arr.append(Find(text))
    return arr

def eta(data, unit='natural'):
    base = {
        'shannon' : 2.,
        'natural' : math.exp(1),
        'hartley' : 10.
    }

    if len(data) <= 1:
        return 0

    counts = Counter()

    for d in data:
        counts[d] += 1

    ent = 0

    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent

def ResultMatrix():
    text = ResultTok()
    arr=[]
    n=[]

    for i in range(0 , 10):
        for j in range(0 , len(text[i])):
            pl=Exists(arr , text[i][j])
            if(Exists(arr , text[i][j])):
                n[Exists(arr , text[i][j])]=f"{1+int(n[Exists(arr , text[i][j])])}"
            else:
                arr.append(text[i][j])
                n.append(1)
        print(f"\nFile{i+1}")
        for i in range(0 , len(arr)):
            print(f"{arr[i]}  {n[i]}")
        arr=[]
        n=[]

def Exists(a , word):
    for i in range(0 , len(a)):
        if(a[i]==word):
            return i;
    return False;

arr=ResultTok()
print("پیش پردازش")
for i in range(0, 10):
    print(arr[i])
print("----------------------------------------------------------------------------")
arr = ResultWords()
print("فراوانی تعداد کلمات کلیدی")
for i in range(0 , 10):
    print(arr[i])
print("------------------------------------------------------------------------------")

a=[]
b=[]
print("آنتروپی")
for i in range(0 , 10):
    for j in range(0 , len(arr[i])):
        b = arr[i][j][0].split(" ");
        for k in range(0 , len(b)):
            a.append(b[k])
    print(eta(a))
    a=[]
print("-------------------------------------------------------------------------------")
for i in range(1 , 11):
    ResultWordCloude(f"data/{i}.txt")

ResultMatrix()