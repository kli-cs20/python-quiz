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
answer2 = input("What is the square root of 64? ")
if answer2 == "8":
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
    "You want to gather user inputs of numbers with decimal points; do you use an 'int' 'str' or 'float'? ")
if answer4 == "float":
    print("Correct")
    score += 1
else:
    print("Incorrect")


# Result
print("\nYour score is", score, "/ 4 or", score / 4 * 100, "%")
