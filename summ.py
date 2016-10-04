import nltk

def read_file():
    read = open("example.txt", "r")
    return read

text = read_file()

#getting the tokens without pontuation
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text.read())

#removing the stopwords and generating a list with most common words
stopwords = nltk.corpus.stopwords.words("portuguese")
freq2 = nltk.FreqDist(w for w in tokens if w not in stopwords)
commons = freq2.most_common(1000)

#generating a list with the five (or more) more common words
usefull_list = []
i = 0
for n in commons:
    usefull_list.append(n[0])
    i += 1
    if i == 5: break
