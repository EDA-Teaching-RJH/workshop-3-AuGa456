num1 = int(input("Whats your first number? "))
num2 = int(input("Whats your second number? "))
operator = input("Whats your operator? ")
tf = False
while tf == False:
    match operator:
        case "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            if num1 == 0 or num2 == 0:
                print("HELL NAW")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        case "^":
            result = num1 ^ num2
            print(f"{num1} ^ {num2} = {result}")
        case "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        case "Quit":
            print("Quitting")
    break


