Age = int(input("How old are you? "))
Student = input("Are you a student? ")

if Student == "yes" and Age >= 12 or Age <= 64:
    print("Tickets are £8 please")
elif Student == "no" and Age >= 12 or Age <=64:
    print("Tickets are £10 please")
elif Student == "no" and Age >= 65:
    print("Tickets are £5 please")
elif Student == "no" and Age <= 12:
    print("Tickets are £5 please")
