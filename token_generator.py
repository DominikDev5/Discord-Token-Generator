import secrets
import string

def random_string(length):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

prefix = "MT"

part1 = prefix + random_string(24)

part2 = random_string(6)

part3 = random_string(38)

token = f"{part1}.{part2}.{part3}"

print(token)
print("Length:", len(token))