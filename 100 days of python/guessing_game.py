#Number Guessing Game Objectives:
import random
from replit import clear
from art import logo




def number_guess():
  print(logo)
  print("I'm guessing a number between 1 and 100")
  print("Are you ready to guess?")
  
  number = random.randint(1,100)
  player_lives = 0
  
  level_difficulty = input("What difficulty do you want? 'easy' or 'hard'?\n").lower()
  
  if level_difficulty == "hard":
    player_lives = 5
  else: 
    player_lives = 10
  
  is_game_done = False
  
  while not is_game_done:
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
    if player_lives < 1:
      is_game_done = True
      print("You've no more guesses")
  replay_state = input("do you want to play again? 'Y' or 'N'\n").lower()
  if replay_state == 'y':
    clear()
    number_guess()
  else:
    clear()
number_guess()