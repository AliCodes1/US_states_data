#!/usr/bin/env python
import csv
import printAllStatesWithDictionaries as printStates

allStates = {1: 'Connecticut', 2: 'Maine', 3: 'Massachusetts', 4: 'New Hampshire', 5: 'Rhode Island', 6: 'Vermont', 7: 'Delaware', 8: 'District of Columbia', 9: 'Maryland', 10: 'New Jersey', 11: 'New York', 12: 'Pennsylvania', 13: 'Illinois', 14: 'Indiana', 15: 'Iowa', 16: 'Michigan', 17: 'Minnesota', 18: 'Missouri', 19: 'Ohio', 20: 'Wisconsin', 21: 'Kansas', 22: 'Nebraska', 23: 'North Dakota', 24: 'Oklahoma', 25: 'South Dakota', 26: 'Colorado', 27: 'Idaho', 28: 'Montana', 29: 'Utah', 30: 'Wyoming', 31: 'California', 32: 'Oregon', 33: 'Washington', 34: 'Arizona', 35: 'Nevada', 36: 'New Mexico', 37: 'Texas', 38: 'Alabama', 39: 'Arkansas', 40: 'Florida', 41: 'Georgia', 42: 'Kentucky', 43: 'Louisiana', 44: 'Mississippi', 45: 'North Carolina', 46: 'South Carolina', 47: 'Tennessee', 48: 'Virginia', 49: 'West Virginia', 50: 'Alaska', 51: 'Hawaii'}
#dictionary w abbreviations:
allStateAbbrs = {1: 'CT', 2: 'ME', 3: 'MA', 4: 'NH', 5: 'RI', 6: 'VT', 7: 'DE', 8: 'DC', 9: 'MD', 10: 'NJ', 11: 'NY', 12: 'PA', 13: 'IL', 14: 'IN', 15: 'IA', 16: 'MI', 17: 'MN', 18: 'MO', 19: 'OH', 20: 'WI', 21: 'KS', 22: 'NE', 23: 'ND', 24: 'OK', 25: 'SD', 26: 'CO', 27: 'ID', 28: 'MT', 29: 'UT', 30: 'WY', 31: 'CA', 32: 'OR', 33: 'WA', 34: 'AZ', 35: 'NV', 36: 'NM', 37: 'TX', 38: 'AL', 39: 'AR', 40: 'FL', 41: 'GA', 42: 'KY', 43: 'LA', 44: 'MS', 45: 'NC', 46: 'SC', 47: 'TN', 48: 'VA', 49: 'WV', 50: 'AK', 51: 'HI'}

#Dictionary with genders:
genders = {'F': 'female', 'M': 'male'}

#Dictionary with names of state groups
stateGroupCodes = {1: 'Highest Immigration (> 15% of Population)', 2: 'Lowest Immigration (< 5% of Population)', 3: 'Union States', 4: 'Confederate States', 5: 'Wealthiest States Per Capita (2019)', 6: 'Poorest States Per Capita (2019)', 7: 'New England', 8: 'Mid-Atlantic', 9: 'Midwest', 10: 'Great Plains', 11: 'Rocky Mountains', 12: 'West Coast', 13: 'Southwest', 14: 'Southeast'}

