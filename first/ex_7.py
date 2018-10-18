word = input("Please insert a word: ")

prefixes = []

for count in range(1, len(word) + 1):
    prefix = word[0:count]
    prefixes.append(prefix)
    print(prefix)

