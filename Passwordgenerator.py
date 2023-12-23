import secrets
import string

def create_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

length = int(input("enter your digit"))
password = create_password(length)
print("Password:", password)

