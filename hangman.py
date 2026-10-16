import time
import random

print("Welcome to Hangman Game")
name = input("Enter your name:")
print("Hello " + name + "! Best of Luck\n The game is about to start")
# time.sleep(1)
print("Let's play Hangman")

def main():
    global word, display, length, already_guessed, limit
    words_to_guess = ["january", "apple", "orange", "computer", "keyboard", "display"]
    word = random.choice(words_to_guess)
    length = len(word)
    print("Length: " + str(length) + "\nThis is a word: " + word)
    display = '_' * length
    already_guessed = []
    limit = 5
    hangman()

def play_loop():
    play_game = input("Do you want to play again? y=yes, n=no\n")
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print("Thanks for playing. We expect you back again.")
        exit()

def hangman():
    global display, word, already_guessed, limit
    guess = input("Enter your word:")
    guess = guess.strip()
    if len(guess) == 0 or len(guess) >= 2:
        print("Invalid input")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        print(index, already_guessed)
        word = word[:index] + '_' + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display)
    elif guess in already_guessed:
        print("Try another letter")
    else:
        limit -= 1
        if limit == 0:
            play_loop()
        print("Try again" + str(limit) + "remaining")
    
    if word == '_' * length:
        print("Congratulation")
        play_loop()
    else:
        hangman()

if __name__ == "__main__":
    main()