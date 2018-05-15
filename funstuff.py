#a number guessing game
from random import randint
random_number = randint(1, 10)
guesses_left = 3
while guesses_left >= 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  else:
    guesses_left -= 1
else:
  print("You lose.")

#letter removing loop
phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == "a":
    print("X"),
  else: 
    print(char),
print

#how to loop through dictionaries
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print("This dictionary has the value 10!")

#another example
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
  print(key)
  print(d[key])

#enumerate function enumerates the choices by putting index next to the list variable
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
  print(index + 1), item

#zip function combines two lists and allows to work through them at the same time
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    print(max(a, b))

#example of uses of lists in if/else statements with for
friends = ['John', 'Ellie', 'David', 'Martha', 'Duncan']
for f in friends:
  if f == 'Duncan':
    print(f + ' is not a friend!')
  else:
    print(f + ' is a friend')
