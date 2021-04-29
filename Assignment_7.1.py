#DSC 430: Python Programming - Assignment 0701: War and Random Numbers
#Student Name: Serena Yang
#Date: Nov, 1, 2020
#Video Link: https://youtu.be/wKXxTkJpnbM
#I have not given or received any unauthorized assistance on this assignment.

import random
import math

#pseudo random number gengerator
class WarAndPeacePseudoRandomNumberGenerator:
    #inital the variables
    def __init__(self, seed):
        self.seed = seed

    #subfunction random
    def random(self):
        #open the file that we are gonna use
        file = open('/Users/serenayang/Desktop/dsc 430/Assignment/Assignment 7/war-and-peace.txt', 'r')

        #set inital
        lst = []
        count = 0

        #get the first start position by user settig seed
        a = random.randint(3,self.seed)
        
        #make the loop run 32 times
        while count < 32:
            
            #set the first letter pointer
            file.seek(a)
            #only read one letter
            x = file.read(1)
            
            #set the second letter pointer which is 100 steps from the first one, and only read one letter
            b = a+100
            file.seek(b)
            y = file.read(1)

            #if the first letter is bigger than the second one
            if x > y:
                #add '1' into the list, counter +1, set the second first pointer
                lst.append(1)
                count += 1
                a = b + 100
            #if the first letter is smaller than the second one
            elif x < y:
                #add '0' into the list, counter +1, set the second first pointer
                lst.append(0)
                count += 1
                a = b + 100
            #if these two letters are the same, only set the next first pointer without counting
            elif x == y:
                a = b + 100

        #calculate the prng number by using 32 0/1s
        number = 0
        #using for loop to read 32 0/1s from the list and using in the function
        for i in range(32):
            number += lst[i] * pow((1/2),(i+1))

        #return the prng number and close the file
        return number
        file.close()

    #get min, max, mean results
    def result(self):
        #set inital
        lst =[]
        total = 0
        
        #since we need to generate 10000 prng
        for i in range(10001):
            #everytime call the "random" function and add into the list and calculate the sum
            r = prng.random()
            lst.append(r)
            total += r

        #sort the list 
        lst.sort()
        #get the min, max, and mean
        min = lst[0]
        max = lst[9999]
        mean = total / 10000
        
        #print results
        print("min: " + str(min))
        print("max: " + str(max))
        print("mean: " + str(mean))


prng = WarAndPeacePseudoRandomNumberGenerator(12345)
prng.random()
prng.result()