#recap 1
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 and 5.")
# else:
#     print(f"{num} is not divisible by both 3 and 5.")
#task 1
# visitor = 4
# while visitor < 25:
#     visitor += 1
#     print(visitor)
#task 2
# visitors = 0
# while True
#     visitors += 1
#     print(visitors)
#     if visitors >= 50:
#         break
#task 3
# totalorder = input("Enter your order.\n ")
# while True:
#     order = input("Enter your order.\n ")
#     if order == "end".lower():
#         break
#     totalorder += ", " + order
# print(f"your order: {totalorder}.")
#task 4
# counter = 10
# while not counter <= 0:
#     print(counter)
#     counter -= 1
# else:
#     print("Happy New Year!!!")
#task 5
import random
score = 0
while score <= 20:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.randint(1, 3)
    if operator == 1:
        answer = num1 + num2
        operator_sign = "+"
    elif operator == 2:
        answer = num1 - num2
        operator_sign = "-"
    else:
        answer = num1 * num2
        operator_sign = "*"
    guess = int(input(f"what is {num1} {operator_sign} {num2}?\n"))
    if guess == answer:
        print("correct")
        score += 2
    else:
        print("wrong")
        score -= 1
print(f"final score: {score}")