import random


print("---Guess my number---")
print("You need to guess a number")
print("Number is in range 1 and 100")
magic_number = random.randint(1, 100)
count = 0
user_number = 0
if magic_number >= 50:
    print("It is more then 50")
if magic_number <= 50:
    print("It is less than 50")
if magic_number == 50:
    print("from 20 to 80")
while user_number != magic_number:
    user_number = int(input("Your number: "))
    count += 1
    if magic_number > user_number:
        print("Your guess is too low")
    elif magic_number < user_number:
        print("Your guess is too hige")
print("You win. It on the",count,)