#Dictionary with numeric codes of all states in each group
#Highest and lowest immigration from https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_immigrant_population
#Highest and lowest wealth from https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income
#Confederate states from https://en.wikipedia.org/wiki/Confederate_States_of_America
#Union states from https://en.wikipedia.org/wiki/Union_(American_Civil_War)
stateGroups = {1: [31, 10, 11, 40, 35, 51, 3, 37, 9], 2: [49, 28, 44, 30, 38, 2, 42, 25, 43, 18, 23, 39, 19, 6], 3: [31, 1, 13, 14, 15, 21, 2, 3, 16, 17, 35, 4, 10, 11, 19, 32, 12, 5, 6, 49, 20, 8], 4: [46, 44, 40, 38, 41, 43, 37, 48, 39, 47, 45], 5: [8, 3, 1, 10, 9, 11, 33, 4, 26, 48], 6: [24, 27, 42, 43, 38, 36, 49, 39, 44], 7: [1, 2, 3, 4, 5, 6], 8: [7, 8, 9, 10, 11, 12], 9: [13, 14, 15, 16, 17, 18, 19, 20], 10: [21, 22, 23, 24, 25], 11: [26, 27, 28, 29, 30], 12: [31, 32, 33], 13: [34, 35, 36, 37], 14: [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}

#User input for functions that sort by state
def userInputsByState():
    
    confirm = 'y'
    
    #While loop lets user confirm selected states or repeat selection if unhappy
    while (confirm != 'Y'):

        numStates = 0
        numYears = 0
        year = 0
        gender = ' '

        statecodes = []

        while(numStates < 2 or numStates > 5):
            try:
                numStates = int(input(print("\nHow many states would you like to compare (2-5): ")))
            except:
                print("Please enter an integer between 2 and 5.")
            
        print("\nPlease reference the following numbers associated with each state:\n")
        printStates.printStateNames()
        
        #Repeats the state entry process as many times as user requested
        for i in range(0,numStates):
            
            statecodes.append(0)
            #While loops repeats entry if the user enters an invalid value
            while(statecodes[i] < 1 or statecodes[i] > 51 or statecodes[i] in statecodes[0:i]):
                try:
                    statecodes[i] = (int(input(print("Enter the numeric code for your state " + str(i+1) + ": "))))
                except:
                    print("Please enter a number between 1 and 51.")
                    
        while (numYears < 1 or numYears > 111):
            try:
                numYears = int(input(print("Enter a number of years to compare (1-111): ")))
            except:
                print("Please enter an integer between 1 and 111.")

        #User's latest choice for starting year is based on how many years they want to count
        latestChoice = 2021-(numYears-1)
        
        if (latestChoice != 1910):
            while(year < 1910 or year > latestChoice):
                try:
                    year = int(input(print("Enter a year between 1910 and " + str(latestChoice) + " to begin counting from: ")))
                except:
                    print("Please enter a number between 1910 and " + str(latestChoice) + ".")
                    
        else: 
            year = 1910
    
        while(gender != 'F' and gender != 'M'):
            try:
                gender = input(print("Please select a gender to compare (F for female or M for male):")).upper()
            except:
                print("Please enter the single character F or M.")
            
        #Confirms user's choices
        print("To confirm, you would like to compare:")
        for i in range(1,(numStates+1)):
            print(allStates[statecodes[i-1]])
        print("In " + str(year) + " to " + str(year+numYears-1) + " for " + genders[gender] + "s.")
        while(confirm != 'Y' and confirm != 'N'):
            try:
                confirm = input(print("Y or N: ")).upper()
                if confirm != 'Y' and confirm != 'N':
                    print("Please enter Y or N")
            except:
                print("Please enter the single character Y or N.")

    return statecodes, year, numYears, genders[gender]



def userInputsByStateGroup():
    
    numYears = 0
    year = 0
    gender = ' '
    confirm = 'y'
    
    print("\nPlease reference the following numbers associated with each group of states:\n")
    for i in range(0,len(stateGroupCodes)):
        print(str(i+1) + ". " + stateGroupCodes[i+1])
        
    #While loop lets user confirm selected states or repeat selection if unhappy
    while (confirm != 'Y'):
        groupcodes = [0, 0]
        #While repeats entry if user enters an invalid group code
        while groupcodes[0] not in range(1,15):
            try:
                groupcodes[0] = int(input(print("\nEnter the numeric code for your first state group: ")))
            except:
                print("Please enter an integer between 1 and 14.")
        groupcodes[1] = groupcodes[0]
        while groupcodes[1] == groupcodes[0] or groupcodes[1] not in range(1,15):
            try:
                groupcodes[1] = int(input(print("Please enter a different second group of states: ")))
            except:
                print("Please enter a different integer between 1 and 14.")

        while (numYears < 1 or numYears > 111):
            try:
                numYears = int(input(print("Enter a number of years to compare (1-111): ")))
            except:
                print("Please enter an integer between 1 and 111.")
                
        latestChoice = 2021-(numYears-1)
        
        if (latestChoice != 1910):
            year = 0
            while(year < 1910 or year > latestChoice):
                try:
                    year = int(input(print("Enter a year between 1910 and " + str(latestChoice) + " to begin counting from: ")))
                except:
                    print("Please enter an integer between 1910 and " + str(latestChoice) + ".")
                    
        else: 
            year = 1910
        
        while(gender != 'F' and gender != 'M'):
            try:
                gender = input(print("Please select a gender to compare (F for female or M for male):")).upper()
            except:
                print("Please enter the single character F or M.")

        #confirms user's choices
        print("To confirm, you would like to compare " + stateGroupCodes[groupcodes[0]] + " states and " + stateGroupCodes[groupcodes[1]] + " states in " + str(year) + " to " + str(year+(numYears-1)) + " for " + genders[gender] + "s.")
        try:
            confirm = input(print("Y or N: "))
        except:
            print("Please enter the single character Y or N.")

    return groupcodes, year, numYears, genders[gender]



#Sorts names in passed states and returns a dictionary containing all passed states' sorted name data
def sort (states, year, numYears, gender):
    
    names = {}
    sortedNames = {}

    #For each state name data for all chosen years are stored as keys to dictionaries with the percentage popularity as the value
    #These dictionaries are stored as the value of a dictionary with state code as the key
    for i in states:
        
        total = 0.0
        names[i] = {}
        
        for j in range(year, (year+numYears)):
            fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[i]) + "/" + gender + "/" + str(j) + ".txt"
            
            try:
                csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
            #If a file is not found, the code will skip that file and continue running with the others
            except:
                print("File not found at " + allStates[i] + " " + str(j) + ".")
                continue
            #Total is calculated to find percentage values 
            for row in csvFile:
                try:
                    total = total + int(row[1])
                except ValueError:
                    continue
        #Files for the state are read again to store names
        for j in range(year, (year+numYears)):
            fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[i]) + "/" + gender + "/" + str(j) + ".txt"
            
            try:
                csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
            except:
                print("File not found at " + allStates[i] + " " + str(j) + ".")
                continue
                
            for row in csvFile:
                try: 
                    #If the name is already in the dictionary, then the percentage is increased by the percentage popularity of the new instance of the name
                    if row[0] in names[i]:
                        names[i][row[0]] = (names[i][row[0]] + (float(row[1])/total)*100)
                    #If it is not already in dictionary, the percentage is stored    
                    else:
                        names[i][row[0]] = (float(row[1])/total)*100
                except:
                    continue
        #The names are sorted and a list of tuples is stored as the value of the state code key
        sortedNames[i] = sorted(names[i].items(), key=lambda x:x[1], reverse=True)
        
    return sortedNames



