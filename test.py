words = []
word_set = []
count = 0

number_of_words = int(input())

for i in range(number_of_words):
    word = input()
    words.append(word)

for x in words:
    if x in word_set:
        pass
    else:
        word_set.append(x)

print(word_set)
print(words)
print(len(word_set))


for w in word_set:
    for i in range(number_of_words):
        if w != words[i]:
            pass
        else:
            count += 1
    print(count,end="")
    count = 0
