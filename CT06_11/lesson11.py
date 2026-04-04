# task 1
# height1 = int(input("Enter the height of the first rider: "))
# height2 = int(input("Enter the height of the second rider: "))
# if height1 >= 120 and height2 >= 120:
#     print("You can ride the roller coaster together!")
# else:    print("Sorry, you cannot ride the roller coaster together.")
# task 2
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 7 == 0:
#     print("The number is divisible by both 3 and 7.")
# else:
#     print("The number is not divisible by both 3 and 7.")
# task 3
# firstname = input("Enter your first name: ").lower()
# lastname = input("Enter your last name: ").lower()
# if firstname == "james" and lastname == "leong":
#     print("YOU ARE WANTED!")
# task 4
# rider1 = int(input("Enter the age of the first rider: "))
# rider2 = int(input("Enter the age of the second rider: "))
# if (rider1 >= 18 or rider2 >= 18):
#     print("You can ride the go kart together!")
# else:
#     print("Sorry, you cannot ride the go kart together.")
# task 5
# age = int(input("Enter your age: "))
# if age < 0:
#     print("Invalid age. Age cannot be negative.")
# if age >= 13 and age < 65:
#     print("You are an adult. Pay $20 for the ticket.")
# elif age <= 12 or age >= 65:
#     print("You are a child or senior. Pay $10 for the ticket.")
# task 6
# gender = input("Enter your gender: ").lower()
# if  gender == "m" or gender == "male":
#     print("valid input")
# else    print("invalid input")
# task 9
# passwordkey = "Python123"
# password = input("Enter the password: ")
# if password == passwordkey:
#     print("Access granted.")
# else:    print("Access denied. Incorrect password.")
johnusername = "John123"
johnpassword = "pw123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == johnusername and password == johnpassword:
    print("Access granted.")
elif username == johnusername or password != johnpassword:
    print("Username or password incorrect.")
else:    print("Access denied. Incorrect username and password.")