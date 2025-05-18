def shift_text(message, steps, direction='encrypt'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    # If we're decrypting, just flip the shift
    if direction == 'decrypt':
        shift = -shift

    for char in message:
        if char.lower() in alphabet:
            is_capital = char.isupper()
            index = alphabet.index(char.lower())
            new_index = (index + shift) % 26
            shifted_char = alphabet[new_index]
            result += shifted_char.upper() if is_capital else shifted_char
        else:
            result += char  # leave punctuation, spaces, numbers unchanged

    return result


print("===>>> Caesar Cipher <<<===")

user_message = input("Enter your message: ")

while True:
    try:
        shift_value = int(input("Enter the shift value (number): "))
        break
    except:
        print("Invalid input! Please enter a valid number.")

# encrypt or decrypt?
mode = input("Do you want to 'encrypt' or 'decrypt'?: ").lower()
while mode not in ['encrypt', 'decrypt']:
    mode = input("Please type 'encrypt' or 'decrypt': ").lower()


final_result = shift_text(user_message, shift_value, mode)


print("\nYour", mode, "result is:", final_result)
