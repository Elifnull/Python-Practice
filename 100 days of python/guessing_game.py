print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

import random
from replit import clear
def number_guess():
  number = random.randint(1,100)
  player_lives = 0
  
  level_difficulty = input("What difficulty do you want? 'easy' or 'hard'?\n").lower()
  
  if level_difficulty == "hard":
    player_lives = 5
  else: 
    player_lives = 10
  
  is_game_done = False
  
  while not is_game_done:
    if player_lives < 0:
      is_game_done = True
      print("You've no more guesses")
    print(f"You have {player_lives} attempts to guess!")
    guess = int(input("Make a guess:\n"))
    if guess == number:
      is_game_done = True
      print(f"You've guessed correct, the number is {number}")
    elif guess > number:
      player_lives -= 1
      print(f"{guess} is too high!")
    elif guess < number:
      player_lives -= 1
      print(f'{guess} is too low!')
  replay_state = input("do you want to play again? 'Y' or 'N'\n").lower()
  if replay_state == 'y':
    clear()
    number_guess()
  else:
    clear()
number_guess()