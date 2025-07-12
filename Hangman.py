import random

print("🎮 Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
word = random.choice(words)

guessed = "_" * len(word)
tries = 6

while tries > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Tries left:", tries)

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("✅ Correct!")
        # Reveal correct letters
        new_guessed = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_guessed += guess
            else:
                new_guessed += guessed[i]
        guessed = new_guessed
    else:
        print("❌ Wrong!")
        tries -= 1

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
