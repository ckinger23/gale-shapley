'''
Homework 2: Gale-Shapley Algorithm
Carter King
Dr. Sanders
CS 355 Advanced Algorithms
13 September 2018
Python 3
'''

import sys
proposerOrder = [] #just to store order of proposers between functions


'''
Function: parseProposerFile(filename)
 This function takes a .txt file of strings and creates a dictionary with the proposer as a key value
 and his list as its values
 parameters: filename - a string of the name of the file
 returns: prefDict - a dictionary of the preferences from the file
'''

def parseProposerFile(filename):
    prefDict = {}
    myFile = open(filename, 'r')
    for line in myFile:
        pieces = line.split(':')
        name = pieces[0].strip()
        prefList = []
        if name:
            proposerOrder.append(name) #keep track in the initial order of the proposers
            pref = pieces[1].strip().split(',')
            for i in range(len(pref)):
                pref[i] = pref[i].strip()
                prefList.append(pref[i])
            prefDict[name] = prefList #value for each proposer key is list of preferences
    return prefDict


'''
Function: parseProposedToFile(filename)
 This function takes a .txt file of strings and creates a dictionary with the proposer as a key value
 and a dictionary of his preferences and their values as its value pair
 parameters: filename - a string of the name of the file
 returns: prefDict - a dictionary of the preferences from the file
'''


def parseProposedToFile(filename):
    prefDict = {}
    myFile = open(filename,'r')
    for line in myFile:
        pieces = line.split(':')
        name = pieces[0].strip()
        prefListOfDicts = {}
        if name:
            pref = pieces[1].strip().split(',')
            for i in range(len(pref)):
                pref[i] = pref[i].strip()
                prefListOfDicts[pref[i]] = i #each value in prefernce dictionary is a dictionary itself with is ranking as its value
        prefDict[name] = prefListOfDicts
    return prefDict


'''
Function: galeShapley(proposer, proposedTo)
 This function takes two preference lists and pairs off the inputs to create a perfect, stable matching
 parameters: proposer - a dictionary representing the preference list of the proposer
             proposedTo - a dictionary representing the preference list(implemented as dictionary) of those being proposed to
 returns: A dictionary of matches
'''


def galeShapley(proposer, proposedTo):
    global proposerOrder
    freeProposer = proposerOrder #names of men proposing
    matches = {}

    while (len(freeProposer) != 0):
        proposerName = freeProposer[0] #first person in the queue
        proposerList = proposer[proposerName]
        l = 0
        while proposerName not in matches.keys(): #pull the first preferred woman from list in dictionary first free proposer
            womanName = proposerList[l]  # name of current woman being asked
            if womanName in matches.keys(): #if woman is already matched
                currMatchName = matches[womanName]
                proposerRank = proposedTo[womanName][proposerName] #pulling rank of proposer
                currMatchRank = proposedTo[womanName][currMatchName] #pulling rank of current engagement
                if proposerRank < currMatchRank: #if proposer is higher on pref list
                    del matches[currMatchName] #remove that man from current matches list
                    matches[womanName] = proposerName #woman matched with new man
                    matches[proposerName]= womanName #new man matched with woman
                    freeProposer.append(currMatchName) #add the old man to free proposer list
                    proposer[proposerName].pop(0) #remove person already engaged to incase of break up
                else:
                    proposer[proposerName].pop(0)  #remove girl from list who rejected
            else:
                matches[proposerName] = womanName #engagement since both free
                matches[womanName] = proposerName
                proposer[proposerName].pop(0) #remove person already engaged to incase of break up
        freeProposer.pop(0) #proposer is engaged,pop from queue

    for w in proposedTo.keys():
        del matches[w] #change it to not display 2n matches
    return matches




def main():
    # Show them the default len is 1 unless they put values on the command line
    print(len(sys.argv))
    if len(sys.argv) == 3:
        proposerFile = sys.argv[1]
        proposedToFile = sys.argv[2]
    else:
        proposerFile = input("What file would you like to use for the Proposer? ")
        proposedToFile = input("What file would you like to use for those Proposed to? ")

        proposerPref = parseProposerFile(proposerFile)
        proposedToPref = parseProposedToFile(proposedToFile)

        print("Proposer's preference list: ")
        print(proposerPref)
        print("Preference list of those being proposed to: ")
        print(proposedToPref)
        print("The Gale-Shapley Algorithm produces these matches: ")
        print(galeShapley(proposerPref,proposedToPref))

main()