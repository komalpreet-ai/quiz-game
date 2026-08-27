print("WELCOME TO QUIZ GAME")

score = 0

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("2. What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("3. Which language is used for this project? ")

if answer.lower() == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("4. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("5. What is 10 - 5? ")

if answer == "5":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nYour final score is:", score, "/ 5")