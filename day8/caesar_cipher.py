from ascii_art import logo
import string


def rotate_letter(letter, step):
    ascii_letter = string.ascii_letters
    num_letters = len(ascii_letter)

    current_letter = ascii_letter.index(letter)

    new_position = (current_letter + step) % num_letters

    return ascii_letter[new_position]


def encrypt_massage(massage, shift_number):
    encrypt_massage = [rotate_letter(x, shift_number) for x in massage]
    print(''.join(encrypt_massage))


def decrypt_massage(massage, shift_number):
    decrypt_massage = [rotate_letter(x, -shift_number) for x in massage]
    print(''.join(decrypt_massage))


print(logo)

while True:
    try:
        print("\nType 'encode' to encrypt, type 'decode' to decrypt:")
        command = input(">>> ")
        if command not in ['encode', 'decode']:
            raise ValueError("Invalid command")

        print("\nType your massage:")
        massage = input(">>> ")
        print("\nType the shift number:")
        shift_number = int(input(">>> "))

        if command == 'encode':
            encrypt_massage(massage, shift_number)

        elif command == 'decode':
            decrypt_massage(massage, shift_number)

        user_choice = ""
        while user_choice not in ["y", "n"]:
            print("\nType 'Y'es' if you want to go again. Otherwise, type 'N'o.")

            user_choice = input(">>> ").lower()
            if user_choice not in ["y", "n"]:
                print("Invalid choice. Please try again.")

        if user_choice == "y":
            continue
        elif user_choice == "n":
            break

    except ValueError as e:
        print(e)
