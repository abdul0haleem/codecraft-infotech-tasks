from PIL import Image


def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print("Image encrypted successfully")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print("Image decrypted successfully")

def main():
    print("Pixel Manipulation for Image Encryption")
    print("---------------------------------------")

    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1/2): ")
    input_path = input("Enter the image file path: ")
    key = int(input("Enter the encryption key: "))
    output_path = input("Enter the output image path: ")

    if choice == "1":
        encrypt_image(input_path, output_path, key)

    elif choice == "2":
        decrypt_image(input_path, output_path, key)

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
