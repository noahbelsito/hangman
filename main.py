import requests
import time

response = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()
name = input("What's your name? ")
word = response[0]
guesses = ''
turns = 10

print("Hello, " + name + " we are going to play hangman today!")
time.sleep(3)

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won!")
        time.sleep(3)
        break

    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have " + str(turns) + " more guesses.")
        time.sleep(1)

        if turns == 0:
            print('You lose!')
            time.sleep(3)
            break
