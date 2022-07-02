import random

# 🚨 Don't change the code below 👇

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_end_index = len(names) -1
random_index = random.randint(0,list_end_index)
print(f"{names[random_index]} is going to buy the meal today!")

"""""
random.choice() is an easier way of doing this 
"""

# alternative method, and simpler

print(print(f"{random.choice(names)} is going to buy the meal today!")) #this is the better method