file = open("document", "r")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for key, value in wordcount.items():
    print(key, value)
