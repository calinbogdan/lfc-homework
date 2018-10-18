number = input("Please insert a number: ")

try:
    number = float(number)    
    if int(number) == number:
        if number < 0:
            print("The number {} is an integer.".format(number))
        else: 
            print("The number {} is a natural number.".format(number))
    else:
        print("The number {} is a real number.".format(number))
except ValueError:
    print("The number {} is invalid.".format(number))