import random

letters = tuple('AaBbCcDdEeFfGgHhIiJjKkLlMmÑñOoPpQqRrSsTtUuVvWwXxYyZz')
numbers = tuple('0123456789')
special_characters = tuple('!@#$%^&*()-_=+[]{}|;:\',.<>?/~`')

def generate_password(length: int):
  password = []
  
  if (length < 4 or length > 30):
    print('Your length the password is very large or very small')
    return
  
  for _ in range(0, length):
    random_character = random.randint(0, 2)
    character = ''

    if random_character == 0:
      j = random.randint(0, len(letters) - 1)
      character = letters[j]
    elif random_character == 1:
      j = random.randint(0, len(numbers) - 1)
      character = numbers[j]
    elif random_character == 2:
      j = random.randint(0, len(special_characters) - 1)
      character = special_characters[j]
    else:
      j = random.randint(0, len(letters) - 1)
      character = letters[j] 
    
    password.append(character)
  
  return ''.join(password)

# pass_one = generate_password(20)
# pass_two = generate_password(18)
# pass_three = generate_password(16)

# print(pass_one)
# print(pass_two)
# print(pass_three)

if __name__ == '__main__':
  while True:
    print('Generator Password v1.0')
    print('Please enter the desired length for the new password')
    length = input()

    password = generate_password(int(length))

    if password == None:
      print()
      continue

    print(f"Your new password is: {password}")
    break