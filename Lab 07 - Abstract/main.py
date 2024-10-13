# Authors: Sophia Ngo, Melanie Loepz, Sara Tfaili
# Date: 3/11/2024
# Description: A program that allows the user to encrypt or decrypt messages usign two different types of encryption methods. 

import check_input 
import atbash
import caesar_cipher

def main(): 
  shift_value = None
  
  while True: 
    print("Secret Decoder Ring:\n1. Encrypt\n2. Decrypt")
    choice = check_input.get_int_range(" ", 1, 2)

    if choice == 1: 
        print("Enter encryption type:\n1. Atbash\n2. Caesar")
        encryption_choice = check_input.get_int_range(" ", 1, 2)
        message = input("Enter message: ")

        if encryption_choice == 1: 
            atbash_cipher_obj = atbash.AtbashCipher() 
            encrypted_message = atbash_cipher_obj.encrypt_message(message)
            with open("message.txt", "w") as file: 
                file.write(f"Encrypted message: {encrypted_message}")
            print("Encrypted message saved to \"message.txt\".\n")
        elif encryption_choice == 2: 
            shift_value = check_input.get_int_range("Enter shift value: ", 0, 25)
            caesar_cipher_obj = caesar_cipher.CaesarCipher(shift_value)
            encrypted_message = caesar_cipher_obj.encrypt_message(message)
            with open("message.txt", "w") as file: 
                file.write(f"Encrypted message: {encrypted_message}")
            print("Encrypted message saved to \"message.txt\".\n")

    elif choice == 2:
        print("Enter decryption type:\n1. Atbash\n2. Caesar")
        decryption_choice = check_input.get_int_range(" ", 1, 2)

        if decryption_choice == 1:
            atbash_cipher_obj = atbash.AtbashCipher()
        elif decryption_choice == 2: 
            shift_value = check_input.get_int_range("Enter shift value: ", 0, 25)
            caesar_cipher_obj = caesar_cipher.CaesarCipher(shift_value)

        print("Reading encrypted message from \"message.txt\".")
        try:
            with open("message.txt", "r") as file:
                encrypted_message = file.read().split(": ")[1].strip()  
        except FileNotFoundError:
            print("Error: 'message.txt' not found.")
            continue
      
        if decryption_choice == 1:
          atbash_cipher_obj = atbash.AtbashCipher()
          decrypted_message = atbash_cipher_obj.decrypt_message(encrypted_message)
          print(f"Decrypted message: {decrypted_message}")
        elif decryption_choice == 2:
          caesar_cipher_obj = caesar_cipher.CaesarCipher(shift_value)
          decrypted_message = caesar_cipher_obj.decrypt_message(encrypted_message)
          print(f"Decrypted message: {decrypted_message}\n")

main()
