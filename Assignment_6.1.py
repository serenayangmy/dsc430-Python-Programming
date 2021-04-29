#DSC 430: Python Programming - Assignment 0601: Palindrome Dates
#Student Name: Serena Yang
#Date: Oct, 25, 2020
#Video Link: https://youtu.be/ii4LQvMQ-50
#I have not given or received any unauthorized assistance on this assignment.

#Create dates and pass the date to function checkPalindrome
def Palindrome():
    #set count
    count = 0

    #set range of years
    for year in range(2000, 2100):
        #set range of months
        for month in range(1, 13):
            #since all years in the 21st century start with "2", so we only need to check February
            if month == 2:
                #Since we do not need to consider leap year, set range of days from 1 to 28
                for day in range(1,29):
                    #add "0" before days when days is smaller than 10
                    dd = "%02d" % day
                    mm = "%02d" % month
                    #pass all datas to checkPalindrome
                    count = checkPalindrome(dd,mm,year, count)
            """
            elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
                for day in range(1, 32):
                    dd = "%02d" % day
                    mm = "%02d" % month
                    count = check(dd,mm,year,count)
            elif  month == 4 or month == 6 or month == 9 or month == 11:
                for day in range(1,31):
                    dd = "%02d" % day
                    mm = "%02d" % month
                    count = check(dd,mm,year, count)
            """
        
    return count

#check whether the date is Palindrome
def checkPalindrome(dd,mm,year,count):
    #convert date into str and save as date
    date = str(dd) + str(mm) + str(year)
    #remove space
    date.replace(' ','')
    #if the forward string is equal to the backward string, then, the date is palindrome
    if date == date[::-1]:
        #print the result with slash and count add 1
        print (dd,mm,year,sep = '/')
        count += 1

    return count 

#call Palindrome function and print the final counts
def main():
    count = Palindrome()
    print ("total count: "+ str(count))
    
main()
        