import string 

phrase = input("Please insert a phrase: ")
new_phrase = ""

for character in phrase:
    if character in string.ascii_letters or character in "-' ":
        new_phrase += character

list_of_words = new_phrase.split(" ")

print("The phrase you inserted is made of {} words. These are: ".format(len(list_of_words)))

for word in list_of_words:
    print(word)

    