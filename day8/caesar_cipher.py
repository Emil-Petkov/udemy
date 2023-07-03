from ascii_art import logo


def encrypt_massage(massage, shift_number):
    encrypt_massage = [ord(x) + shift_number for x in massage]
    encrypt = [chr(x) for x in encrypt_massage]
    print(''.join(encrypt))


def decrypt_massage(massage, shift_number):
    decrypt_massage = [ord(x) - shift_number for x in massage]
    decrypt = [chr(x) for x in decrypt_massage]
    print(''.join(decrypt))


is_play = True

print(logo)

while is_play:

    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    command = input(">>> ")
    print("Type your massage:")
    massage = input(">>> ")
    print("Type the shift number:")
    shift_number = int(input(">>> "))

    if command == 'encode':
        encrypt_massage(massage, shift_number)

    elif command == 'decode':
        decrypt_massage(massage, shift_number)

    print("Type 'Y'es' if you want to go again. Otherwise, type 'N'o.")

    user_choice = input(">>> ").lower()

    if user_choice == "y":
        continue
    elif user_choice == "n":
        break
