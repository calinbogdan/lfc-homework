alphabet = input("Please insert all the letters from the alphabet: ")
word = input("Please insert the word you want to check: ")

word_is_in_alphabet = True

for letter in word:
    if letter not in alphabet:
       word_is_in_alphabet = False
       break 


if word_is_in_alphabet:
    print("Yay! Your word is there.")
else:
    print(":(. Maybe next time?")