import nltk

def read_file():
    read = fopen("example.txt", "r")
    return read

text = read_file()

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text.read())


stopwords = nltk.corpus.stopwords.words("portuguese")
freq2 = nltk.FreqDist(w for w in tokens if w not in stopwords)
print(freq2.most_common(1000))
