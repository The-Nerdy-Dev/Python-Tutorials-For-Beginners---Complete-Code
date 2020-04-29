import random

# Choices for our game
game_choices = ["rock", "paper", "scissor"]
cpu_choice = random.choice(game_choices)

# Scores
cpu_score = 0.0
your_score = 0.0

waiting_for_input = True

while waiting_for_input:
   your_choice = input("Enter your choice: ")

   if your_choice == cpu_choice:
       print("It is a tie")
       cpu_score += 1
       your_score += 1
   elif your_choice == "rock" and cpu_choice == "paper":
       print("CPU's", cpu_choice, "beats your", your_choice)
       cpu_score += 1
   elif your_choice == "paper" and cpu_choice == "scissor":
       print("CPU's", cpu_choice, "beats your", your_choice)
       cpu_score += 1
   elif your_choice == "scissor" and cpu_choice == "rock":
       print("CPU's", cpu_choice, "beats your", your_choice)
       cpu_score += 1
   elif your_choice == "rock" and cpu_choice == "scissor":
       print("Your's", your_choice, "beats CPU's", cpu_choice)
       your_score += 1
   elif your_choice == "paper" and cpu_choice == "rock":
       print("Your's", your_choice, "beats CPU's", cpu_choice)
       your_score += 1
   elif your_choice == "scissor" and cpu_choice == "paper":
       print("Your's", your_choice, "beats CPU's", cpu_choice)
       your_score += 1

   print("Your current score:", your_score)
   print("CPU's current score:", cpu_score)

   if your_score == 10 or cpu_score == 10:
       waiting_for_input = False
   cpu_choice = random.choice(game_choices)

print(your_score, cpu_score)

# Select the winner
if your_score > cpu_score:
    print("You are the winner")
elif your_score < cpu_score:
    print("CPU is the winner")
else:
    print("It was a close match, but nobody won :D")

