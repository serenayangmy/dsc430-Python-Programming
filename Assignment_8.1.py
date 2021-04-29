#DSC 430: Python Programming - Assignment 0801: Plot Generator
#Student Name: Serena Yang
#Date: Nov, 9, 2020
#Video Link: https://youtu.be/f5vkkzGpeNE
#I have not given or received any unauthorized assistance on this assignment.
import random

#when queried for a plot returns “Something happens”
class SimplePlotGenerator:
    
    #initial variable
    def registerPlotViewer(self, pg):
        self.pg = pg
    
    #in this situation, return "something happens"
    def generate(self):
        return "Something happens" 

#when queried for a plot returns a random plot produced from the seven files, extend SimplePlotGenerator
class RandomPlotGenerator(SimplePlotGenerator):
    #in this situation, return the plot by format
    def generate(self):

        #get each random word from 7 files
        name = random.choice(open('/Users/serenayang/Desktop/folder/plot_names.txt').read().splitlines())
        adjective = random.choice(open('/Users/serenayang/Desktop/folder/plot_adjectives.txt').read().splitlines())
        profesion = random.choice(open('/Users/serenayang/Desktop/folder/plot_profesions.txt').read().splitlines())
        verb = random.choice(open('/Users/serenayang/Desktop/folder/plot_verbs.txt').read().splitlines())
        adjective_evil = random.choice(open('/Users/serenayang/Desktop/folder/plot_adjectives_evil.txt').read().splitlines())
        villian_job = random.choice(open('/Users/serenayang/Desktop/folder/plot_villian_job.txt').read().splitlines())
        villain = random.choice(open('/Users/serenayang/Desktop/folder/plot_villains.txt').read().splitlines())

        #save as the format
        pg = name + ', a ' + adjective + ' ' + profesion + ', must ' + verb + ' the ' + adjective_evil + ' ' + villian_job + ', ' + villain + '.'
        return pg

#when queried for a plot offers the user a list of five random plot_n, select each words from the fives
class InteractivePlotGenerator(SimplePlotGenerator):

    def generate(self):
        #using for loop to get 5 random lines and save in the list 
        namelist = []
        for i in range(5):
            name = random.choice(open('/Users/serenayang/Desktop/folder/plot_names.txt').read().splitlines())
            namelist.append(name)
        #query user to select the name
        namechose = self.pg.queryUser("Chose a hero’s name from the following list: \n" + str(namelist) + '\n')

        #same method as getting plot name
        adjectivelist = []
        for i in range(5):
            adjective = random.choice(open('/Users/serenayang/Desktop/folder/plot_adjectives.txt').read().splitlines())
            adjectivelist.append(adjective)
        adjectivechose = self.pg.queryUser("Chose a adjective from the following list: \n" + str(adjectivelist) + '\n')

        #same method as getting plot name
        profesionlist = []
        for i in range(5):
            profesion = random.choice(open('/Users/serenayang/Desktop/folder/plot_profesions.txt').read().splitlines())
            profesionlist.append(profesion)
        profesionchose = self.pg.queryUser("Chose a profesion from the following list: \n" + str(profesionlist) + '\n')

        #same method as getting plot name
        verblist = []
        for i in range(5):
            verb = random.choice(open('/Users/serenayang/Desktop/folder/plot_verbs.txt').read().splitlines())
            verblist.append(verb)
        verbchose = self.pg.queryUser("Chose a verb from the following list: \n" + str(verblist) + '\n')

        #same method as getting plot name
        adjective_evillist = []
        for i in range(5):
            adjective_evil = random.choice(open('/Users/serenayang/Desktop/folder/plot_adjectives_evil.txt').read().splitlines())
            adjective_evillist.append(adjective_evil)
        adjective_evilchose = self.pg.queryUser("Chose a adjective evil from the following list: \n" + str(adjective_evillist) + '\n')

        #same method as getting plot name
        villian_joblist = []
        for i in range(5):
            villian_job = random.choice(open('/Users/serenayang/Desktop/folder/plot_villian_job.txt').read().splitlines())
            villian_joblist.append(villian_job)
        villian_jobchose = self.pg.queryUser("Chose a villian job from the following list: \n" + str(villian_joblist) + '\n')

        #same method as getting plot name
        villainlist = []
        for i in range(5):
            villain = random.choice(open('/Users/serenayang/Desktop/folder/plot_villains.txt').read().splitlines())
            villainlist.append(villain)
        villainchose = self.pg.queryUser("Chose a villain from the following list: \n" + str(villainlist) + '\n')

        #get plot by format
        pg = name + ', a ' + adjective + ' ' + profesion + ', must ' + verb + ' the ' + adjective_evil + ' ' + villian_job + ', ' + villain + '.'
        return pg


#responsible for displaying the results
#I print to the console, but another viewer could 'extend' me into a advance smany GUI.
class PlotViewer:
    def registerPlotGenerator(self, pv):
        self.pv = pv
        self.pv.registerPlotViewer(self)
    
    #ask the user for some info if there needs me to
    def queryUser(self, str):
        return input(str)
    
    #call generate
    def generate(self):
        print(self.pv.generate())

#responsible for displaying the results
#I use some other means other than the console to interact with the user
class advancePlotViewer(PlotViewer):
    #I will inhereit registerDiceRoller 

    def queryUser(self, str):
        #Here I might pop up a GUI window.
        pass
    
    def generate(self):
        #Here I present the roll in my GUI.
        pass


#---------------------------------------------
pv = PlotViewer()

pv.registerPlotGenerator( SimplePlotGenerator() )
pv.generate()


pv.registerPlotGenerator( RandomPlotGenerator() )
pv.generate()

pv.registerPlotGenerator( InteractivePlotGenerator() ) 
pv.generate()