#Similar function as sort but works with an entire group of states as one data pool and must be called once for each group of states to be sorted
def groupedStateSort(states, year, numYears, gender):
    total = 0.0
    names = {}
    
    #Calculates total population in the group of states
    for state in stateGroups[states]:
        for currentYear in range(year, year+numYears):
            fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[state]) + "/" + gender + "/" + str(year) + ".txt"
            
            try:
                csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
            except:
                print("File not found at " + allStates[state] + " " + str(currentYear) + ".")
                continue
            for row in csvFile:
                try:
                    total = total + int(row[1])
                except ValueError:
                    continue
    #Sorts all names in the group of states
    for state in stateGroups[states]:
        for currentYear in range(year, year+numYears):
            fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[state]) + "/" + gender + "/" + str(year) + ".txt"
            
            try:
                csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
            except:
                print("File not found at " + allStates[state] + " " + str(currentYear) + ".")
                continue
            for row in csvFile:
                try:
                    if row[0] in names:
                        names[row[0]] = (names[row[0]] + (float(row[1])/total)*100)
                    else:
                        names[row[0]] = (float(row[1])/total)*100
                except ValueError:
                    continue
    sortednames = sorted(names.items(), key=lambda x:x[1], reverse=True)

    #Prints top 10 names
    if len(sortednames) >= 10:
        num = 10
    else:
        num = len(sortednames)
    print("\n" + stateGroupCodes[states] + " Top " + str(num) + ":")
    for x in range(0, num):
        print(str(x+1) + ". " + sortednames[x][0] + " (" +      str(round(sortednames[x][1], 2)) + "%)")
    
    return sortednames



