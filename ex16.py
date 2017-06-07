import random
import string

def get_random_letter():
    letter = string.ascii_lowercase[random.randint(0, 25)]
    upper = random.randint(0, 1)
    if upper:
        return letter.upper()
    return letter

def get_random_number():
    return random.randint(0, 9)

def generate_random_string(length):
    count = 0
    password = []
    while count < length:
        letter = random.randint(0, 1)
        if letter:
            password.append(get_random_letter())
        else:
            password.append(str(get_random_number()))
        count += 1
    return "".join(password)


length = input("Password length: ")
pw = generate_random_string(int(length))
print(pw)
