# recap 1
# sumof = 0
# for i in range(1, 6):
#     num = int(input(f"Enter number {i} \n"))
#     sumof = sumof + num
# multiplication = sumof * 5
# print(f"The multiplication of the numbers is: {multiplication}")
#task 1
# import time
# seconds = int(input("how many seconds "))
# for i in range(seconds , 0, -1):
#     print(i)
#     time.sleep(1)
# print("Time's up")
#task 2a
# import random
# num = random.randint(1, 6)
# print(num)
# #task 2b
# import random
# for i in range(1, 21):
#     i = random.randint(0, 9999)
#     print(i)
# #task 3a
# boolean = True
# print(boolean)  
# #task 3b
# boolean = True
# boolean2 = True
# print(bool(boolean == boolean2))   
# #task 3c
# boolean = True
# boolean2 = False
# print(bool(boolean == boolean2))
#task 5
# import random
# total = 0
# num1 = random.randint(1, 50)
# num2 = random.randint(1, 50)
# total = num1 + num2
# guess = (int(input(f"What is {num1} + {num2} ?\n")))

# boolean = bool(guess == total)
# print(f"Your guess is {boolean}")
# print(f"The number was {total}")
#task 6
# import random
# questions = int(input("How many questions do you want to try?\n"))
# for questions in range(1, questions + 1):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     answer = num1 * num2
#     guess = (int(input(f"What is {num1} * {num2} ?\n")))
#     if guess == answer:
#         print("Correct!")
#     else:        
#         print("Wrong!")
#task 7
# number = int(input("Gimme a number and i will tell you if odd or even\n"))
# if number % 2 == 0:
#     print("the number is even")
# else:    print("the number is odd")
# task 8
# num1 = int(input("Gimme a number\n"))
# num2 = int(input("Gimme another number\n"))
# if num1 % num2 == 0:
#     print(f"{num1} is a multiple of {num2}")
# else:    print(f"{num1} is not a multiple of {num2}")
# if num2 % num1 == 0:
#     print(f"{num2} is a multiple of {num1}")
# else:    print(f"{num2} is not a multiple of {num1}")
# challege 1
# score = 0
# question1 = input("What is the capital of France?\n")
# if question1.lower() == "paris":
#     score += 1
#     print("Correct!")
# else:
#  print("Wrong!")
# question2 = input("What is the largest planet in our solar system?\n")
# if question2.lower() == "jupiter":
#     score += 1
#     print("Correct!")
# else:
#  print("Wrong!")
# question3 = input("Who wrote the play 'Romeo and Juliet'?\n")
# if question3.lower() == "william shakespeare":
#     score += 1
#     print("Correct!")
# else:
#    print("Wrong!")
# question4 = input("What is the chemical symbol for potassium?\n")
# if question4.lower() == "k":
#     score += 1
#     print("Correct!")
# else:
#  print("Wrong!")
# question5 = input("what is 1 + 1\n")
# if question5 == "window":
#     score += 1
#     print("Correct!")
# else: print("Wrong!")
# question6 = input("What is the worst number ever?\n")
# if question6 == "67":
#     score += 1
#     print("Correct!")
# else:
#     print("Wrong!")

# print(f"Your score is {score} out of 6")
#challenge 2
import random
print("Guess the number between 1 and 100")
number = random.randint(1, 100)
attempt = 1
print(f"Attempt {attempt}")
guess = int(input("Enter your guess: "))
while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempt += 1
    print(f"Attempt {attempt}")
    guess = int(input("Enter your guess: "))
    if attempt > 5:
        print(f"Sorry, you've used all 5 attempts. The number was {number}.")
        break
    if attempt < 5 and guess == number:
        print(f"Congratulations! You've guessed the number {number} in {attempt} attempts!")
        break