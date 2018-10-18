string = input('Insert the text you want to evaluate: ')

character = input('What character do you want to count in the string? ')

print("The character '{}' shows up {} times in the '{}' string.".format(character, string.count(character), string))
