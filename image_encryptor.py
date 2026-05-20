from PIL import Image

# Encrypt Image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            # Simple pixel manipulation
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save("encrypted_image.png")
    print("Encrypted image saved as encrypted_image.png")


# Decrypt Image
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save("decrypted_image.png")
    print("Decrypted image saved as decrypted_image.png")


# Main Program
choice = input("Enter 'e' for encryption or 'd' for decryption: ")

image_path = input("Enter image path: ")
key = int(input("Enter secret key: "))

if choice == 'e':
    encrypt_image(image_path, key)

elif choice == 'd':
    decrypt_image(image_path, key)

else:
    print("Invalid choice")
