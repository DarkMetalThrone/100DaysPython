#print the logo
import art
import os

#define all the operations as functions
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multi(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

#make a dictionary which has symbols as keys and functions as values
operation_list = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

def calculator():
    #clearing the terminal screen dosent work yet
    os.system('cls' if os.name == 'nt' else 'clear')
    #print the logo
    print(art.logo)
    #start taking inputs
    num1 = float(input("Enter the First Number: "))
    for i in operation_list:
        print(i)

    end_of_program = False

    #the perpetual while loop
    while not end_of_program:
        action = input("Choose an Operation: ")
        num2 = float(input("Enter the Subsequent Number: "))
        #calculate the answer
        operation = operation_list[action]
        answer = operation(num1, num2)
        print(f"{num1} {action} {num2} = {answer}")
        intent = input("continue? 'y' or 'n', Press 'C' to reset: ")
        if intent == "y":
            num1 = answer
        elif intent == "C":
            calculator()
        else:
            print("Invalid Input, The program will end.")
            end_of_program = True

calculator()