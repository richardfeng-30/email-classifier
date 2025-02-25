file = "demo text.txt"

# r is for reading file (vs writing)
fileContents = open(file, "r")

emails = []
for line in fileContents:
    emails.append(line[2:])
    # print(line)

fileContents.seek(0)

labels = []
for line in fileContents:
    labels.append(int(line[0]))


print("iteration 2")
for line in fileContents:
    print(line)

# seek() resets the cursor for a file if you need to go through it again
fileContents.seek(0)

# print("iteration 3")
# for line in fileContents:
#     print(line)

# iterate through each email
# for email in emails:
#     print(email)

# save each word in email 0 to wordList
wordList = emails[0].split()

# for word in wordList:
#     print(word)

# create a dictionary
dictionary = {}
# dictionary["banana"] = 1
# dictionary["banana"] += 5

# print(dictionary["banana"])

# dictionary["shoe"] = 0
# print(dictionary)

# if "chicken" in dictionary.keys():
#     dictionary["chicken"] += 10
# else:
#     dictionary["chicken"] = 4

# del dictionary["chicken"]

# print(len(dictionary))

spam_dictionary = {}
ham_dictionary = {}

for i in range(len(emails)):
    wordList = emails[i].split()
    if labels[i] == 1:
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

# print(ham_dictionary)

# test
wordList = emails[0].split()

spam_words = 0
ham_words = 0
for word in wordList:
    if word in spam_dictionary.keys():
        spam_words += 1
    elif word in ham_dictionary.keys():
        ham_words += 1

print(spam_words, ham_words)