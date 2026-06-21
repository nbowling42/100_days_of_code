from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    def caesar(original_text, shift_amount, encode_or_decode):
        #check if user input is valid
        if "encode" != encode_or_decode != "decode":
            print("Please type 'encode' to encrypt or 'decode' to decrypt")
            return

        #change shift amount to negative if user wants to decode
        if encode_or_decode == "decode":
            shift_amount *= -1

        output_text = ""
        #shift each letter in the original text by the shift amount and add it to the output text
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]

        print(f"Here is the {encode_or_decode}d result: {output_text}")

    #ask user for direction, text, and shift amount, then call the caesar function
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #call the caesar function with the user input and then ask if they want to go again
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    go_again = input("Do you want to go again (y/n)?\n").lower()
    if go_again == "n":
        print("Goodbye!")
        break
    