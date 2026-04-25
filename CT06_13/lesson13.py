# # #recap 1
# # money = 1000
# # while True:
# #     print("Welcome to the atm ---")
# #     print("1) Withdraw")
# #     print("2) Deposit")
# #     print("3) Check Balance")
# #     print("4) Exit\n")

# #     choice = input("Enter your choice: ")
# #     if choice == "1":
# #         howmuch = int(input("Enter how much money you want to withdraw."))
# #         if howmuch > money:
# #             print("You dont have that much in your bank!")
# #         elif howmuch < money:
# #             print("Heres your money!")
# #     elif choice == "2":
# #         deposit = input("Enter the amount ")
# #         if not deposit.isdigit():
# #             print("Invalid amount. Try again.\n")
# #         else:
# #             deposit = int(deposit)
# #             money = money + deposit
# #             print(f"You have deposited ${deposit}.\n")
# #     elif choice == "3":
# #         print(f"Your balance is ${money}.\n")
# #     elif choice == "4":
# #         print("goodbye!")
# #         break

# # fruits = ["apple", "banana", "cherry", "durian"]

# # fruits = [
# #     "apple",
# #     "banana",
# #     "cherry",
# #     "durian"
# # ]

# # print(fruits[3])
# # task 1a
# groceries = ["apples", "bread", "carrots", "dates", "eggs", "flour", "grapes", "honey"]
# #task 1b
# groceries[7] = "herbs"
# # print(groceries)
# # #task 1c
# groceries.append("ice")
# groceries.insert(1, "bananas")
# # print(groceries)
# # #task 1d
# removed = groceries.pop(2)
# # print(groceries)
# # print(f"{removed} was removed.")
# #task 2
# for i in range(len(groceries)):
#     if groceries[i] == "apples":
#         print(f"{groceries[i]}: I need 5 of these.")
#     elif groceries[i] == "carrots":
#         print(f"{groceries[i]}: I need 3 of these.")
#     elif groceries[i] == "grapes":
#         print(f"{groceries[i]}: I need to buy the farmfresh brand.")
#     else:
#         print(groceries[i])
# #task 3
# while True:
#     items = input("What items are in ur basket. TELL ME")
#     groceries.append(items)
#     if items == "end":
#         groceries.pop(items)
#         break
# for i in range(len(groceries)):
#     print(f"I have bought {groceries[i]}.")
# #task 4
# catalogue =[]
# while True:
#     item = input("what items should you put into the online catalogue?\n")
#     catalogue.append(item)
#     if item == "end":
#         break
#     catalogue.append(item)
# print(catalogue)
# ask = input("what are u looking for?")
# if ask in catalogue:
#     print(f"Yes we sell {ask}")
# else:
#     print(f"Sorry, we dont have {ask}")
#task 5
# import random
# number = []
# for i in range(10):
#     randomnum = random.randint(1, 10000)
#     number.append(randomnum)
# print(number)
# for i in range(len(number)):
#     print(number[i])
#     print(f"Winner #{i + 1} = {number[i]}")
#task 6
thetoppings = []
toppings = ["shit", "pepperoni", "cheese", "melted cheese", "extra cheese", "the sauce", "dough", "More Cheese", "EVEN MORE CHEESE", "watered down"]
for i in range(len(toppings)):
    print(f"{i + 1} = {toppings[i]}")
while True:
    whattoppings = input("choose the toppings you want based on number.\n")
    if whattoppings == "end":
        break
    thetoppings.append(int(whattoppings))
print(thetoppings)
for i in range(len(thetoppings)):
    print(toppings[thetoppings[i] - 1])
