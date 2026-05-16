# recap
# import random
# dieroll = []
#for i in range(5):
#    numberrolled = random.randint(1, 6)
#    dieroll.append(numberrolled)
# print(dieroll)
# rolledsum = 0
# for i in range(len(dieroll)):
#    rolledsum = dieroll[i] + rolledsum
# print(f"Sum: {rolledsum}")
#task 1
# fruits = ["Apples", "Oranges", "Grapes", "Water"]
# price = [1000000, 99999999999999999999999, 219384753429024857893487, 1]
# for i in range(len(fruits)):
#     print(f"{fruits[i]} costs ${price[i]}")
# # task 2a
# items = ["apple", "milk", "bread", "egg", "chocolate"]
# stock = [10, 0, 2, 210, 20]
# for i in range(len(items)):
#     if stock[i] == 0:
#         status = "no stock lol"
#     elif stock[i] >=10:
#         status = "not good stock :)"
#     else:
#         status = "good stock :("
#     print(f"item: {items[i]} | stock amount: {stock[i]} | Status = {status}")
# #task 2b
# askforitem = input(f"What item do u wanna check lol")
# if askforitem in items:
#     check_index = items.index(askforitem)
#     print(f"we have {stock[check_index]} {askforitem}(s) remaining")
# else:
#     print("error: we dont have that lmao")
#task 4a
import random
choicesallowed = ["scissors", "paper", "stone"]
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
    computerchoice = random.choice(choicesallowed)
    yourchoice = input(f"input your choice between Scissors, Paper, Stone, gun, or shield!").lower()
    print(f"Computer chose {computerchoice}.")
    if yourchoice in choicesallowed:
        if (yourchoice == "scissors" and computerchoice == "paper") or (yourchoice == "paper" and computerchoice == "stone") or (yourchoice == "stone" and computerchoice == "scissors") or (yourchoice == "gun" and computerchoice == "scissors" or "stone" or "paper") or (yourchoice == "shield" and )
            player_score += 1
            print("You won!")
        elif yourchoice == computerchoice:
            print("T I E : D D D D D")
        else:
            computer_score += 1
            print("computer won lmao imagine being terrible and losing hahaha")
        print(f"Score rn - The person playing rn: {player_score} | Computer: {computer_score}")
        
    else:
        print("invalid move bro")