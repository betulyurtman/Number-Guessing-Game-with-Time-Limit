#Number guessing game

#Importing the necessary libraries.
import random 
import time 

#To make the game more interesting, I limited the time of the game.
time_limit = 10

#Starting the timer
start_time = time.time()

#Created a random number between 1 and 100 for the game.
correct_number = random.randint(1,100)

#I also limited the chance of guess to 5.
guess_chance = 5

#To count the guess, I created a count variable and started it from 0.
count = 0

#Created a while loop that runs while count is smaller than the chance of guess.
while count < guess_chance:
    #Increasing the count by 1 for every guess.
    count += 1
    #Taking the guess of the player.
    guess = int(input("Please guess an integer number between 1 and 100. \n\nYou have 5 chance and 10 seconds to guess the correct number. \n\nYour guess: "))            
    #If guess is correct: 
    if guess == correct_number:
        print("Congrats, your guess is correct!")
        break
    #Directing the player to the correct answer.
    elif guess < correct_number:
        print("\n**Guess higher.")
    elif guess > correct_number:
        print("\n**Guess lower.")

    #Checking the time and guessing chance limits
    if time.time() - start_time > time_limit or count == guess_chance:
        #If the time played is greater than the time limit, the game will stop.
        if time.time() - start_time > time_limit:
            print("\n:( Sorry, you ran out of time! The correct answer was", correct_number, ".")
            break
        #If the number of guesses exceeds the number of guess chances, the game will stop.
        else: 
            print("\nPhew! You are out of chances. I believe in you, you can guess the number next time!") 
            break
