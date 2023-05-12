import os
import sys
import getopt
import csv
import pandas as pd
import printAllStatesWithDictionaries as printStates
#A directory of all state codes with assigned numbers
allStateAbbrs = {1: 'CT', 2: 'ME', 3: 'MA', 4: 'NH', 5: 'RI', 6: 'VT', 7: 'DE', 8: 'DC', 9: 'MD', 10: 'NJ', 11: 'NY', 12: 'PA', 13: 'IL', 14: 'IN', 15: 'IA', 16: 'MI', 17: 'MN', 18: 'MO', 19: 'OH', 20: 'WI', 21: 'KS', 22: 'NE', 23: 'ND', 24: 'OK', 25: 'SD', 26: 'CO', 27: 'ID', 28: 'MT', 29: 'UT', 30: 'WY', 31: 'CA', 32: 'OR', 33: 'WA', 34: 'AZ', 35: 'NV', 36: 'NM', 37: 'TX', 38: 'AL', 39: 'AR', 40: 'FL', 41: 'GA', 42: 'KY', 43: 'LA', 44: 'MS', 45: 'NC', 46: 'SC', 47: 'TN', 48: 'VA', 49: 'WV', 50: 'AK', 51: 'HI'}

#This prints out the most popular male name and all the occurences of that name
def printPopularNames(sex):
    while True: 
        try: 
            
            printStates.printStateNames() #Prints out all 
            state_code = int(input("Enter the state code you would like to search for: ")) #stores user choice to compare to allStateAbbrs dict
            if state_code in allStateAbbrs:
                print(f"In {allStateAbbrs[state_code]}:")
                mp, most_freq = most_popular(state_code, sex) #mp is a string list for the most popular male name(s) and most_freq is the occurences for the name(s)

                if len(mp) == 1:
                    print(f"\nMost popular {sex.lower()} name: {mp[0]} ({most_freq} occurrences)") #If there is only one most popular name, it will print out one
                else:
                    print(f"\nMost popular {sex.lower()} names: ({most_freq} occurrences each)") #if there are multipe most popular names (meaning the frequency is the same), it will print them all out
                    for name in mp:
                        print(f"{name}")
                print("\n") #Spacing to make the output more readable

                break
            elif state_code < 0 or state_code > 51: # validating user input and continuing untill they enter a correct input
                print("Thats is an invalid state code, please try again\n")
                continue

        except:
            
            print("Please input a integer value of the state codes") #If the input is invalid, the user gets to try again
            continue

#This prints out the least popular male name and all the occurences of that name
def printLeastPopular(sex): 
    while True: 
        try: 
            
            printStates.printStateNames() #Prints out all 
            state_code = int(input("Enter the state code you would like to search for: ")) #stores user choice to compare to allStateAbbrs dict
            if state_code in allStateAbbrs:
                print(f"In {allStateAbbrs[state_code]}:")

                lp, least_freq = least_popular(state_code, sex) #lp is a string list for the least popular male name(s) and least_freq is the occurences for the name(s)

                if len(lp) == 1:
                    print(f"\nLeast popular {sex.lower()} name: {lp[0]} ({least_freq} occurrences)") #If there is only one least popular name, it will print out one
                else: 
                    print(f"\nLeast popular {sex.lower()} names: ({least_freq} occurrences each)") #if there are multipe most popular names (meaning the frequency is the same), it will print them all out
                    for name in lp:
                        print(f"{name}")
                print("\n") #Spacing to make the output more readable
                break
            elif state_code < 0 or state_code > 51: # validating user input and continuing untill they enter a correct input
                print("Thats is an invalid state code, please try again\n")
                continue

        except:
            
            print("Please input a integer value of the state codes") #If the input is invalid, the user gets to try again
            continue

# Iterates through all years for the provided state code and finds the most popular male name by frequency and returns it along with its total frequency
def most_popular(state_code, sex):
    name_counts = {}
    #Following two integers store minimum and maximum years that the user can iterate through
    minYear = 0 
    maxYear = -1
    while minYear < 1910 or minYear > 2021: 
        try: #Tries to input, in case the user inputs a character
            minYear = int(input("Please input the starting year for the range of years from 1910-2021: ")) 
            if minYear < 1910 or minYear > 2021:
                print(f"{minYear} is not a valid year in the range of 1910-2021, please pick a different year")
        except: 
            print("You cannot input a character, please input an integer")
        
        
    while maxYear < minYear or maxYear > 2021:
        try: #Tries to input, in case the user inputs a character
            maxYear = int(input(f"Please input the ending year for the range of years from {minYear}-2021: ")) 
            if maxYear < minYear or maxYear > 2021:
                print(f"{maxYear} is not a valid year in the range of {minYear}-2021")
        except:
            print("You cannot input a character, please input an integer")
    
    for i in range(minYear, maxYear +1):
        file_name = "./Data files/Organizedstates/" + str(allStateAbbrs[state_code]) + "/" + sex + "/" + str(i) + ".txt" #Expected address of files
        with open(file_name, "r") as file:
            next(file)
            for line in file:
                column = line.strip().split(",") #splitting elements of each row of the file into elements of an array
                name = column[0]
                count = int(column[1])
                if name in name_counts: #If the dictionary key exists, add to the total frequency of the name
                    name_counts[name] += count
                else:
                    name_counts[name] = count
    # sorting through the dictionary to find the max frequency
    most = max(name_counts.values())
    #in case there is more than one top name, this list stores all of them:)
    most_popular = [name for name, count in name_counts.items() if count == most]#most popular stores the popular name(s)
    most_popular = sorted(most_popular) # sorting in alphabetical order so it's easier to read and make connections

    return most_popular, most

#Iterates through all years for the provided state code and finds the least popular male name by frequency and returns it along with its total frequency
def least_popular(state_code, sex):
    name_counts = {}
    #Following two integers store minimum and maximum years that the user can iterate through
    minYear = 0 
    maxYear = -1
    while minYear < 1910 or minYear > 2021: 
        try: #Tries to input, in case the user inputs a character
            minYear = int(input("Please input the starting year for the range of years from 1910-2021: ")) 
            if minYear < 1910 or minYear > 2021:
                print(f"{minYear} is not a valid year in the range of 1910-2021, please pick a different year")
        except: 
            print("You cannot input a character, please input an integer")
        
        
    while maxYear < minYear or maxYear > 2021:
        try: #Tries to input, in case the user inputs a character
            maxYear = int(input(f"Please input the ending year for the range of years from {minYear}-2021: ")) 
            if maxYear < minYear or maxYear > 2021:
                print(f"{maxYear} is not a valid year in the range of {minYear}-2021")
        except:
            print("You cannot input a character, please input an integer")
    
    for i in range(minYear, maxYear +1):
        file_name = "./Data files/Organizedstates/" + str(allStateAbbrs[state_code]) + "/" + sex + "/" + str(i) + ".txt" #Expected address of files
        with open(file_name, "r") as file:
            next(file)
            for line in file:
                column = line.strip().split(",") #splitting elements of each row of the file into elements of an array
                name = column[0]
                count = int(column[1])
                if name in name_counts: #If the dictionary key exists, add to the total frequency of the name  
                    name_counts[name] += count
                else:
                    name_counts[name] = count
    # same syntax and logic as before       
    least = min(name_counts.values())
    least_popular = [name for name, count in name_counts.items() if count == least]#most popular stores the popular name(s)
    least_popular = sorted(least_popular) # sorting in alphabetical order so it's easier to read and make connections

    return least_popular, least