'''
Finnian Wengerd
01/11/2020
Programming Dictionary

This program allows the user to build their own dictionary with terms and definitions that
they append to a text document on their own schedule. The dictionary can be scanned with both
complete or partial searchable terms and deffinitions

As a long term project I hope to expand this program to have a pleasing GUI.
'''

'''
open/create a text file

main menu{
1. Create Entry
2. Look up
3. Alphabetize
'''
'''with open("Programming_Dictionary.txt", "a+") as file:  #for some reason I cannot append and read with a+
    file.write("I'm here\n")
'''
with open("Programming_Dictionary.txt", "r+") as file:
    text = file.readlines()
    textDict = {}
    #iterate through every other line in text and enter line as a key and line+1 as its value
    count = 2 #start at two keys will be even and values will be odd so as not to deal with 0
    keyNum = 0 #create a tracker for the line being assessed
    for line in text:
        if count %2 == 0:
            textDict[line.rstrip()] = text[keyNum+1].rstrip() #dictionary [key=line : value=keyNum+1] #.rstrip() removes '\n'
            count+=1
            keyNum+=1
        else:
            count+=1  #if the next line is a definition
            keyNum+=1
    print(textDict)        
            
        


    action = int(input("Welcome to your personal Programming Dictionary. Please choose your next move: \n1. Create a new Entry \n2. Search for a term \n3. Alphabetize my dictionary\n"))

    if action == 1:
        newTerm = input("What is the term?")
        #Check if term exists as a key in the text/dictionary
        if newTerm in textDict.values(): #THIS IS NOT WORKING
            action = input("Term already exists. Would you like to: \n1. Redefine \n2. Append a new definition")
        if newTerm not in textDict.values():  #THIS SHOULD BE ITS OWN FUNCTION
            file.write("\n"+newTerm)
            print("new term in place")
            newDef = input("What is the definition? ")
            file.write("\n"+newDef)


    '''    (1) if: create new:
            ask for term:
                if term already exists:
                    print: "That term has already been defined" and show term w/ definition
                    ask if they still want redefine, add new definition, or leave
                if term does not exist:
                    ask for term
                    ask for definition
                    place at the end of the dictionary or text (TBD)
                ask if they want to continue adding terms
                if yes: add{}
                if no: main menu
                '''

    '''(2)if looking up:
        look{
        ask for term or definition
        is this partial or complete?
            if term:
             if partial:
                 search for keys
                  if more than one: list out possible
                  if none: ask if they want to make a new entry
             if complete search for key
                 if more than one: list out possible
                 if none: ask if they want to make a new entry
            if definition
                if partial:
                     search for values
                      if more than one: list out possible
                      if none: ask if they want to make a new entry
                 if complete search for values
                     if more than one: list out possible
                     if none: ask if they want to make a new entry
                     }

            ask if they want to continue searching terms
                if yes: look{}
                if no: main menu
                '''

    '''(3) if alphabetize
         sort txt file by reading as a dictionary and sorting (sorting method TBD)
         send a completion statement
         '''

            

    
    

    
