#DSC 430: Python Programming - Assignment 0101: Grading Logic
#Student Name: Serena Yang
#Date: Sep, 20, 2020
#Video Link: https://youtu.be/5TBuUdaM6C8
#I have not given or received any unauthorized assistance on this assignment.

def main():
    
    """ If the assignment is not submitted as a single uncompressed .py file, the grade is 0. """  

    #get the answer of whether the student compress the file from user typing...
    filetype = input('Did the student submit the assignment as a single uncompressed .py file? (Yes/No)：\n')
    
    #use if statement to filter student's grade, if the user typed "no"
    if ('no' in filetype or 'No' in filetype or 'NO' in filetype):  

        #if the student didn't compress the file, int grade = 0                                                                    
        grade = 0  
        #if the student gets 0, print the statements
        print('Final score of the student is ' + str(grade) + '.')

    #else if the user typed "yes"
    elif ('yes' in filetype or 'Yes' in filetype or 'YES' in filetype):

        """If the assignment does not include the author’s name and date, the grade is 0."""

        #get the answer of whether the student include the name and date from user typing...
        includename = input('Did the student include the authors name and date? (Yes/No):\n')   
        
        #use if statement to filter student's grade, if the user typed "no"
        if ('no' in includename or 'No' in includename or 'NO' in includename): 

            #if the student didn't include the name in the file, int grade = 0 
            grade = 0

            #if the student gets 0, print the statements
            print('Final score of the student is ' + str(grade) + '.')

        #else if the user typed "yes"
        elif ('yes' in includename or 'Yes' in includename or 'YES' in includename):

            """If the assignment does not include the honor statement, “I have not given or received any
            unauthorized assistance on this assignment”, the grade is 0"""

            #get the answer of whether the student include the honorcode from user typing...
            honorcode = input('Did the student include the honor statement, “I have not given or received any unauthorized assistance on this assignment”? (Yes/No): \n')

            #use if statement to filter student's honorcode, if the user typed "no"
            if ('no' in honorcode or 'No' in honorcode or 'NO' in honorcode):
                #if the student didn't include the honrcode in the file, int grade = 0
                grade = 0

                #if the student gets 0, print the statements
                print('Final score of the student is ' + str(grade) + '.')

            #else if the user typed "yes"
            elif ('yes' in honorcode or 'Yes' in honorcode or 'YES' in honorcode):

                """If the assignment does not include a link to an unlisted 3-minute YouTube video presenting the
                code and answering the assigned questions, the grade is 0."""

                #get the answer of whether the student include the video link from user typing...
                videolink = input('Did the student include a link to an unlisted 3-minute YouTube video presenting the code and answering the assigned questions? (Yes/No): \n')
                
                #use if statement to filter student's video link, if the user typed "no"
                if ('no' in videolink or 'No' in videolink or 'NO' in videolink):

                    #if the student didn't include the video link in the file, int grade = 0
                    grade = 0   
                
                     #if the student gets 0, print the statements
                    print('Final score of the student is ' + str(grade) + '.')

                #else if the user typed "yes"
                elif ('yes' in videolink or 'Yes' in videolink or 'YES' in videolink):
                    """If the assignment satisfies all of the above conditions...
                        o Up to ten points are awarded based on the correctness of the code; that is, how well it meets the given specifications.
                        o Up to ten points are awarded based on the elegance of the code(data structure selection, algorithm efficiency, function implementation, etc.).
                        o Up to ten points are awarded based on the code hygiene (white space, docstrings, etc.).
                        o Up to ten points are awarded based on the quality of the discussion in the YouTube video."""

                    #get the answer of how many score on the correctness from user typing...
                    correctness = input('How many score does the student get on the correctness of the code? (Up to ten points): \n')

                    #use if statement to filter user's typing, if the user typed in the wrong score range
                    if (int(correctness) > 10 or int(correctness) < 0):

                        #since the user typed wrong score, notice user and end the function to start over.
                        print('Typed the wrong score, please start over!')
                        return

                    #if the user typed grade in the right range
                    else:

                        #caculating the grade
                        grade = 0 + int(correctness)

                        #get the answer of how many score on the elegance from user typing...
                        elegance = int(input('How many score does the student get on the elegance of the code(data structure selection, algorithm efficiency, function implementation, etc.)？(Up to ten points): \n'))
                        
                        #use if statement to filter user's typing, if the user typed in the wrong score range
                        if (elegance > 10 or elegance < 0):

                            #since the user typed wrong score, notice user and end the function to start over.
                            print('Type the wrong score, please start over!')
                            return

                        #if the user typed grade in the right range
                        else:

                            #caculating the grade
                            grade = grade + elegance

                            #get the answer of how many score on the code hygiene from user typing...
                            hygiene = int(input('How many score does the student get on the code hygiene (white space, docstrings, etc.)? (Up to ten points): \n'))

                            #use if statement to filter user's typing, if the user typed in the wrong score range
                            if (hygiene > 10 or hygiene < 0):

                                #since the user typed wrong score, notice user and end the function to start over.
                                print('Type the wrong score, please start over!')
                                return
                            
                            #if the user typed grade in the right range
                            else:

                                #caculating the grade
                                grade = grade + hygiene

                                #get the answer of how many score on the Youtube from user typing...
                                quality = int(input('How many score does the student get on the quality of the discussion in the YouTube video? (Up to ten points): \n'))

                                #use if statement to filter user's typing, if the user typed in the wrong score range
                                if (quality > 10 or quality < 0):

                                    #since the user typed wrong score, notice user and end the function to start over.
                                    print('Type the wrong score, please start over!')
                                    return
                                
                                #if the user typed grade in the right range
                                else:

                                    #caculating the grade
                                    grade = grade + quality

                                    #get the answer of whether the student submit late from user typing...
                                    late = input('Did the student submit the assignment late? (Yes/No): \n')

                                    #use if statement to filter student's late submission, if the user typed "no"
                                    if ('no' in late or 'No' in late or 'NO' in late):

                                        #print the final result
                                        print('Final score of the student is ' + str(grade) + '.')

                                    #use if statement to filter student's late submission, if the user typed "yes"
                                    elif ('yes' in late or 'Yes' in late or 'YES' in late):
                                        
                                        """Late assignments lose 1% (of total possible) per hour."""

                                        #get the answer of how many hours does the student submit late from user typing...
                                        hours = int(input('How many hours did the student submit late? \n') )

                                        #caculating the grade
                                        grade = (100 - hours * 1) * grade / 100
                                        
                                        #print the final result
                                        print('Final score of the student is ' + str(grade) + '.')
                                    return
                                return
                            return
                        return
                    return
                else:
                    print('Wrong type, please start over!')
                return
            else:
                print('Wrong type, please start over!')
            return
        else:
            print('Wrong type, please start over!')
        return 
    else:
        print('Wrong type, please start over!')
    return 
main()
