#creating a simple Python script that allows the user to input a password (or an array of passwords). Use the cryptography library to encrypt the password(s) and then decrypt it, displaying both the encrypted and decrypted forms.
from cryptography.fernet import Fernet
#input password
print("A strong password is a combination of letters, numbers, and symbols that is at least 12 characters long.")
user_password = input("Enter a strong password: ")

# Generate key
def key_generate():
    key = Fernet.generate_key()
    return key

# Encrypt password
def encrypt_password(fernet, password):
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt password
def decrypt_password(fernet, encrypted_password):
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Main function to handle the process
def main():
    # Generate key and create Fernet instance
    key = key_generate()
    fernet = Fernet(key)
    print(f"Encryption Key: {key.decode()}")
    # Encrypt the password
    encrypted_password = encrypt_password(fernet, user_password)
    print("Encrypted Password is:", encrypted_password.decode())

    # Decrypt the password
    decrypted_password = decrypt_password(fernet, encrypted_password)
    print("Decrypted Password is:", decrypted_password)

main()