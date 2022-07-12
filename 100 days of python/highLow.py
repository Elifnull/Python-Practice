import random
from replit import clear
from art import Hlogo, vs
from game_data import data

def highLow():
    choiceA = random.choice(data)
    choiceB = random.choice(data)
    game_continue = True
    score = 0
    
    while game_continue:
        print(Hlogo)
        print(f'Compare A: {choiceA["name"]}, {choiceA["description"]}, from {choiceA["country"]}')
        print(choiceA['follower_count'])
        print(vs)
        
        print(f'Compare B: {choiceB["name"]}, {choiceB["description"]}, from {choiceB["country"]}')
        
        print(choiceB['follower_count'])
        
        player_choice = input("Who has more followers? Type 'A' or 'B'  ").lower()
        print(player_choice)
        
        if player_choice == "a":
        if (choiceA['follower_count'] > choiceB['follower_count']) == True:
            clear()
            score += 1
            print(f"You are correct! Your Score: {score}")
            choiceA = choiceA
            choiceB = random.choice(data)
        else:
            print(f"You are wrong. Your Score: {score}")
            game_continue = False
        elif player_choice == "b":
        if (choiceA['follower_count'] < choiceB['follower_count']) == True:
            clear()
            score += 1
            print(f"You are correct! Your Score: {score}")
            choiceA = choiceB
            choiceB = random.choice(data)
        else:
            print(f"You are wrong. Your Score: {score}")
            game_continue = False

highLow()