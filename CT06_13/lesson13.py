# #recap 1
# money = 1000
# while True:
#     print("Welcome to the atm ---")
#     print("1) Withdraw")
#     print("2) Deposit")
#     print("3) Check Balance")
#     print("4) Exit\n")

#     choice = input("Enter your choice: ")
#     if choice == "1":
#         howmuch = int(input("Enter how much money you want to withdraw."))
#         if howmuch > money:
#             print("You dont have that much in your bank!")
#         elif howmuch < money:
#             print("Heres your money!")
#     elif choice == "2":
#         deposit = input("Enter the amount ")
#         if not deposit.isdigit():
#             print("Invalid amount. Try again.\n")
#         else:
#             deposit = int(deposit)
#             money = money + deposit
#             print(f"You have deposited ${deposit}.\n")
#     elif choice == "3":
#         print(f"Your balance is ${money}.\n")
#     elif choice == "4":
#         print("goodbye!")
#         break

# fruits = ["apple", "banana", "cherry", "durian"]

# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "durian"
# ]

# print(fruits[3])
# task 1a
groceries = ["apples", "bread", "carrots", "dates", "eggs", "flour", "grapes", "honey"]
#task 1b
groceries[7] = "herbs"
# print(groceries)
# #task 1c
groceries.append("ice")
groceries.insert(1, "bananas")
# print(groceries)
# #task 1d
removed = groceries.pop(2)
# print(groceries)
# print(f"{removed} was removed.")
#task 2
for i in range(len(groceries)):
    if groceries[i] == "apple":
        print(f"{groceries[i]}: I need 5 of these.")
    elif groceries[i] == "carrots":
        print(f"{groceries[i]}: I need 3 of these.")
    elif groceries[i] == "grapes":
        print(f"{groceries[i]}: I need to buy the farmfresh brand.")
    else:
        print(groceries[i])
#task 3
while True:
    items = input("What items are in ur basket. TELL ME")
    groceries.append(items)
    if items == "end":
        break
    groceries.append(items)
for i in range(len(groceries)):
    print(f"I have bought {groceries[i]}.")