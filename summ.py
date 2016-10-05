import nltk

def read_file():
    read = open("example.txt", "r")
    return read

text = read_file().read()

#getting the tokens without pontuation
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

#removing the stopwords and generating a list with most common words
stopwords = nltk.corpus.stopwords.words("portuguese")
freq2 = nltk.FreqDist(w for w in tokens if w not in stopwords)
commons = freq2.most_common(1000)

sentence_regex = "([A-Z][^\.!?]*[\.!?])"


# #generating a list with the five (or more) more common words
# usefull_list = []
# i = 0
# for n in commons:
#     usefull_list.append(n[0])
#     i += 1
#     if i == 5: break

# #print(usefull_list)


# #generating a list with the sentences that the more common words appears
# expressions = []
# for n in usefull_list:
#     regex = '[\w," ]+' + n + '[\w," ]+\.'
#     tokenizer = nltk.tokenize.RegexpTokenizer(regex)
#     tokens = tokenizer.tokenize(text)
#     for i in tokens: expressions.append(i)

# #excluding repeated expressions
# def exclude_repeated_sentences(sentences):
#     not_repeated = []
#     not_repeated.append(expressions[0])
#     flag = 1

#     for n in sentences:
#         for i in not_repeated:
#             if n == i: flag = 0
#         if flag: not_repeated.append(n)
#         else: flag = 1

#     return not_repeated


# for i in exclude_repeated_sentences(expressions):
#     print(i + "\n")
