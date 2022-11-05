import random

number = []
attempts = 0

# funciton that makes secret number in range 4 digits in int
def Secret_number():
    for i in range(4):
        # it gives random number between 0 and 9
        a = random.randrange(0, 9)
        # it gives random number to the list called number
        number.append(a)
    # list without repeating digit
    if len(number) > len(set(number)):
        # it reset the list and make a new number
        number.clear()
        Secret_number()
   
print(number)

# function for playing this game
def Game():
    # change a global variable attempts in this function
    global attempts
    # it counts number of attempts
    attempts += 1
    # variable
    bulls = 0
    cows = 0
    print(number)
    # user input 4 digits it is string, necessary to retype to int
    user_choice = input("Enter number, which contains from 4 digits ")
    guess = []
    # loop which makes a list from user choice
    for i in range(4):
        # append user choice to guess list in int variable
        guess.append(int(user_choice[i]))
    for b in range(4):
        for c in range(4):
            if guess[b] == number[c]:
                cows += 1
    # loop controls number of guessed digits and print the results
    for d in range(4):
        if guess[d] == number[d]:
            bulls += 1
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    # all digits are guessed and user won
    if bulls == 4:
        print("You won in ", attempts, " tries!")
    # user doesn't guess all bulls, the game continue
    elif bulls != 4:
        Game()



Secret_number()
Game()



