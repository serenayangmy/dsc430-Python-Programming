#DSC 430: Python Programming - Assignment 0102: Coprime
#Student Name: Serena Yang
#Date: Sep, 20, 2020
#Video Link: https://youtu.be/ug_JvkCXyFs
#I have not given or received any unauthorized assistance on this assignment.

"""Write a function coprime_test_loop() that asks the user for two numbers. This function will pass those two numbers onto a second function"""
def coprime_test_loop():

    #Create a while loop to make sure the whole function running when the user's want to play another around.
    second = 'Yes'
    while second == 'Yes':  

        #get the value a and b from user typing...
        a = input('Please enter the first nubmer: ')
        b = input('Please enter the second number: ')

        #make the types of a and b are integer
        a = int(a)
        b = int(b)

        """second function coprime(a,b) which will return true or false depending on whether or not the numbers are coprime."""
        def coprime(a,b):
            #Start with the smaller of the two Numbers and go to one by one
            for i in range(min(a,b), 0, -1):
                #If it's divisible by both Numbers
                if (a % i == 0 and b % i == 0):
                    #if the number equals to 1, then return True, otherwise return False
                    if (i == 1):
                        return True
                    else:
                        return False
                    #stop the loop, while the function get the T/F
                    break
        
        """The function coprime_test_loop() will print out a message indicating the result. It will then ask the user for another 
        pair of numbers and query coprime(a,b) again. It will continue this loop until the user indicates that they wish to exit the program."""

        #When these two numbers are coprime
        while (coprime(a,b) == True):
            #tell the user the final result and get the reply that whether the user what to play again
            second = input('These two numbers are coprime! Do you want type in another pair of numbers? (Yes/No): \n')
            #if the user doesn't want to play again
            if ('no' in second or 'No' in second or 'NO' in second):
                print('Thank you for playing!')
                break
            #if the user want to play again
            elif ('yes' in second or 'YES' in second or 'Yes' in second):
                #start the loop again
                coprime_test_loop()
            #in case, user typed the wrong option
            else: 
                print('Incorrect option.')
            break
        
        ##When these two numbers are not coprime
        while (coprime(a,b) == False):
            #tell the user the final result and get the reply that whether the user what to play again
            second = input('These two numbers are not Co-Prime! Do you want type in another pair of numbers? (Yes/No): \n')
            #if the user doesn't want to play again
            if ('no' in second or 'No' in second or 'NO' in second):
                print('Thank you for playing!')
                break
            #if the user want to play again
            elif ('yes' in second or 'YES' in second or 'Yes' in second):
                #start the loop again
                coprime_test_loop()
            #in case, user typed the wrong option
            else: 
                print('Incorrect option.')
            break
    

coprime_test_loop()
