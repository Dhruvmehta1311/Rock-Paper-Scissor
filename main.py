import random
from replit import clear
still_on= True
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

while still_on:
  game_images = [rock, paper, scissors]

  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")

  want_to_continue =input("Do you want to Continue ? 'Yes' or 'No' ? : ").lower()
  if want_to_continue :
    clear()  
  else :
    still_on = False  

