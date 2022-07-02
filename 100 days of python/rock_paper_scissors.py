import random as ran
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
if human_choice > 2 or human_choice < 0:
  print("You lose, wrong value")
else:
  robot_choice = ran.randint(0,2)
  
  def rock_paper_sissors(choice, person="You"):
    if choice == 0:
      print(f'{person} chose Rock \n {rock}')
      return rock
    elif choice == 1:
      print(f"{person} chose Paper\n {paper}")
      return paper
    elif choice == 2:
      print(f"{person} chose Scissors\n {scissors}")
      return scissors
  
  
  human_output = rock_paper_sissors(int(human_choice))
  robot_output = rock_paper_sissors(robot_choice, "Robot")
  value_difference = human_choice - robot_choice
  
  
  if value_difference == 0:
    print("it is a Draw")
  elif value_difference == -2 or value_difference == 1:
    print("You win")
  elif value_difference == -1 or value_difference == 2:
    print("You lose")

##added logic at begining to elimate values outside of the choices of 0,1,2.