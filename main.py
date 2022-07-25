# Python Quiz

# Score
score = 0

# Question One
answer1 = input("What class are you taking? ").lower()
if answer1 == "cs20" or answer1 == "computer sciences":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question Two
answer2 = input("What is the square root of 64? ").lower()
if answer2 == "8" or answer2 == "eight":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question Three
answer3 = input("What coding language is this program created by? ").lower()
if answer3 == "python":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question Four
answer4 = input(
    "You want to gather user inputs of numbers with decimal points; do you use an 'int' 'str' or 'float'? ").lower()
if answer4 == "float":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question Five
answer5 = input("What year was Python released as a programming language? ")
if answer5 == "1991":
    print("Correct")
    score += 1
else:
    print("Incorrect")


# Result
print("\nYOUR RESULTS:")
print(score, "/ 5 or", score / 5 * 100, "%")
if score <= 2:
    print("You need to study... ")
elif score <= 4:
    print("Not bad, want to try again?")
else:
    print("Perfection!")
