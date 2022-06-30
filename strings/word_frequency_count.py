input = [" The", "dog", "jumped", "in", "the", "dog", "house"]
target_word = 'dog'

count = 0
words = {}
answer = ""

for i in input:
    if len(input) > 0:
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1

for key, value in words.items():
    if value > count:
        answer = key

print(" Most frequently appearing target word is", answer)
print("Target word is ", words[target_word])
