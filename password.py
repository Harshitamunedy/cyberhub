#creating a simple Python script that allows the user to input a password (or an array of passwords). Use the cryptography library to encrypt the password(s) and then decrypt it, displaying both the encrypted and decrypted forms.
from cryptography.fernet import Fernet
#input password
user_password=input("enter a strong password:")

# genrate key 
def key_genrate():
    key=Fernet.generate_key()
    fernet=Fernet(key)
    return fernet

def encrypt_password():
    encrypted_password=Fernet.encrypt(user_password.encode())
    print("Encrypted Password is", encrypted_password)

def decrypt_password():
    decrypted_password=Fernet.decrypt((encrypted_password).decode())
    print("Decrypted Password is",decrypted_password)

key_genrate()
encrypt_password()
decrypt_password()