import string
import random

chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    length = int(input("Enter password length: "))

    random.shuffle(chars)

    password = []
    for i in range(length):
        password.append(random.choice(chars))

    random.shuffle(password)

    # converting the list to string
    # printing the list
    print("".join(password))


generate_random_password()
