first_word = input("First word: ")
second_word = input("Second word: ")

if first_word[-2:] == second_word[-2:]:
    print("Congrats! The two words you inserted are rhyming.")
else:
    print("Bummer! The two words you inserted aren't rhyming. Sadly.")