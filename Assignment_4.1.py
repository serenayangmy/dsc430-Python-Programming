#DSC 430: Python Programming - 0401: Goldbach Deuce
#Student Name: Serena Yang
#Date: Oct, 10, 2020
#Video Link: https://youtu.be/Gcs8rS9-WNo
#I have not given or received any unauthorized assistance on this assignment.


#ask user the input the list
def asklist():
   #set a while loop if the user input wrong type, rerun this step
   while True:
      #set a ValueError exception
      try: 
         print("Please enter number of elements in the list: (separate them with commas)")
         #stored user's input into the list "setlist"
         setlist = [int(i) for i in raw_input().split(',')]
         #if user input correct type, keep running into the next sub-function
         break
      #if the user type in the wrong value type, print notification
      except ValueError:
         print("That was no valid number. Try again...")
   #return user's input   
   return setlist

#ask the user to input the sum
def asksum():
   #set a while loop if the user input wrong type, rerun this step
   while True:
      #set a ValueError exception
      try:
         #stored user's input as variable "setsum"
         setsum = int(input("Please enter the sum of two numbers: "))
         #if user input correct type, keep running into the next sub-function
         break
      #if the user type in the wrong value type, print notification
      except ValueError:
         print("That was no valid number. Try again...")
   #return user's input  
   return setsum

#binary search, run log(n)
def binarysearch(addend, setlist, i):
   #set the search start from index i
   low = i
   high = len(setlist) - 1

   #set a while loop with the condition
   while low <= high:
      #get the mid index
      mid = (low + high)//2
      #if the middle number equals to the target, return True
      if setlist[mid] == addend:
         return True
      #if the middle number is bigger than the target, reset high index
      elif setlist[mid] > addend:
         high = mid - 1
      #if the midlle number is smaller than the target, reset the low index
      else:
         low = mid + 1
   #otherwise, target is not in the list and return False
   return False


#get two addends by n(logn)
def findSummands(setsum, setlist):
   #set count to get, in case, there are no two numbers in this list add up to the sum user entered
   count = 0
   #sort the list
   setlist.sort()
   print("result: ")
   #set a for loop
   for i in range(len(setlist)):
      #get the another addend
      addend = setsum - setlist[i]
      #if the addend can be found in the setlist, and the two addends do not equal
      if (binarysearch(addend, setlist, i) == True) and (addend != setlist[i]):
         #then print the result and count by 1 time
         print(str(setsum) + " = " + str(setlist[i]) + " + " + str(addend))
         count += 1
      #otherwise, keep running into the next number
      else:
         continue
   #if the count equals to 0, it means there are no two numbers in this list add up to the sum and print the notification
   if count == 0:
      print("There are no two numbers in this list add up to the sum you entered!")

#call main
def main():
   #ask the user to input the list
   setlist = asklist() 
   #ask the user to input the sum
   setsum = asksum()
   #get the results
   findSummands(setsum, setlist)
      
main()