import random
import string

def generate_random_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = random.sample(all_characters, length)

    password_str = ''.join(password)

    return password_str

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Password length should be greater than zero.")
    else:
        password = generate_random_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
