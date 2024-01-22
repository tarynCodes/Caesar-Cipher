from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(message, shift_amount, direction_answer):
    final_text = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            if direction_answer == "encode":
                shifted_index = (index + shift_amount) % 26
            elif direction_answer == "decode":
                shifted_index = (index - shift_amount) % 26
            final_text += alphabet[shifted_index]
        else:
            final_text += char
    print(f"Your {direction}d message is {final_text}")


should_continue = True
while should_continue:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar(message=text, shift_amount=shift, direction_answer=direction)



    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("\nGoodbye!")

