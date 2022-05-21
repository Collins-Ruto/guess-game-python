import random


print("Welcome to the guessing game")
print("5 Attempts numbers range from 1 to 40. There will be cues to lead you through. GoodLuck 💪")

number = random.randint(0, 40)
# print(number)
guess = 51

i = 0

while guess != number and i != 5 :
    guess = int(input("Whats your guess: "))

    if guess >= number + 10:
        print("Thats too high, guess lower")
        
    if guess < number + 10 and guess > number:
        print("A litle high, guess a bit lower")
        
    if guess + 10 < number:
        print("Thats too litle, guess higher")
        
    if guess >= number - 10 and guess < number:
        print("litle but close, guess a bit higher")
    
    if i == 3 and guess != number:
        print("One last chance !")
        
    i += 1

if guess != number and i >= 5 :
    print("You loose 😔, the number was: " + str(number))

if guess == number:
        print("🥳 You lucky soul!🎆 You won 🍾🍾")
