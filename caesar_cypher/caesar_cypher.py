alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print the logo
import art
print(art.logo)

end_of_program = False

#The input fucntion
def ask():
    direction = input("Enter 'encode' to ENCRYPT and 'decode' to DECRYPT: ")
    text = input("Enter your message: ")
    shift = int(input("Enter the Cypher Key: "))
    cypher(plain_text = text, shift_parameter = shift, purpose = direction)

#cipher logic
def cypher(plain_text, shift_parameter, purpose):
    #change the magnitude of shift if the direction is reversed
    if purpose == 'decode':
        shift_parameter *= -1
    elif purpose == 'encode':
        shift_parameter *= 1
    else:
        print("Invalid Entry, Restart the program to continue.")
        return

    #create a new string with the ecoded/ decoded message
    new_text = ""
    for i in plain_text:
        #encode only the letters of the alphabet
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_parameter) % 26
            new_text += alphabet[new_position]
        #exclude all symbols and numbers -- just add them to the new string as is
        else:
            new_text += i

    print(f"The processed message is: {new_text}")

while not end_of_program:
    #ask the user if wants to continue?
    intent = input("Do you want to continue? type 'yes' or 'no': ")
    #call the input function if YES
    if intent == 'yes':
        ask()
    #end the program if NO
    elif intent == 'no':
        end_of_program = True
        print("Good Bye")