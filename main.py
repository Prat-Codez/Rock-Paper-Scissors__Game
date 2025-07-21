import random
print("Hello!!")
print("Welcome to Rock Paper Scissors!!!")
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please enter rock, paper, or scissors")
        continue
    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print("Computer chose: " + computer_choice+".")
    if computer_choice == user_input:
        print("DRAW!!")
    elif user_input == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You won!")
    elif user_input == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You Won!")
    elif user_input == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You Won!")
    else:
        print("Sorry, you lost!")
        computer_wins += 1

print("User_wins are {},Computer_wins are {}".format(user_wins, computer_wins))
print("Thank you for playing!")
print('Goodbye!!')
