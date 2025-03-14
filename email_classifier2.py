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

dictionary = {}

for i in range(len(train_x)):
    wordList = train_x[i].split()
    if train_y[i] == 1:
        for word in wordList:
            if word in dictionary.keys():
                dictionary[word] += 1 / len(wordList)
            else:
                dictionary[word] = 1 / len(wordList)
    else:
        for word in wordList:
            if word in dictionary.keys():
                dictionary[word] -= 1 / len(wordList)
            else:
                dictionary[word] = -1 / len(wordList)

# train accuracy
print("train accuracy:")
accuracy = 0
last_accuracy = -1
i = 0
learning_rate = 20
while abs(accuracy - last_accuracy) > 0.0005:
    correct = 0
    last_accuracy = accuracy
    for j in range(len(train_x)):
        wordList = train_x[j].split()
        score = 0
        for word in wordList:
            if word in dictionary.keys():
                score += dictionary[word]
        if score >= 0:
            if train_y[j] == 1:
                correct += 1
            else:
                for word in wordList:
                    dictionary[word] -= learning_rate / len(wordList)
        else:
            if train_y[j] == 0:
                correct += 1
            else:
                for word in wordList:
                    dictionary[word] += learning_rate / len(wordList)
    accuracy = correct / len(train_x)
    print("pass", i + 1, "- accuracy", accuracy)
    i += 1
    learning_rate = 20 * (0.9 ** i)

# validation
correct = 0
for i in range(len(test_x)):
    wordList = test_x[i].split()

    score = 0
    for word in wordList:
        if word in dictionary.keys():
            score += dictionary[word]

    if score >= 0:
        if test_y[i] == 1:
            correct += 1
    else:
        if test_y[i] == 0:
            correct += 1
        
print()
print("validation accuracy")
print(correct / len(test_x))