#Similar functionality as groupedStateSort but takes groups of years for only one state at a time
def genSort(gens, state, gender):
    
    total = 0.0
    names = {}
    
    #Calculates generational total population
    for year in range(gens[0], (gens[0]+gens[1])):
        fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[state]) + "/" + gender + "/" + str(year) + ".txt"
        
        try:
            csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
        except:
            print("File not found at " + allStates[state] + " " + str(year) + ".")
            continue
        for row in csvFile:
            try:
                total = total + int(row[1])
            except ValueError:
                continue

    #Sorts names for the whole generation
    for year in range(gens[0], (gens[0]+gens[1])):
        
        fileName = "./Data files/OrganizedStates/" + str(allStateAbbrs[state]) + "/" + gender + "/" + str(year) + ".txt"
        try:
            csvFile = csv.reader(open(fileName, 'r'), delimiter=',')
        except:
            print("File not found at " + allStates[state] + " " + str(year) + ".")
            continue
        for row in csvFile:
            try:
                if row[0] in names:
                    names[row[0]] = (names[row[0]] + (float(row[1])/total)*100)
                else:
                    names[row[0]] = (float(row[1])/total)*100
            except ValueError:
                continue
    sortednames = sorted(names.items(), key=lambda x:x[1], reverse=True)

    #Prints top 10 names for the generation
    if len(sortednames) >= 10:
        num = 10
    else:
        num = len(sortednames)
    print("\n" + gens[2] + " Top " + str(num) + ":")
    for x in range(0, num):
        print(str(x+1) + ". " + sortednames[x][0] + " (" + str(round(sortednames[x][1], 2)) + "%)")
        
    return



#Finds the similarity of names in 2 states
#Takes two lists - MUST be presorted - and the codes of the states they are from
def similarityCheck(stateNames1, stateNames2, statecode1, statecode2):
    
    i = 0
    a = 0
    similarity = 0
    sameNames = []
    avNumNames = (len(stateNames1) + len(stateNames2))/2.0
    
    #Compares two lists index by index
    for i in range(0, len(stateNames1)):
        #Sorts based on which list has more names to ensure all are checked
        if(len(stateNames1) <= len(stateNames2)):
            #Checks the lists index by index to see if there is a match
            if stateNames1[i] == stateNames2[i]:
                #Stores the name, the code for each state and the rank in each state
                sameNames.append([stateNames1[i], [statecode1, i+1], [statecode2, i+1]])
                #Similarity is calculated as a percentage with one point for each identically ranked name and .5 points for each recurring name at different ranks
                similarity = similarity + (1/avNumNames)
            #If they do not match at the same index, checks the entire other list for the name
            else:
                
                for a in range(0, len(stateNames2)):
                    
                    if stateNames1[i] == stateNames2[a]:
                        
                        sameNames.append([stateNames1[i], [statecode1, i+1], [statecode2, a+1]])
                        a = len(stateNames2)
                        similarity = similarity + (0.5/avNumNames)
                        
        else:
            #Repeats the logic in the event the second list is longer
            for a in range(0, len(stateNames2)):
                
                if stateNames1[i] == stateNames2[a]:
                    
                    sameNames.append([stateNames1[i], [statecode1, i+1], [statecode2, a+1]])
                    a = len(stateNames2)
                    similarity = similarity + (0.5/avNumNames)
                    
    #Similarity is multiplied from a decimal to a percentage            
    similarity = similarity*100
    
    #Returns a list of the same names in both states and their ranks, as well as the percent similiarity of the two states
    return sameNames, similarity



#Finds names that are in all lists of states given
def commonNames(sameNames, statecodes):

    #All names that occur in two or more states are stored in a dictionary called same
    same = {}

    #The length of sameNames is the number of comparisons that had to be done between pairs of states
    for i in range(0,len(sameNames)):

        #The length of sameNames[i] is the number of names which were the same in a given comparison of two states
        for j in range(0,len(sameNames[i])):

            #Checks if the name is already in the common names list
            if sameNames[i][j][0] not in same:
                #If it is not, it stores the name as the key to a dictionary value which holds the state codes and ranks thus far
                same[sameNames[i][j][0]] = [sameNames[i][j][1], sameNames[i][j][2]]

            #If it is already in the dictionary, it adds only the ranks at new states
            else:
                if (sameNames[i][j][1]) not in same[sameNames[i][j][0]]:
                    same[sameNames[i][j][0]].append(sameNames[i][j][1])
                if (sameNames[i][j][2]) not in same[sameNames[i][j][0]]:
                    same[sameNames[i][j][0]].append(sameNames[i][j][2])
    return same

    

