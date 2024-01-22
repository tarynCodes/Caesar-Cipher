alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # doubled up to ensure we can encrypt all letters

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(message, shift_amount, direction_answer):
    final_text = ""
    for letter in message:
        index = alphabet.index(letter)
        if direction_answer == "encode":
            shifted_index = index + shift_amount
        elif direction_answer == "decode":
            shifted_index = index - shift_amount
        final_text += alphabet[shifted_index]
    print(f"Your {direction}d message is {final_text}")


caesar(message=text, shift_amount=shift, direction_answer=direction)

