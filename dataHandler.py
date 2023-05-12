try:
    import os
    import sys
    import subprocess
    import getopt
    import csv
    import mostLeastPopularNames as popNames
    import nameOverTimeInGivenState as nameOTime
    import similarNames
    import printAllStatesWithDictionaries
    import ethnicName
    import pandas as pd
    import compareFunctions
except :
    print("Installing pandas")
    python = sys.executable
    subprocess.check_call([python,'-m', 'pip', 'install', "-U", 'pandas'], stdout=subprocess.DEVNULL)
finally:
    import pandas as pd
    import os
    import sys
    import subprocess
    import getopt
    import csv
    import mostLeastPopularNames as popNames
    import nameOverTimeInGivenState as nameOTime
    import similarNames
    import printAllStatesWithDictionaries
    import ethnicName
    import compareFunctions

genders = {'F': 'female', 'M': 'male'}

def main ( argv ): 
    names    = [] #Set of names to be saved
    frequency  = [] #Set of frequency of names
    tempName = '' #Holder for names
    fileName = '' #Holder for output file name
    currentYear = 0 #Current year counter
    previousyear = 0 #Previous year counter
    parentOrganizedPath = './Data files/OrganizedStates/' #Path that will save all organized states
    stateCodeTuple = () #Empty tuple that will store the tuple that will store the state code and the extention so that the name can be accessed
    stateCode = '' #Saves state code for organizing states
    desiredDirectory = '' #Saves a directory that users will pick for the function finding Similar names
    stopLoop = 1 #A integer that will determine if the user wishes to stop a function call with a loop
    cont = ''
    #This creates a list of all files in the USStates folder in order to iterate through as many states as ar provided
    pathOfFiles = "./Data files/USStates"
    filesList = os.listdir(pathOfFiles)
    while cont.lower() != 'y' and cont.lower() != 'n' :
        cont = input("Are all the files initialized? (y/n) ")
        if cont.lower() != 'y' and cont.lower() != 'n' :
            print("Please input y or n")
    
    if cont != 'y':
        for state in filesList:
            parentOrganizedPath = './Data files/OrganizedStates/' #resets path with every state
            print("Working on " + str(state)[:2] + ".....")
            
            #Saves state code using os function splittext by putting the code in the first element of the tuple and the extention in the second
            stateCodeTuple = os.path.splitext(state)
            stateCode = stateCodeTuple[0]

            stateDirectory = parentOrganizedPath + stateCode

            if os.path.isdir(stateDirectory) == False: #Checks to see if directory for that state's organized data exists
                maleOrganizedPath = os.path.join(stateDirectory, "Male")
                os.makedirs(maleOrganizedPath)
                femaleOrganizedPath = os.path.join(stateDirectory, "Female")
                os.makedirs(femaleOrganizedPath)

            


            with open ( "./Data files/USStates/"+str(state) ) as csvDataFile:
                
                csvReader = csv.reader(csvDataFile, delimiter=',')
                #print("Running...")
                for row in csvReader:
                    currentYear = int(row[2]) #Sets current year
                    #print("I am running " + row[2])
                    if row[3] != ' ' or row[3] != 'NONAME':
                        if str(row[1]) == "F":

                            if currentYear != previousyear: #Checking for year changes
                                
                                #print(fileName)
                                #The section below takes the currently filled arrays of names and frequency, and puts them into the proper format as a dataframe into a new file
                                if previousyear != 0: #A check for the first year, to make sure that the year is saved properly
                                    
                                    people = {'Name':names,'Frequency':frequency} #Putting people and frequency into a dictionary so it can go into a  dataframe
                                    people_df = pd.DataFrame(people)
                                    people_df.to_csv(fileName, sep=',', index=False,mode="w", encoding='utf-8')
                                    tempName = ''
                                    names = [] #Resets the array for use in the next year's dataset
                                    frequency = [] #Resets the array for use in the next year's dataset
                                fileName = "./Data files/OrganizedStates/"+ stateCode+"/Female/" + str(currentYear)+".txt"
                                
                                #These blocks of text add the contents of each row to the corresponding lists
                                tempName = row[3].strip()
                                tempName = row[3].strip()
                                names.append(tempName)
                                frequency.append(int(row[4]))
                            else:
                                tempName = row[3].strip()
                                names.append(tempName)
                                frequency.append(int(row[4]))

                                
                        elif str(row[1]) == "M":
                            if currentYear != previousyear: #Checking for year changes
                                
                                #print(row[2])
                                #The section below takes the currently filled arrays of names and frequency, and puts them into the proper format as a dataframe into a new file
                                if previousyear != 0: #A check for the first year, to make sure that the year is saved properlyx
                                    
                                    people = {'Name':names,'Frequency':frequency} #Putting people and frequency into a dictionary so it can go into a  dataframe
                                    people_df = pd.DataFrame(people)
                                    people_df.to_csv(fileName, sep=',', index=False,mode="w", encoding='utf-8')
                                    tempName = ''
                                    names = [] #Resets the array for use in the next year's dataset
                                    frequency = [] #Resets the array for use in the next year's dataset
                                fileName = "./Data files/OrganizedStates/"+ stateCode+"/Male/" + str(currentYear)+".txt"
                                
                                #These blocks of text add the contents of each row to the corresponding lists
                                tempName = row[3].strip()
                                names.append(tempName)
                                frequency.append(int(row[4]))
                            else:
                                tempName = row[3].strip()
                                names.append(tempName)
                                frequency.append(int(row[4]))
                                
                        else: #Checks to make sure there is a valid sex in every line for the sake of storage in the directory
                            print("File contains an invalid sex, there is no specifier for Sex, please correct file or insert new data")
                            print("File invalid at this row: " + str(row))
                            return -1
                        
                    previousyear = currentYear #Sets previous year

                #Adds the contenets of the final year into its appropriate file
                people = {'Name':names,'Frequency':frequency}
                people_df = pd.DataFrame(people)
                people_df.to_csv(fileName, sep=',', index=False,mode="w", encoding='utf-8')

                print("Done!")
                #print(names)
                #print(fileName)
        
    userSelection = 1

    while(userSelection in range(1,12)):
        print("\nWhich functions would you like to use?")
        print("1 - Most popular female names in a certain state")
        print("2 - Least popular female names in a certain state")
        print("3 - Most popular male names in a certain state")
        print("4 - Least popular male names in a certain state")
        print("5 - Frequency of a name over time in given states")
        print("6 - Find and display all names with more than one way to spell it")
        print("7 - A breakdown of the types of names used in a given year in a given state by demographic")
        print("8 - Copmparing the top 10 most popular names in two given generations in different states")
        print("9 - Most popular names in groups of states (geographic or socioeconomic)")
        print("10 - View and compare top 10 popular names in 2-5 states")
        print("11 - Naming similarity between states")
        print("0 - Exit program\n")
        userSelection = int(input("Please make your selection: "))
        if userSelection not in range(0,12):
            print("Invalid input, please try again")
        else: 
            match userSelection: 
                case 1: 
                    popNames.printPopularNames("Female")
                case 2: 
                    popNames.printLeastPopular("Female")
                case 3: 
                    popNames.printPopularNames("Male")
                case 4: 
                    popNames.printLeastPopular("Male")
                case 5:
                    nameOTime.nameOverTime()
                case 6: 
                    #Resetting user choices
                    stopLoop = 1
                    desiredDirectory = ''
                    selectedGender = ''
                    while os.path.exists(desiredDirectory) == False and stopLoop != "0":
                        print("\nHere's a list of all the states")
                        printAllStatesWithDictionaries.printStateNames()
                        try:
                            selectedState = int(input("Please input the state to look at: "))
                        except:
                            selectedState = -1
                        while int(selectedState) not in range(1, 52): 
                            print("Invalid choice, please enter a number from 1-51")
                            try:
                                selectedState = int(input("Please input the state to look at: "))
                            except ValueError:
                                continue
                        
                        while selectedGender.lower() not in ["m", "f"] :
                            selectedGender = str(input("Please enter the gender you wish to look at (M for male/F for female): "))
                            if selectedGender.lower() not in ["m", "f"]: #If the user inputs anything that is not related to the two sexes, it will make sure they input correctly
                                print("Invalid choice, please type M or F")
                            #Making sure that the user can input the words or the shorthand
                            elif selectedGender.lower() == "m":
                                selectedGender = "M"
                            elif selectedGender.lower() == "f":
                                selectedGender = "F"
                        

                            
                        selectedYear = input("Please select the desired year to look at (1910-2021): ")
                        
                        desiredDirectory = str(parentOrganizedPath) + printAllStatesWithDictionaries.allStateAbbrs[int(selectedState)] + "/" + genders[selectedGender]  + "/" + str(selectedYear) + ".txt"
                        
                        if os.path.exists(desiredDirectory) == False:
                            #print()
                            stopLoop = str(input(f"{desiredDirectory} is not a existing directory, press 0 to exit function, press any other key to continue: "))
                        else:
                            similarNames.openfileAndOutputSimilarNames(desiredDirectory)

                case 7:
                    #Resetting user choices
                    stopLoop = 1
                    desiredDirectory = ''
                    selectedGender = ''
                    while os.path.exists(desiredDirectory) == False and stopLoop != "0":
                        print("\nHere's a list of all the states")
                        printAllStatesWithDictionaries.printStateNames()
                        
                        try:
                            selectedState = int(input("Please input the state to look at: "))
                        except:
                            selectedState = -1
                        while int(selectedState) not in range(1, 52): 
                            print("Invalid choice, please enter a number from 1-51")
                            try:
                                selectedState = int(input("Please input the state to look at: "))
                            except ValueError:
                                selectedState = -1
                        
                        while selectedGender.lower() not in ["m", "f"] :
                            selectedGender = str(input("Please enter the gender you wish to look at (M for male/F for female): "))
                            if selectedGender.lower() not in ["m", "f"]: #If the user inputs anything that is not related to the two sexes, it will make sure they input correctly
                                print("Invalid choice, please type M or F")
                            #Making sure that the user can input the words or the shorthand
                            elif selectedGender.lower() == "m":
                                selectedGender = 'M'
                            elif selectedGender.lower() == "f":
                                selectedGender = "F"
                        
                        selectedYear = input("Please select the desired year to look at (1910-2021): ")
                        
                        desiredDirectory = str(parentOrganizedPath) + printAllStatesWithDictionaries.allStateAbbrs[int(selectedState)] + "/" + genders[selectedGender]  + "/" + str(selectedYear) + ".txt"
                        
                        if os.path.exists(desiredDirectory) == False:
                            #print()
                            stopLoop = str(input(f"{desiredDirectory} is not a existing directory, press 0 to exit function, press any other key to continue:"))
                        else:
                            ethnicName.openfileAndOutput(desiredDirectory)
                case 8:
                    compareFunctions.generationalComp()
                case 9:
                    compareFunctions.compareStateGroups()
                case 10:
                    compareFunctions.compareStates()
                case 11:
                    compareFunctions.stateNamingPatterns()
                case 0: 
                    print("Have a nice day!")
                    break


if __name__ == "__main__":
    main ( sys.argv[1:] )