#See/Compare Top 10 Names of 2-5 States:
def compareStates():
    states, year, numYears, gender = userInputsByState()
    sorted = sort(states, year, numYears, gender)

    #Prints Top 10 names in each state:
    for i in states:
        if len(sorted[i]) > 10:
            num = 10
        else:
            num = len(sorted[i])
        print("\n" + allStates[i] + " Top " + str(num) + ":")
        for x in range(0, num):
            print(str(x+1) + ". " + sorted[i][x][0] + " (" + str(round(sorted[i][x][1], 2)) + "%)")
    
    #Same names:
    sortedNames = []
    sameNames = []
    simScore = []
    c = 0
    w = 0
    s = 1

    #Creates a list of lists containing all sorted names with no other data
    for i in states:
        sortedNames.append([])
        for x in range(0, len(sorted[i])):
            sortedNames[w].append(sorted[i][x][0])
        w = w+1

    #Compares each pair of states once
    for i in range(0, len(states)):
        for t in range(s, len(states)):
            if ((i != t)):
                sameNames.append([])
                simScore.append([0.0])
                sameNames[c], simScore[c][0] = similarityCheck(sortedNames[i], sortedNames[t], states[i], states[t])
                c = c+1
        s = s+1
        
    same = commonNames(sameNames, states)

    print("\nAll common names or the first 10 common names in your selected states are:")

    #Count is a counter to print only the first ten names in all states
    count = 0
    for i in same:
        #Only prints the names which occur in all states
        if len(same[i]) == len(states):
            print("\n" + i + ": ")
            for j in range(0, len(same[i])):
                print("Ranked #" + str(same[i][j][1]) + " in " + allStates[same[i][j][0]])
            #Count increments each time a name in all states is printed and breaks the loop after 10 are found
            count = count + 1
        if count > 9:
            break

    return



#Naming patterns of states
def stateNamingPatterns():
    
    statecodes, year, numYears, gender = userInputsByState()
    sorted = sort (statecodes, year, numYears, gender)

    i = 0
    similarity = []
    sortedNames = []
    w = 0
    
    for i in statecodes:
        sortedNames.append([])
        for x in range(0, len(sorted[i])):
            sortedNames[w].append(sorted[i][x][0])
        w = w + 1
    
    c = 0
    simScore = []
    maxSimScore = 0.0
    j = 1

    #Compares each pair of states once
    for i in range(0, (len(statecodes))):
        if j < len(statecodes):
            for t in range(j, (len(statecodes))):
                if ((i != t)):
                    similarity.append([])
                    simScore.append([0.0])
                    similarity[c], simScore[c][0] = similarityCheck(sortedNames[i], sortedNames[t], statecodes[i], statecodes[t])
                    print(allStates[statecodes[i]] + " and " + allStates[statecodes[t]] + " have a similarity of " + str(round(simScore[c][0], 2)) + "%.")
                    #Stores the maximum similarity score that is found over all iterations
                    if simScore[c][0] > maxSimScore:
                        maxSimScore = simScore[c][0]
                    #Stores state codes of states with the similarity score making a nested list
                    simScore[c].append(statecodes[i])
                    simScore[c].append(statecodes[t])
                    c = c+1
        j = j+1

    print("\nThe most similar states have a similarity of " + str(round(maxSimScore, 2)) + "%. They are:")
    #Finds all pairs of states with the maximum similarity score and prints their names
    for c in range(0, len(simScore)):
        if simScore[c][0] == maxSimScore:
            print(allStates[simScore[c][1]] + " and " + allStates[simScore[c][2]])
    
    printNames = 0

    #Option to further enrich pattern exploration by viewing names that occur in all states
    while printNames != 1 and printNames != 2:
        try:
            printNames = int(input(print("\nWould you like to view the top 10 names which occur in all states (1 or 2)?\n1. Yes\n2. No")))
        except ValueError:
            print("Please enter a valid number")
    if printNames == 1:
        same = commonNames(similarity, statecodes)
        print("\nThe top 10 common names in your selected states are:")

        #Count ensures only the first ten names in all states are printed
        count = 0
        for i in same:
            if len(same[i]) == len(statecodes):
                print("\n" + i + ": ")
                for j in range(0, len(same[i])):
                    print("Ranked #" + str(same[i][j][1]) + " in " + allStates[same[i][j][0]])
                #Count increments each time a name in all states is printed and breaks the loop after 10 are found
                count = count + 1
            if count > 9:
                break

    return



