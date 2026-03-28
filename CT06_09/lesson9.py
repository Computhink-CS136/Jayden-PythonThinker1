# # task 1
# import random
# random1 = random.randint(1, 6)
# random2 = random.randint(1, 6)
# random3 = random.randint(1, 6)
# print(f"1st die: {random1}")
# print(f"2nd die: {random2}")
# print(f"3rd die: {random3}")
# even = False
# odd = False
# if random1 % 2 == 0 and random2 % 2 == 0 and random3 % 2 == 0:
#     even = True
# if random1 % 2 == 1 and random2 % 2 == 1 and random3 % 2 == 1:
#     odd = True
# if even == True or odd == True:
#         print("All dice are even or all even/odd")
# else:    print("Not all dice are even or odd")
# #task 2
# numdays = int(input("Enter the number of days: "))
# if numdays > 25 or numdays == 25:
#     print("Remember to return the library books!")
#task 3a
# apple = int(input("Enter the number of apples: "))
# if apple > 10 or apple == 10:
#     print("You will get a 10% discount!")
#     print("Your total is: ", f"${apple * 0.9:.2f}")
# else:
#     print("Your total is: ", f"${apple * 1.0:.2f}")
#task 3b
# num_apples = int(input("Enter the number of apples: "))
# num_oranges = int(input("Enter the number of oranges: "))
# if num_apples > 5 or num_apples == 5 or num_oranges > 5 or num_oranges == 5:
#     print("You will get a 10% discount!")
#     print("Your total is: ", f"${(num_apples * 0.9 * 0.6) + (num_oranges * 0.9 * 0.9):.2f}")
# else:    print("Your total is: ", f"${(num_apples * 1.0) + (num_oranges * 1.0):.2f}")