from cryptography.fernet import Fernet
import os

# Function to generate a new key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved to 'secret.key'.")

# Function to load the existing key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{filename}' encrypted successfully!")

# Function to decrypt a file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{filename}' decrypted successfully!")

# Main logic
if __name__ == "__main__":
    # If key file doesn't exist, create it automatically
    if not os.path.exists("secret.key"):
        generate_key()
    
    action = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    file_path = input("Enter file name (e.g., test.txt): ")
    
    if action == 'E':
        encrypt_file(file_path)
    elif action == 'D':
        decrypt_file(file_path)
    else:
        print("Invalid choice! Please type 'E' or 'D'.")