#Compares groups of states
def compareStateGroups():
    
    names = {}
    states, year, numYears, gender = userInputsByStateGroup()
    names[states[0]] = groupedStateSort(states[0], year, numYears, gender)
    names[states[1]] = groupedStateSort(states[1], year, numYears, gender)
    
    #Just names stored:
    sortedNames = []
    w = 0
    for i in states:
        sortedNames.append([])
        for x in range(0, len(names[i])):
            sortedNames[w].append(names[i][x][0])
        w = w+1

    #Because similarityCheck requires only lists of names and indices, it can be run with state group codes instead of state codes
    similarity, simScore = similarityCheck(sortedNames[0], sortedNames[1], states[0], states[1])

    print(f"\nThe similarity of these groups is {str(round(simScore,2))}%.\n")



#Compares generations
def generationalComp():
    
    generations = {1: [1910, 18, 'GI Generation'], 2: [1928, 18, 'Silent Generation'], 3: [1946, 18, 'Baby Boomers'], 4: [1965, 16, 'Generation X'], 5: [1981, 16, 'Millenials'], 6: [1997, 16, 'Generation Z'], 7: [2013, 9, 'Generation Alpha']}
    
    confirm = 'N'
    
    #While loop lets user confirm selected states or repeat selection if unhappy
    while (confirm != 'Y'):
        state = 0
        gen1index = 0
        gen2index = 0
        gender = ' '
        #define generations (range of years)
        print("\nGenerations:")
        print("1. The GI Generation (b. 1910-1927)")
        print("2. The Silent Generation (b. 1928-1945)")
        print("3. The Baby Boomers (b. 1946-1963)")
        print("4. Generation X (b. 1965-1980)")
        print("5. The Millenials (b. 1981-1996)")
        print("6. Generation Z (b. 1997-2012)")
        print("7. Generation Alpha (b. 2013-2021)")
        #Select generations to compare (select 2 of however many)
        while gen1index > 7 or gen1index < 1:
            try:
                gen1index = int(input(print("\nSelect the first generation to compare by reference number: ")))
            except:
                print("Please enter an integer between 1 and 7.")
        while gen2index == gen1index or gen2index < 1 or gen2index > 7:
            try:
                gen2index = int(input(print("Select a different second generation to compare by reference number: ")))
            except:
                print("Please enter a different integer between 1 and 7.")
        #Select gender
        while gender != 'F' and gender != 'M':
            try:
                gender = str(input(print("Please select a gender to compare (F for female or M for male):"))).upper()
                
            except:
                print("Please enter the single character F or M.")
        #Select one state
        print("\nPlease reference the following numbers associated with each state:\n")
        printStates.printStateNames()
        #While repeats entry if user enters an invalid code
        while(state < 1 or state > 51):
            try:
                state = (int(input(print("Enter the numeric code for your selected state: "))))
            except:
                print("Please enter an integer between 1 and 51.")
        #Confirms user's choices
        print("To confirm, you would like to compare:")
        print(generations[gen1index][2] + " and " + generations[gen2index][2] + " in " + allStates[state] + " for " + genders[gender] + "s.")
        try:
            confirm = str(input(print("Y or N: "))).upper()
        except:
            print("Please enter a single character Y or N.")
            confirm = str(input(print("Y or N: "))).upper()

    genSort(generations[gen1index], state, genders[gender])
    genSort(generations[gen2index], state, genders[gender])
