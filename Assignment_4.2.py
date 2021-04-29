#DSC 430: Python Programming - Assignment 0402: Human Pyramid
#Student Name: Serena Yang
#Date: Oct, 11, 2020
#Video Link: https://youtu.be/75Q39HltD5k
#I have not given or received any unauthorized assistance on this assignment.

#get user's input of row and column
def getinput():

    #ask the user to input row number 
    while True:
        try: 
            #store the value as variable "row"
            row = int(input("Which row you want to check? "))
            break
        
        #print out the notification if the input value is not right
        except ValueError:
            print("That was no valid number. Try again...")

    #ask user to input column number 
    while True:
        try: 
            #store the value as variable "column"
            column = int(input("Which column you want to check? "))
            break
        
        #print out the notification if the input value is not right
        except ValueError:
            print("That was no valid number. Try again...")

    #return the row and column value
    return row, column


#to check whether user's input is in the right range of the pyramid
def check(row, column):

    #if the column is bigger than the row, it means the checking point is out of the range
    if row < column:
        #then, print out the notification and return False
        print("Out of range, please restart!")
        return False
    #otherwise, keep running the function humanPyramid
    else:
        return humanPyramid(row, column)
    

#to caculate each number by user's input
def humanPyramid(row, column):

    #base case of the recursive function
    #if the row equals to 0, which is the top one, then print out 0
    if row == 0:
        number = 0
    #if the column equals to 0, which is the first number of each row
    elif column == 0:
        number = (humanPyramid(row - 1, column) + 128) / 2
    
    #if the column equals to the row, which is the last number of each row
    elif row == column:
        number = (humanPyramid(row - 1, column -1) + 128) / 2
    
    #other center points
    else:
        number = 128 + (humanPyramid(row - 1, column - 1) / 2) + (humanPyramid(row - 1, column) / 2)
    
    #return the value
    return number
 
#call main   
def main():

    #get user's input of row and column value
    row, column = getinput()
    #to check whether the input is in the range of the pyramid, if do, run the function humanPyramid and return the value
    number = check(row, column)
    #print out the finnal result
    print("humanPyramid(" + str(row) + "," + str(column) + ")=" + str(number))
    
main()
