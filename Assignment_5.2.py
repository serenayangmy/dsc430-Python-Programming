#DSC 430: Python Programming - Assignment 0502: Cups and Dice
#Student Name: Serena Yang
#Date: Oct, 18, 2020
#Video Link: https://youtu.be/a1J647Bb5-c
#I have not given or received any unauthorized assistance on this assignment.


#import the Cup function from Dice file which is Assignment5.1 file
from Dice import Cup
import random

#class game:

#get user's name and set inital balance = 100
def meetUser():
    name = input("Welcome to the Cups and Dice! May I have your name please? ")
    print("Hello " + name + ", your inital balance is 100 dolars.")
    balance = 100
    return balance, name

#ask player's whether he wants to play
def play():
    #get the answer
    option = input("Would you like to play a game? ")
    
    #if the user want to play again
    if ('yes' in option or 'YES' in option or 'Yes' in option):
        return True

    elif ('no' in option or 'No' in option or 'NO' in option):
        print('See you later!')
        return False

    #in case, user typed the wrong option
    else: 
        print("Incorrect option.")
        play()

#get bet value from user
def betValue():
    while True:
        try: 
            bet = int(input("How much would you like to bet? "))
            break 

        except ValueError:
            print("That was invalid number. Try again...")

        except SyntaxError:
            print("That was invalid number. Try again...")

    #if the bet value is smaller than or equal to 0, then ask for typing again 

    #if bet is greater than 0, return bet value, otherwise, ask again
    if bet > 0:
        return bet

    elif bet < 0 or bet == 0:
        print("That was invalid value, it must be greater than 0. Try again...")
        return betValue()

#get times of each dices  
def getTimes():
    #get times of dice six
    while True:
        try: 
            sixtime = int(input("How many of die six would you like to roll? "))
            break
        except ValueError:
            print("That was no valid number. Try again...")

        except SyntaxError:
            print("That was no valid number. Try again...")

    #get times of dice ten
    while True:
        try: 
            tentime = int(input("How many of die ten would you like to roll? "))
            break
        
        except ValueError:
            print("That was no valid number. Try again...")

        except SyntaxError:
            print("That was no valid number. Try again...")

    #get times of dice twenty
    while True:
        try: 
            twentytime = int(input("How many of die twenty would you like to roll? "))
            break
        
        except ValueError:
            print("That was no valid number. Try again...")

        except SyntaxError:
            print("That was no valid number. Try again...")
    
    return sixtime, tentime, twentytime


#start rolling by using Cup function from Dice file
def startgame(name, balance, bet, sixtime, tentime, twentytime): 
    
    #set the goal
    goal = random.randint(1,100)
    #call Cup function by passing times of each dice
    value = Cup(sixtime,tentime,twentytime)
    #shake the cup
    result = value.roll()

    #compare the result to goal, and caculate the balance
    if (result == goal):
        balance = balance + 10 * bet
    elif (result <= goal + 3 and result >= goal - 3):
        balance = balance + 5 * bet
    elif (result <= goal + 10 and result >= goal - 10):
        balance = balance + 2 * bet
    else:
        balance = balance - bet

    #print the results
    print ("the goal is: " + str(goal) + ", and the result for the dices is: " + str(result))
    print("name: " + name)
    print("updated balance: " + str(balance))   
    
    return balance 
    
#ask user whether wants to play again
def playagain():
    option = input("Would you like to play one more around? ")
    
    #if the user want to play again
    if ('yes' in option or 'YES' in option or 'Yes' in option):
        return True
        
    #if the user doesn't want to play again
    elif ('no' in option or 'No' in option or 'NO' in option):
        print('See you later!')
        return False

    #in case, user typed the wrong option
    else: 
        print("Incorrect option.")
        playagain()

    #call all function in main
def main():
    balance, name = meetUser()
    #at beginning ask user whether want to play.
    while True:
        if play() == False:
            return False
        else: 
            break
    
    bet = betValue()
    sixtime, tentime, twentytime = getTimes()
    balance = startgame(name, balance, bet, sixtime, tentime, twentytime)
    #if the user wants to play again, keep the while loop running; otherwise, exit..
    while True:
        if playagain() == False:
            return False
        else: 
            bet = betValue()
            sixtime, tentime, twentytime = getTimes()
            balance = startgame(name, balance, bet, sixtime, tentime, twentytime)

main()


