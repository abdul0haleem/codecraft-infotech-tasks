def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char

    return result


while True:
    print("\n===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "3":
        print("Exiting Caesar Cipher...")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue

    message = input("Enter your message: ")

    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value! Please enter a number.")
        continue

    if choice == "1":
        encrypted = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted)

    elif choice == "2":
        decrypted = caesar_cipher(message, -shift)
        print("Decrypted message:", decrypted)
