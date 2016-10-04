import nltk

def read_file():
    read = fopen("example.txt", "r")
    return read

text = read_file()

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text.read())
