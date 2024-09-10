'''This is a normal password generator project in 
python--'''

import secrets
import string

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += secrets.choice(alphabet)

        # Check password strength after generation
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True

    return pwd

if __name__ == '__main__':
    print(create_pw())  # Calling the function to generate and print the password
