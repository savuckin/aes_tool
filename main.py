from aes import AESTool

def main():
    print("Welcome to the AES Encryption/Decryption Tool!")
    aes = AESTool()

    print("\nYour AES Key (keep this secret!):")
    print(base64.b64encode(aes.key).decode())

    action = input("\nDo you want to (e)ncrypt or (d)ecrypt? ").lower()
    if action == 'e':
        plaintext = input("Enter the text to encrypt: ")
        iv, ciphertext = aes.encrypt(plaintext)
        print(f"\nIV: {iv}")
        print(f"Ciphertext: {ciphertext}")
    elif action == 'd':
        iv = input("Enter the IV: ")
        ciphertext = input("Enter the ciphertext: ")
        plaintext = aes.decrypt(iv, ciphertext)
        print(f"\nDecrypted Text: {plaintext}")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()