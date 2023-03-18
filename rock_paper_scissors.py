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
import random
print("Welcome to the Rock Paper Scissors Game")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors : "))
choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choice)
if computer_choice == "Rock" and user_choice == 1:
  print("Your choice :")
  print(paper)
  print("Computer\'s choice :")
  print(rock)
  print("You won")
if computer_choice == "Rock" and user_choice == 2:
  print("Your choice :")
  print(scissors)
  print("Computer\'s choice :")
  print(rock)
  print("Computer won")
if computer_choice == "Rock" and user_choice == 0 :
 print("Your choice :")
 print(rock)
 print("Computer\'s choice :")
 print(rock)
 print("It\'s a tie")
if computer_choice == "Paper" and user_choice == 0:
 print("Your choice :")
 print(rock)
 print("Computer\'s choice :")
 print(paper)
 print("Computer won")
if computer_choice == "Paper" and user_choice == 2 :
 print("Your choice :")
 print(scissors)
 print("Computer\'s choice :")
 print(paper)
 print("Computer won")
if computer_choice == "Paper" and user_choice == 1 :
 print("Your choice :")
 print(paper)
 print("Computer\'s choice :")
 print(paper)
 print("It\'s a tie")
if computer_choice == "Scissors" and user_choice == 0 :
 print("Your choice :")
 print(rock)
 print("Computer\'s choice :")
 print(scissors)
 print("You won")
if computer_choice == "Scissors" and user_choice == 1:
 print("Your choice :")
 print(paper)
 print("Computer\'s choice :")
 print(scissors)
 print("Computer won")
if computer_choice == "Scissors" and user_choice == 2:
 print("Your choice :")
 print(scissors)
 print("Computer\'s choice :")
 print(scissors)
 print("It\'s a tie")
#else:
#  print("Thanks for visiting !")
