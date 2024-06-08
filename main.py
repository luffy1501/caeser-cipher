alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art

print(art.logo)




   
def ceasar(text, shift, direction):
    
        if direction == "decode":
            shift *= -1
        plain_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                plain_text += alphabet[new_position]
            else:
                plain_text += char
        print(f"The {direction}d text is {plain_text}")
        
    


should_cotinue = True
while should_cotinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= 45:
        exit("You have entered a shift value greater than 45. Please enter a shift value less than 45")
    ceasar(text, shift, direction)
    restart = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart =="no":
        should_cotinue = False
        print("Goodbye")


        
