import random

print("Welcome to hangman!")

word = ["hacker", "bounty", "random"]

# Ask user for one letter
guess = input("Guess a letter: ").lower()

#random
words = random.choice(word)
# Loop through each word in the list
for word in words:
 #   print(f"\nChecking word: {word}")
    for letter in word:
        if letter == guess:
            print("Right")
        else:
            print("Wrong")
