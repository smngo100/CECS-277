# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 2/6/2024
# Description: This program, 'Hangman', randomly selects a 5-letter word from the dictionary file to use. The user then has 6 guesses to guess the word.

import random
from dictionary import words
import check_input


# Displays stages of gallows
def display_gallows(num_incorrect):
    stages = [
        """
        ========
        | |/  |
        | |   
        | |   
        | |  
        """,
        """
        ========
        | |/  |
        | |   o
        | |   
        | |  
        """,
        """
        ========
        | |/  |
        | |   o
        | |   |
        | |  
        """,
        """
        ========
        | |/  |
        | |   o
        | |   |
        | |  / 
        """,
        """
        ========
        | |/  |
        | |   o
        | |   |
        | |  / \\
        """,
        """
        ========
        | |/  |
        | |  \o
        | |   |
        | |  / \\
        """,
        """
        ========
        | |/  |
        | |  \o/
        | |   |
        | |  / \\
        """ ]
    print(stages[num_incorrect])


# Joins the letters in the gallows into a string
def display_letters(letters):
    print(" ".join(letters))
  
# Displays remaining letters that have not been guessed
def get_letters_remaining(incorrect, correct):
    remaining = [] 
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      if letter not in incorrect and letter not in correct:
        remaining.append(letter)
    return remaining

# User gusses 5 letters for a word. If they guess correctly, they win. If they guess incorrectly, they lose. The game loops until the user decides to quit.
def main():
    play_again = True
    while play_again:
        word = random.choice(words)
        correct_guesses = ['_'] * 5
        incorrect_guesses = []
        num_correct = 0
        num_incorrect = 0

        print("-Hangman-")

        while num_incorrect != 6 and num_correct != 5:
            print("\nIncorrect selections:", end=" ")
            display_letters(incorrect_guesses)
            display_gallows(num_incorrect)
            print(" ".join(correct_guesses) + "\n")
            print("Letters remaining:", end=" ")
            letters_remaining = get_letters_remaining(incorrect_guesses, correct_guesses)
            display_letters(letters_remaining)

            guess = input("\nEnter a letter: ").upper()
            if guess in incorrect_guesses or guess in correct_guesses:
                print("You have already used that letter.")
                continue
            elif guess in word:
                print("Correct!")  
                for i, letter in enumerate(word):
                    if letter == guess:
                        correct_guesses[i] = guess
                        num_correct += 1
            else:
                print("Incorrect!")
                incorrect_guesses.append(guess)
                num_incorrect += 1

      
        display_gallows(num_incorrect)
        display_letters(correct_guesses)
        if num_incorrect == 6:
          print("\nYou lose.")
          print("\nThe word is: " + word)
          play_again = check_input.get_yes_no("\nPlay again (Y/N)? ")
          
        else:
          print("\nYou win!")
          play_again = check_input.get_yes_no("Play again (Y/N)? ")


if __name__ == "__main__":
    main()
