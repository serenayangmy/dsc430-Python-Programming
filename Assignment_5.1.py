#DSC 430: Python Programming - Assignment 0501: Dice and Cups
#Student Name: Serena Yang
#Date: Oct, 19, 2020
#Video Link: https://youtu.be/ii4LQvMQ-50
#I have not given or received any unauthorized assistance on this assignment.

import random
import sys

#class for six sieded dice - super function
class SixSidedDie:

    #set initial
    def __init__(self, value):
        self.value = 0

    #roll the dice
    def roll(self):
        self.value = random.randint(1,6)
        return self.value

    #return the value
    def getFaceValue(self):
        return self.value

    #print the result
    def __repr__(self):
        return "SixSidedDie({})".format(self.value)

#extend
class TenSidedDie(SixSidedDie):
    #roll the dice
    def roll(self):
        self.value = random.randint(1,10)
        return self.value
    
    #print 
    def __repr__(self):
        return "TenSidedDie({})".format(self.value)

#extend
class TwentySidedDie(SixSidedDie):
    #roll
    def roll(self):
        self.value = random.randint(1,20)
        return self.value

    #print
    def __repr__(self):
        return "TwentySidedDie({}) ".format(self.value)

#make cup conclude dices
class Cup:

    #set initial values
    def __init__(self, timeSix, timeTen, timeTwenty):
        #cup for defualt
        cup = ()
        #sum value
        self.value = 0
        #times for each dices
        self.timeSix = timeSix
        self.timeTen = timeTen
        self.timeTwenty = timeTwenty
        #list for storing for each type of dices
        self.sixList = []
        self.tenList = []
        self.twentyList = []
        #set three dices
        self.a = SixSidedDie(0)
        self.b = TenSidedDie(0)
        self.c = TwentySidedDie(0)
        
    #roll the dices
    def roll(self):
        #set for loop for as many as dice six
        for i in range(self.timeSix):
            #roll once by count one time
            result = self.a.roll()
            #add the result in the list
            self.sixList.append(result)
            #addup the result for each time roll
            self.value += result 

        #set for loop for as many as ten dices
        for i in range(self.timeTen):
            result = self.b.roll()
            self.tenList.append(result)
            self.value += result

        #set for loop for as many as twenty dices
        for i in range(self.timeTwenty):
            result = self.c.roll()
            self.twentyList.append(result)
            self.value += result

        #return value
        return self.value

    #get sum
    def getSum(self):
        return self.value
    
    #print reslut
    def __repr__(self):

        print ("the sum of the dices is {} ".format(self.value))

        #print details by using for loop
        print("Cup(", end=" ")
        for i in range(self.timeSix):
            print ("SixSidedDie({}),".format(self.sixList[i]), end=" ")

        for i in range(self.timeTen):
            print ("TenSidedDie({}),".format(self.tenList[i]), end=" ")

        for i in range(self.timeTwenty):
            if i != self.timeTwenty-1:
                print ("TwentySidedDie({}),".format(self.twentyList[i]), end=" ")
            else:
                print ("TwentySidedDie({})".format(self.twentyList[i]), end="")

        return ")"


#plase comment this part for assignment 5.2 by using """"
"""
dice = SixSidedDie(0)
dice.roll()
dice.getFaceValue()
print(dice)

tendice = TenSidedDie(0)
tendice.roll()
tendice.getFaceValue()
print(tendice)

twentydice = TwentySidedDie(0)
twentydice.roll()
twentydice.getFaceValue()
print(twentydice)

cup = Cup(1,2,1)
cup.roll()
cup.getSum()
print(cup)
"""


