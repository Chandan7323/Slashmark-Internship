Number Guessing Game

This Python code implements a fun and challenging number guessing game. The computer picks a random number between 1 and 200, and you have 6 chances to guess it correctly.

*How to Play:*
1.Clone or download the repository.
2.Open a terminal or command prompt and navigate to the directory containing the code (number_guessing_game.py).
3.Run the script using python number_guessing_game.py.
4.Follow the on-screen prompts to enter your name and guess the number.
5.After each guess, you'll receive feedback on whether it's too low, too high, or correct.
6.The game will continue until you guess the number or run out of guesses.
7.You'll be asked if you want to play again after each round.

Feel free to play and have fun!



import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()  # Ask for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)

def pick():
    number = random.randint(1, 200)
    max_guesses = 6
    guesses_taken = 0

    while guesses_taken < max_guesses:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < number:
                    print("The guess of the number that you have entered is too low")
                elif guess > number:
                    print("The guess of the number that you have entered is too high")
                else:
                    print(f"Congratulations! You guessed the number in {guesses_taken} guesses!")
                    return
            else:
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Sorry, you ran out of guesses. The number I was thinking of was {number}.")

def play_game():
    intro()
    pick()
    return input("Do you want to play again? (yes/no): ").lower().strip() in ["yes", "y"]

def main():
    play_again = True
    while play_again:
        play_again = play_game()

if __name__ == "__main__":
    main()
