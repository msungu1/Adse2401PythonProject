# Demonstration: Python's selection/decision/conditional constructs

# Import the sys (system) module
import sys

# -------------------------------------------------------------------------
# 1. if
# -------------------------------------------------------------------------
temperature = float(input("What is your temperature? \n"))
if temperature > 25:
    print("Let's head to the beach!")

password = "xeefe"
if password == "":
    print("Please enter your password.")

# -------------------------------------------------------------------------
# 2. if......else
# -------------------------------------------------------------------------
user_num = int(input("What is your number? I will tell you if it is odd or even: "))
if user_num % 2 == 0:
    print(f"{user_num} is even")
else:
    print(f"{user_num} is odd")

score = int(input("What is your score? "))
if score >= 40:
    print(f"Congratulations! A score of {score} is awesome.")
else:
    print(f"Unfortunately, a score of {score} is not awesome.")

# -------------------------------------------------------------------------
# 3. if........elif........else
# -------------------------------------------------------------------------
# Grade the student based on their score entered above
if score >= 85 and score <= 100:
    print(f"With a score of {score}, you got Grade A")
elif score >= 70 and score < 85:
    print(f"With a score of {score}, you got Grade B")
elif score >= 50 and score < 70:
    print(f"With a score of {score}, you got Grade C")
elif score >= 40 and score < 50:
    print(f"With a score of {score}, you got Grade D")
else:
    print(f"With a score of {score}, you got Grade F")
# -------------------------------------------------------------------------
# 4. match-case (Python 3.10+)
# -------------------------------------------------------------------------
day = input("Enter a day of the week: ").capitalize()

match day:
    case "Monday":
        print("Start the week strong! Stay focused.")
    case "Tuesday":
        print("Keep the momentum going.")
    case "Wednesday":
        print("Halfway there, stay motivated!")
    case "Thursday":
        print("Almost the weekend, keep pushing.")
    case "Friday":
        print("Great job! Finish the week on a high note.")
    case "Saturday" | "Sunday":
        print("Enjoy your weekend and recharge.")
    case _:
        print("That doesn't look like a valid day.")

# -------------------------------------------------------------------------
# 5. match-case for exam comments
# -------------------------------------------------------------------------
match score:
    case s if s >= 85:
        print("Excellent performance! You're a star 🌟")
    case s if s >= 70:
        print("Good job! Keep improving.")
    case s if s >= 50:
        print("Fair effort, but you can do better.")
    case s if s >= 40:
        print("You passed, but more practice is needed.")
    case _:
        print("Don't give up! Study harder and try again.")
m