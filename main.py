from modules.encryption import aes_ed, rsa_ed
from modules.hash_file import hash_file, verify_integrity
from modules.password import check_password_strength, hash_pw, verify_password
from getpass import getpass

def menu(): 
    print("Choose an operation (from 1 to 4)")
    print("1. Encryption")
    print("2. Hashing")
    print("3. Integrity verification (for files)")
    print("4. Checking a password's strength")

def encryption():
    print("Choose encryption method (choose 1 or 2)")
    print("1. AES method")
    print("2. RSA method")
    method = int(input())
    message = input("Enter the message you want to encrypt: ")
    if method == 1:
        result = aes_ed(message)
    elif method == 2:
        result = rsa_ed(message)
    else: 
        print("Something went wrong with your input. Please try again.")
    print(f"encrypted message: {result[0]}")
    print(f"Plain text: {result[1]}")

def hashing():
    print("Choose an option:")
    print("1. Hash a file (relative path needed)")
    print("2. Hash a message")
    choice = int(input())
    if choice == 1:
        file_path = input("Enter the relative path to your file: ")
        result = hash_file(file_path)
    elif choice == 2:
        message = input("Enter the message you want to hash: ")
        result = hash_pw(message)
    return result

def integrity_verification():
    file_path1 = input("Enter the first relative file path: ")
    file_path2 = input("Enter the second relative file path: ")
    print(verify_integrity(file_path1, file_path2))

def password():
    while True:
        password1 = getpass("Enter your password: ")
        if check_password_strength(password1).startswith("Weak"):
            print("Please choose a strong password. Try again.")
        else:
            break
    hashed_password = hash_pw(password1)
    verification_attempt = getpass("Re-enter your password to verify.")
    print(verify_password(verification_attempt, hashed_password))

def main():
    menu()
    choice = int(input())
    if choice == 1:
        encryption()
    if choice == 2:
        hashing()
    if choice == 3:
        integrity_verification()
    if choice == 4:
        password()

main()