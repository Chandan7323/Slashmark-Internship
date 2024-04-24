Number Guessing Game

This Python application offers a fun and engaging number guessing experience. Test your skills against the computer, which will pick a random number between 1 and 200. You'll have 6 attempts to guess the correct number!

Features:
*Clear instructions: The program guides you through the gameplay.
*User-friendly interface: Interact with the game by entering your name and guesses.
*Informative feedback: Receive hints about whether your guess is too high, too low, or correct.
*Multiple rounds: Play as many rounds as you like!

How to Play:
1.The program will ask for your name.
2.You'll be informed that the computer has chosen a number between 1 and 200.
3.Enter your guesses one at a time.
4.The program will provide feedback on each guess, indicating if it's too high, too low, or correct.
5.You have a maximum of 6 attempts.
6.If you guess the number correctly, you'll be congratulated! Otherwise, the computer will reveal the secret number.
7.The program will ask if you'd like to play another round.

# In[ ]:


import random
import time

def main():
  """
  Runs the number guessing game.
  """
  number = random.randint(1, 200)  # Pick a random number
  name = get_player_name()
  play_game(name, number)
  play_again = get_play_again_choice()
  while play_again.lower() in ("yes", "y"):
    name = get_player_name()
    number = random.randint(1, 200)  # Pick a new random number
    play_game(name, number)
    play_again = get_play_again_choice()

def get_player_name():
  """
  Asks the player for their name and returns it.
  """
  print("May I ask you for your name?")
  name = input()
  return name

def play_game(name, number):
  """
  Manages the guessing process for a single game.
  """
  print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
  time.sleep(0.5)
  print("Go ahead. Guess!")
  guesses_taken = 0
  while guesses_taken < 6:
    guess_str = input("Guess: ")
    try:
      guess = int(guess_str)
      if 1 <= guess <= 200:
        guesses_taken += 1
        if guesses_taken < 6:
          if guess < number:
            print("Your guess is too low.")
          elif guess > number:
            print("Your guess is too high.")
          else:
            break
          print("Try again!")
      else:
        print("Silly Goose! That number isn't in the range!")
        print("Please enter a number between 1 and 200")
    except ValueError:
      print(f"I don't think '{guess_str}' is a number. Sorry.")
  if guess == number:
    guesses_taken_str = str(guesses_taken)
    print(f'Good job, {name}! You guessed my number in {guesses_taken_str} guesses!')
  else:
    print(f'Nope. The number I was thinking of was {number}')

def get_play_again_choice():
  """
  Asks the player if they want to play again and returns their choice.
  """
  print("Do you want to play again?")
  play_again = input()
  return play_again

if __name__ == "__main__":
  main()

