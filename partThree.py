score = int(input("What is your score? "))

if score >= 90 and score <= 100:
    print("You got an A!")
elif score >=80 and score <= 89:
    print("You got a B!")
elif score >= 70 and score <= 79:
    print("You got a C")
elif score >=60 and score <= 69:
    print("You got a D")
elif score < 60 and score >= 0:
    print("You got an F :(")
elif score > 100:
    print("Holy cow batman! Thats too much score.")
else:
    print("Thats sad, negative score :(")