# A program that encrypts and decrypts messages!

def module_cipher_function():
    text = input("Enter your message to encrypt: ")
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    print(cipher)

def module_decryptor_function():
    cipher = input('Enter your encripted message to decrypt: ')
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    print(text)
    
def run_module(module_number):
    if module_number == 1:
        module_cipher_function()
    elif module_number == 2:
        module_decryptor_function()
    else:
        print("Invalid module number. Please select 1 or 2.")

def main():
    while True:
        print("Select a module to run:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")

        try:
            choice = int(input("Enter the module number (1, 2, or 0 to exit): "))
            if choice == 0:
                print("Exiting program.")
                break
            run_module(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
