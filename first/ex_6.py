def get_words():
    number_of_words = int(input("Number of words you want to insert: "))

    words = []

    for word_number in range(1, number_of_words + 1):
        word = input("Word #{}: ".format(word_number))
        words.append(word)

    return words

def first_option():
    words = sorted(get_words())

    for word in words:
        print(word)

def second_option():
    print("Type PRINT to stop adding words.")
    read_and_print_reverse()

def read_and_print_reverse():
    word = input("Word: ")
    if word == "PRINT":
        pass
    else:
        read_and_print_reverse()
        print(word)

def main():
    print("1. Insert words and get them ordered")
    print("2. Insert words and get them in inversed order")

    option = int(input("Pick the option you want: "))

    if option == 1:
        first_option()
    elif option == 2:
        second_option()
    else:
        print("The option you picked isn't valid.")
    
main()