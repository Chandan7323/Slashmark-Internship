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
