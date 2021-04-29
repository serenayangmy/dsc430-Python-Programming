#DSC 430: Python Programming - Assignment 0702: Overlapping Ellipses
#Student Name: Serena Yang
#Date: Nov, 1, 2020
#Video Link: https://youtu.be/qeEYc-SZ9Pg
#I have not given or received any unauthorized assistance on this assignment.

import random
import math

#pseudo random number gengerator, which is from the assignment 7.1
class WarAndPeacePseudoRandomNumberGenerator:
    #inital the variables
    def __init__(self, seed):
        self.seed = seed

    #subfunction random
    def random(self):
        #open the file that we are gonna use
        file = open('/Users/serenayang/Desktop/dsc 430/Assignment/Assignment 7/war-and-peace.txt', 'r')

        #set initals
        lst = []
        count = 0

        #get the first start position by user settig seed
        a = random.randint(3,self.seed)

        #make the loop run 32 times
        if a == 1:
            a = random.randint(3,self.seed)
        else: 
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

#class Point
class Point:
    #set initals
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    #get x,y
    def get(self):
        retrun (self.x, self.y)

#class Ellipse
class Ellipse:
    #set initals
    def __init__(self, p1, p2, w):
        self.p1 = p1
        self.p2 = p2
        self.w = w
    
    #get point1, point2, and the width of axis
    def get(self):
        return (self.p1, self.p2, self.w)

#class compute overlapping area
class computeOverlapOfEllipses:
    #set initals
    def __init__(self, e1, e2):
        self.e1 = (e1, e2)
        self.e2 = (e1, e2)
        self.width_base = 0
        self.width_top = 0
        self.length_base = 0
        self.length_top = 0
        self.square = 0
        self.p_dot = (0,0)
        self.dotx = 0
        self.doty = 0
        self.dotw1 = 0
        self.dotw2 = 0
        self.time = 0

    #set square to conclude two ellipses
    def setsquare(self):
        #set the list includes all the point-x of four points and sort the list
        width_lst = [e1.p1.x, e1.p2.x, e2.p1.x, e2.p2.x]
        width_lst.sort()
        #if the width of the long axis of first ellipse is bigger than the second one
        if e1.w > e2.w:
            #using the smallest point-x - half of the long aixs set as the width_base
            self.width_base = width_lst[0] - e1.w/2
            #using the biggest point-x + half of the long axis set as the width_top
            self.width_top = width_lst[3] + e1.w/2
        
        #if the width of the long axis of first ellipse is smaller than the second one
        elif e1.w < e2.w:
            self.width_base = width_lst[0] - e2.w/2
            self.width_top = width_lst[3] + e2.w/2

        #if they are the same 
        else:
            self.width_base = width_lst[0] - e1.w/2
            self.width_top = width_lst[3] + e1.w/2

        #set the length_base and length_top, using the same logic as width_base and width_top
        length_lst = [e1.p1.y, e1.p2.y, e2.p1.y, e2.p2.y]
        length_lst.sort()
        if e1.w > e2.w:
            self.length_base = length_lst[0] - e1.w/2
            self.length_top = length_lst[3] + e1.w/2
            
        elif e1.w < e2.w:
            self.length_base = length_lst[0] - e2.w/2
            self.length_top = length_lst[3] + e2.w/2
            
        else:
            self.length_base = length_lst[0] - e1.w/2
            self.length_top = length_lst[3] + e1.w/2

        #calculate the square area
        self.square = (abs(self.width_base) + abs(self.width_top)) * (abs(self.length_base) + abs(self.length_top))
        
        #return all the variables
        return (self.square, self.width_base,self.width_top,self.length_base,self.length_top)
    
    #get dots
    def getdot(self):
        
        #compare two width of the long axis of two ellipses
        if(abs(e1.w - e2.w) == 0):
            #if width of the long axis of two ellipses are bigger than 0, then scale the prng number
            if (e1.w // 10) > 0:
                a = (e1.w // 10) * 10
            #otherwise, do not scale
            else: 
                a = 1
        #otherwise, shift
        else:
            a = abs(e1.w - e2.w)

        #set x and y for the random dot
        self.dotx = prng.random() * a
        self.doty = prng.random() * a
        #if the dot is in the square, return dots, otherwise, count time, get extra times of dots
        if self.dotx > self.width_base and self.dotx < self.width_top:
            if self.doty > self.length_base and self.dotx < self.length_top:
                #if the dot fits these two situation, return the dots
                return (self.dotx, self.doty)
            #otherwise, return time
            else:
                self.time += 1
    
    #check wheather the dot is in the overlapping area
    def whetherin(self):
        #get the distance between dots and the point 1
        dota1 = abs(self.dotx - e1.p1.x)
        dotb1 = abs(self.doty - e1.p1.y)
        dotc1 = math.sqrt(dota1**2 + dotb1**2)

        #get the distance between dots and the point 2
        dota2 = abs(self.dotx - e1.p2.x)
        dotb2 = abs(self.doty - e1.p2.y)
        dotc2 = math.sqrt(dota2**2 + dotb2**2)

        #get the distance between dots and the point 3
        dota3 = abs(self.dotx - e2.p1.x)
        dotb3 = abs(self.doty - e2.p1.y)
        dotc3 = math.sqrt(dota3**2 + dotb3**2)

        #get the distance between dots and the point 4
        dota4 = abs(self.dotx - e2.p2.x)
        dotb4 = abs(self.doty - e2.p2.y)
        dotc4 = math.sqrt(dota4**2 + dotb4**2)

        #get the distance between dots and ellipse1's a and ellipse1's b
        self.dotw1 = dotc1 + dotc2
        #get the distance between dots and ellipse2's a and ellipse2's b
        self.dotw2 = dotc3 + dotc4

        
        return(self.dotw1, self.dotw2)

    #get overlapping area
    def calculate(self):
        
        #set initals
        count = 0
        num = 0

        #run 10000 times in totals
        while count < (10000 + self.time):
            #call get dot and whetherin functions
            a = overlap.getdot()
            overlap.whetherin()
            #if the dots is in the overlapping area, count one times
            if (self.dotw1 <= e1.w) and (self.dotw2 <= e2.w):
                num += 1
            count += 1

        #print the num, count, self.square
        print("sqare area: " + str(self.square)+ "\ntotal dots: " + str(count) + "\ndots in the overlapping area: " + str(num))
        #get the area of overlapping of two ellipses and print the result
        area =  num / (count-self.time) * self.square
        print("overlapping area: " + str(area))

            
p1 = Point(0,0)
p2 = Point(0,0)
e1 = Ellipse(p1,p2,2)

p3 = Point(0,0)
p4 = Point(0,0)
e2 = Ellipse(p3,p4,2)

overlap = computeOverlapOfEllipses(e1,e2)

overlap.setsquare()
prng = WarAndPeacePseudoRandomNumberGenerator(12345)
prng.random()
overlap.calculate()
