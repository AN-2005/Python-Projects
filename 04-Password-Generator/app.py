import random
import string

print("================ Password Generator ================")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("\nGenerated Password:")
    print("".join(password))