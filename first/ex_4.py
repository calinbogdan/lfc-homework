phrase = input("Please insert a phrase: ")

str1 = input("Insert the string you want to replace in the phrase: ")
str2 = input("Insert the string you want to replace it with: ")

phrase = phrase[::-1]

phrase = phrase.replace(str1, str2)

print("The result phrase is: {}".format(phrase))