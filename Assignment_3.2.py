#DSC 430: Python Programming - Assignment 0302: Happy Primes
#Student Name: Serena Yang
#Date: Oct, 5, 2020
#Video Link: https://youtu.be/PApOurPDokE
#I have not given or received any unauthorized assistance on this assignment.

import sys

def asknum():
    while True:
        try: 
            num = input("Which number you want to check? (in number) ")
            break
        
        except NameError:
            print("That was no valid number. Try again...")
        
    return num, int(num)

def checkhappy(num, num1):

    var = 1
    while var==1: 
        save = []
        while(num != 1 ):
            a = list(str(num))
            num = 0
            for i in a:
                num = num + int(i)**2

            loopprint(num, a)
            if (num == num1 or num in save):
                break
            else: 
                save.append(num)
        return num

def checkprime(num):
    prime = 0
    if num > 1: 
      
        # Iterate from 2 to n / 2  
        for i in range(2, num): 
         
            # If num is divisible by any number between  2 and n / 2, it is not prime  
            if (num % i) == 0: 
                prime = 0 
                break
        else: 
            prime = 1 
  
    else: 
        prime = 0

    return prime


def loopprint(num, a):

    for i in range(len(a)):
        if i == len(a)-1:
            sys.stdout.write(str(a[i]) + "^2 ")
        else:
            sys.stdout.write(str(a[i]) + "^2 + ")
    print("= " + str(num))



def resultprime(num, prime, num1):
    if (num == 1 and prime == 0):
        print(str(num1) + ' is a happy non-prime!')
        
    elif (num == 1 and prime == 1):
        print(str(num1) + ' is a happy prime!')
       
    elif (num == num and prime == 0): 
        print(str(num1) + ' is a sad non-prime!')
       
    elif (num == num and prime == 1):
        print(str(num1) + ' is a sad prime!')


def main():
    num, num1 = asknum()
    prime = checkprime(num1)
    num = checkhappy(num, num1)
    resultprime(num, prime, num1)

main()