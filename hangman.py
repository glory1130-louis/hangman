import time
import random

print("Welcome to Hangman Game")
name = input("Enter your name:")
print("Hello " + name + "! Best of Luck")
print("The game is about to start\n")
# time.sleep(1)
print("Let's play Hangman")

def main():
    global word, display
    words_to_guess = ["january", "apple", "orange", "computer", "keyboard", "display"]
    word = random.choice(words_to_guess)
    length = len(word)
    display = '_' * length

def play_loop():
    play_game = input("Do you want to play again? y=yes, n=no")
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print("Thanks for playing. We expect you back again.")
        exit()

def hangman():
    global display, word, already_guessed
    guess = input("This is a word: " + word + display + "\n Enter your word:")
    guess = guess.strip()
    already_guessed = []
    limit = 5
    if len(guess) == 0 or len(guess) >= 2:
        print("Invalid input")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        display = display[:index] + '_' + display[index+1:]
        print(display)
    elif guess in already_guessed:
        print("Try another letter")
    else:
        limit -= 1
        if limit == 0:
            play_loop()
        hangman()
        print("Try again" + str(limit) + "remaining")

if __name__ == "__main__":
    main()

hangman()