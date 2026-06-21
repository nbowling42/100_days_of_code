alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, original_text, shift_amount):

        if "encode" != direction != "decode":
            print("Please type 'encode' to encrypt or 'decode' to decrypt")
            return

        cipher_text = ""

        if direction == "decode":
            shift_amount *= -1

        for char in original_text:
            i = alphabet.index(char) + shift_amount
            i %= len(alphabet)
            cipher_text += alphabet[i]
        print(f"Here is the {direction}d result: {cipher_text}")

caesar(direction = direction, original_text = text, shift_amount = shift)
