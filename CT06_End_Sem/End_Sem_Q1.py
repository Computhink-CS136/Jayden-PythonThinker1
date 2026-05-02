"""
============================================================
Q1a. Multiples of 10
============================================================
You are writing a program to print numbers from 10 to 200.
The program must use a while loop and increase in multiples of 10.

Program Requirements:
- Start from 10
- End at 200
- Increase by 10 each time
- Use a while loop

============================================================
"""

# ============================================================
# Step 1: Create while loop
# ============================================================

    

"""
============================================================
Q1b. Password Checker
============================================================
You are writing a program to check a password.

The program must:
- Store the password "superpass123"
- Ask the user to enter a password
- If correct, print:
    Access Granted
- If wrong, print:
    Access Denied

============================================================
"""

# ============================================================
# Step 1: Store password
# ============================================================



# ============================================================
# Step 2: Ask for input
# ============================================================



# ============================================================
# Step 3: Check password and print result
# ============================================================

#question 1
#task 1
num = 10
while num < 200:
    print(num)
    num += 10
    if num == 200:
        print(num)
        break
#task 2
password = "superpass123"
guess = input("Enter the password: ")
if guess == password:
    print("Access Granted")
else:
    print("Access Denied")