import math

file = "training.txt"

fileContents = open(file, "r")

emails = []
for line in fileContents:
    emails.append(line[2:])
    # print(line)

print(len(emails))

train_x = emails[ : math.ceil(len(emails) * 0.8)]
test_x = emails[math.ceil(len(emails) * 0.8) : ]

print(len(train_x), len(test_x))

fileContents.seek(0)

labels = []
for line in fileContents:
    labels.append(int(line[0]))

train_y = labels[ : math.ceil(len(labels) * 0.8)]
test_y = labels[math.ceil(len(labels) * 0.8) : ]

# for word in wordList:
#     print(word)

spam_dictionary = {}
ham_dictionary = {}

for i in range(len(train_x)):
    wordList = train_x[i].split()
    if train_y[i] == 1:
        for word in wordList:
            if word in spam_dictionary.keys():
                spam_dictionary[word] += 1
            else:
                spam_dictionary[word] = 1
    else:
        for word in wordList:
            if word in ham_dictionary.keys():
                ham_dictionary[word] += 1
            else:
                ham_dictionary[word] = 1

print(ham_dictionary)


# train accuracy
correct = 0
for i in range(len(train_x)):
    wordList = train_x[i].split()

    spam_words = 0
    ham_words = 0
    for word in wordList:
        if word in spam_dictionary.keys():
            spam_words += 1
        if word in ham_dictionary.keys():
            ham_words += 1

    if spam_words >= ham_words:
        if train_y[i] == 1:
            correct += 1
    else:
        if train_y[i] == 0:
            correct += 1
        
print(correct)
print("train accuracy", correct / len(train_x))

# test accuracy
correct = 0
for i in range(len(test_x)):
    wordList = test_x[i].split()

    spam_words = 0
    ham_words = 0
    for word in wordList:
        if word in spam_dictionary.keys():
            spam_words += 1
        if word in ham_dictionary.keys():
            ham_words += 1
    # print(spam_words, ham_words)

    if spam_words >= ham_words:
        if test_y[i] == 1:
            correct += 1
    else:
        if test_y[i] == 0:
            correct += 1
        
print(correct)
print("test accuracy", correct / len(test_x))