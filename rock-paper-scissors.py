import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

computer_picked = random.randint(0, 2)
list_items = [rock, paper, scissors]
strings = ["rock", "paper", "scissors"]
idx = int(input("Please type 0 for rock, 1 for paper or 2 for scissors \n"))

if idx >= len(list_items) or idx < 0:
    exit("Invalid entry! Please make sure you enter either 0, 1 0r 2.")

if idx == computer_picked:
    print(
        f"Draw! You picked {list_items[idx]} \ncomputer picked {list_items[computer_picked]}"
    )
elif idx == 0 and computer_picked == 2:
    print(
        f"You win! You picked {list_items[idx]} \ncomputer picked {list_items[computer_picked]}"
    )
elif idx == 1 and computer_picked == 0:
    print(
        f"You win! You picked {list_items[idx]} \ncomputer picked {list_items[computer_picked]}"
    )
elif idx == 2 and computer_picked == 1:
    print(
        f"You win! You picked {list_items[idx]} \ncomputer picked {list_items[computer_picked]}"
    )
else:
    print(
        f"You lost! You picked {list_items[idx]} \ncomputer picked {list_items[computer_picked]}"
    )
