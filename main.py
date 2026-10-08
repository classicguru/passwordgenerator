import time
import random
print("Welcome to Password Generator 2.0, We will generate a password in a second")
time.sleep(1) # This just adds a bit of delay

with open("words.txt", "r") as file:
    word = file.read().split()
randomword = random.choice(word)
num = random.randint(10,99) # This generates a number 10-99
print("Your new password is: " + str(randomword) + str(num )) # We need to add these as a string otherwise the program will crash
