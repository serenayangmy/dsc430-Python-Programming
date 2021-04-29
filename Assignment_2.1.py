#DSC 430: Python Programming - Assignment 0201: Stem-and-Leaf Design
#Student Name: Serena Yang
#Date: Sep, 27, 2020
#Video Link: https://youtu.be/-Ch_1hOCaZI
#I have not given or received any unauthorized assistance on this assignment.


print("Hello! Welcome to the Stem and Leaf Design! ")

#function for getting the file number that user choose
def meetuser():

    filenumber = input("Which file do you want to choose? (1/2/3): " )
    
    return filenumber
        
#to check whether the user input is in a correct format     
def wrongnumber(filenumber):
    
    #if the input = 1 2 3, then return T, otherwise return F and print notice
    if (filenumber == "1" or filenumber == "2" or filenumber == "3"):
        print("check")
        return True
    else:
        print("Typed wrong filenumber! Please start over! ")
    return False        

#open the file by url, copy and convert the file into a new list as integer
def getfile(filenumber):
    #set a new list called data
    data = []
    
    #set file url
    file = "/Users/serenayang/Desktop/dsc 430/Assignment/Assignment 2 data/StemAndLeaf" + filenumber + ".txt"
    
    #open the file and read
    infile = open((file), "r")
    #read each line and store into lineList
    lineList = infile.readlines()
    #close the file
    infile.close()

    #using for loop to read each line in lineList
    for i in range(0, len(lineList)):
        #store and convert each line as x
        x = int(lineList[i].strip())
        #add x into the new list: data
        data.append(x)

    #sort the data list
    data.sort()
    return data
    
def getstem(data):
    #create sn new list for stem 
    stem = []

     #check one by one in the dataset
    for i in data:
        #if the number //10 is not in the stem list
        if ((i//10) not in stem):
            #then add the stem into the stem list
            stem.append(i//10)

    #let stem list rank from small to large
    stem.sort()
    return stem

#to get the stem list and leaf list
def getstemleaf(data, stem):
    #create two new list for stem and leaf
    leaf = []

    #get the stem one by one from the stem list
    for i in stem:
        temp = []
        #get the number one by one from the dataset
        for j in data:
            #if the number //10 equals to stem(i)
            if (j // 10 == i):
                #then add the remainder of j which is the leaf into the temp list
                temp.append(j % 10)
        
        #add leaf into the list and sort the leaf list
        leaf.append(temp)
        sorted(leaf)   

    return stem,leaf

#to draw the stem_leaf plot
def getplot(stem, leaf, filenumber):
    print("This result for file " + filenumber + " is:")

    #by using for loop to get stem[i] and sublist i of leaf list
    for i in range(len(stem)):
        print (str(i+1), '|', leaf[i], sep = ' ') 
        
    return True

#ask user whether he wants to play again
def playagain():

    #get the answer
    again = input("Do you still want to play again: (Yes/No) \n ")
    
    #if the user want to play again
    if ('yes' in again or 'YES' in again or 'Yes' in again):
        main()
    #if the user doesn't want to play again
    elif ('no' in again or 'No' in again or 'NO' in again):
        print('Thank you for playing!')
        return False  
    #in case, user typed the wrong option
    else: 
        print("Incorrect option.")
        playagain()
         
#call all the function in main
def main():
    
    #function for getting the file number that user choose
    filenumber = meetuser()

    #to check whether the user input is in a correct format     
    while (not wrongnumber(filenumber)):
        filenumber = meetuser()

    #open the file by url, copy and convert the file into a new list as integer    
    data = getfile(filenumber)

    #get stem list
    stem = getstem(data)

    #to get the leaf list
    stem,leaf = getstemleaf(data,stem)

    #to draw the stem_leaf plot
    getplot(stem, leaf, filenumber)

    #ask user whether he wants to play again
    if playagain():
        return False

main()