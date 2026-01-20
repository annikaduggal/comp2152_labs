import random

choices = ["rock", "paper", "scissors"]

playerChoice = input("Enter your choice: Rock (1), Paper (2) or Scissors (3): ")
playerChoice = int(playerChoice)
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")

computerChoice = random.randint(1,3)

playerChoice = choices[playerChoice-1]
computerChoice = choices[computerChoice-1]

print ("Computer chose: " + computerChoice)

if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == "rock" and computerChoice == "scissors":
    print("Rock beats scissors. You win!")
elif playerChoice == "paper" and computerChoice == "rock":
    print("Paper beats rock. You win!")
elif playerChoice == "scissors" and computerChoice == "paper":
    print("Scissors beats paper. You win!")
else:
    print("You lose!")





