#DSC 430: Python Programming - Assignment 0301: Goldbach's Conjecture
#Student Name: Serena Yang
#Date: Oct, 5, 2020
#Video Link: https://youtu.be/FrgA1-6yRbM
#I have not given or received any unauthorized assistance on this assignment.

#ask the user to input the range
def askrange():
    #set a while loop if the user input wrong type, rerun this step
    while True:
        #set a ValueError exception
        try: 
            setrange = int(input("Please enter the range number that you want to interate over the integers 4 through? (in number) "))
            #if user input correct type, keep running into the next sub-function
            break
        #if the user type in the wrong value type, print notification
        except ValueError:
            print("That was no valid number. Try again...")
    #store user's input   
    return setrange

#check if the addend is a prime number
def checkprime(n):

    #since 1 is not prime number, if n <= 1, return false saying n is not a prime number
    if n <= 1:
        return False

    #set a for loop with starting from 2 and end with n
    for i in range (2, n):
        #if n is divisible by i, return false which n is not a prime number
        if n % i == 0:
            return False
    #otherwise, return n is prime number
    return True

#get two prime addends
def Goldbach(setrange):
    
    #set a nested loop for the sum, start with range of 4 to setrange+1, increment with 2 everytime(even number)
    for a in range(4, setrange+1, 2):
        #set another loop for the first addend, with range of 4 to a
        for b in range(2, a):
            #the second addend equals a-b
            c = a-b
            #if addend b and c are all prime by using checkprime subfunction
            if checkprime(b) and checkprime(c):
                #then print out the result for a everytime
                print(str(a) + " = " + str(b) + " + " + str(c))
                #once print one time for b, junp out from the inside loop, keep running into the outside loop.
                break
      
#call main
def main():
    #ask the user to input the range
    setrange = askrange() 
    #get two prime addends, and call the checkprime subfunction to check if each addend is a prime number in the goldbach function
    Goldbach(setrange)
     
main()

