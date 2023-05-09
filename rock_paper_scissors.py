import random

user = 0
cpu = 0


pick = ["rock", "paper", "scissors"]

while True:
    user_input = input("pick one Rock Paper or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in pick:
        continue

    ran_num = random.randint(0,2)

    cpu_pick = pick[ran_num]
    print("cpu picked", cpu_pick + ".")

    if user_input == "rock" and cpu_pick == "scissors":
        print("winner")
        user += 1

    elif user_input == "paper" and cpu_pick == "rock":
        print("winner")
        user += 1
    
    elif user_input == "scissors" and cpu_pick == "paper":
        print("winner")
        user += 1

    else:
        print("loser!")
        cpu += 1

print("you won", user, "times.")
print("the cpui won", cpu, "times.")
print("I hope you did well, See ya!")