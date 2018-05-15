# this is a script for age verification with 2 possible variables
def verification(age):
# this command transferes the age into an integer number, python takes input() as a string at first
    age = int(age)
    if age < 18 and age >= 16:
        print("Welcome.")
    elif age < 16:
        print("You're too young. Come back in " + str(16 - age) + " years.")
    else:
        print("You're too old to be using this app.")

def how_old():
    age = input("In order to use this app you need to be younger than 18 but older than 16 years old. Your age: ")
# this command makes sure that the age is specified using numbers, as in integers
    if age.isalpha():
        print("Please use digits to write your age.")
        return how_old()
    else:
        verification(age)

how_old()
