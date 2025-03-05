def division(a, b):
    print("The result of division between " + str(a) + " / " + str(b) + " is " + str(a/b) + "\n")

def multiplication(a, b):
    print("The result of multiplication between " + str(a) + " x " + str(b) + " is " + str(a*b) + "\n")

print("Please enter two numbers: ")
num1 = int(input())
num2 = int(input())
exit = False
while not exit:
    decision = input("Choose an option [M for multiplication, D for division, E for exit]")
    if decision == "M":
        multiplication(num1,num2)
    elif decision == "D":
        division(num1,num2)
    elif decision == "E":
        exit = True
    else:
        decision = input("You didnt pick one of the choices. please try again [M,D,E]")

