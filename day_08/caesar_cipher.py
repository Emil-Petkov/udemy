











from ascii_art import art

print(art)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text: str, shift_amount: int, cipher_direction: str):
    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]

        else:
            end_text += char

    print(f'\nThe {cipher_direction}d text is: {end_text}\n')


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))

    caesar(text, shift, direction)

    command = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if command == 'yes':
        continue

    elif command == 'no':
        print('Goodbye!')
        should_continue = False

    else:
        print(f'\nInvalid command: {command}')
        should_continue = False
