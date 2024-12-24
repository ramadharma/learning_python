def caesar_cipher():
    """
    A simple implementation of Caesar Cipher that allows encryption and decryption.
    """
    while True:
        # User selects encryption or decryption
        choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
        
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
            continue

        # User inputs the text
        text = input("Enter the text: ")

        # User inputs the shift value
        try:
            shift = int(input("Enter the shift number: "))
        except ValueError:
            print("Invalid input! Shift must be a number.")
            continue

        # Function to process the text
        def caesar(text, shift, direction):
            result = ""
            for char in text:
                if char.isalpha():
                    start = ord('A') if char.isupper() else ord('a')
                    shift = shift if direction == 'encrypt' else -shift
                    result += chr((ord(char) - start + shift) % 26 + start)
                else:
                    result += char  # Non-alphabetic characters remain unchanged
            return result

        # Perform the chosen operation
        if choice == 'encrypt':
            result = caesar(text, shift, 'encrypt')
            print(f"Encrypted text: {result}")
        elif choice == 'decrypt':
            result = caesar(text, shift, 'decrypt')
            print(f"Decrypted text: {result}")

        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

# Run the Caesar Cipher program
caesar_cipher()
