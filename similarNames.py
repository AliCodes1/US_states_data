try:
    import csv                            # import the csv module
    import itertools                     # import the itertools module
    import sys
    import subprocess
    from Levenshtein import distance     # import the Levenshtein distance function from the Levenshtein module
except ModuleNotFoundError:
    print("Installing Levenshtein")
    python = sys.executable
    subprocess.check_call([python,'-m', 'pip', 'install', "-U", 'Levenshtein'], stdout=subprocess.DEVNULL)
finally:
    from Levenshtein import distance 


# define a function to find any similar names and add them to a list of tuples
def find_similar_names(names):
    similar_names = []                # create an empty list to store the similar names
    for name1, name2 in itertools.combinations(names, 2):  # loop through all possible pairs of names
        # check if the Levenshtein distance between the names is less than or equal to 1
        if distance(name1, name2) <= 1:
            for similar in similar_names:
                # check if either name is already in a tuple in the similar_names list
                if name1 in similar or name2 in similar:
                    similar.add(name1)  # add the names to the existing tuple
                    similar.add(name2)
                    break
            else:
                similar_names.append(set([name1, name2]))  # create a new tuple for the similar names
    # convert the sets in the similar_names list to tuples
    return [tuple(similar) for similar in similar_names]

# define a function to open a file and output similar names
def openfileAndOutputSimilarNames(fileName):
    with open(fileName) as csv_file:  # open the file
        next(csv_file)               # skip the first line (header)
        csv_reader = csv.reader(csv_file)  # create a csv reader object
        names = [row[0] for row in csv_reader]  # create a list of names from the first column of the file
        similar_names = find_similar_names(names)  # call the find_similar_names function to find similar names
        num = 0                       # initialize a counter
        position = -1                 # initialize the position variable to -1
        
        # loop through the similar_names list and print each tuple with its index
        if len(similar_names) != 0:
            print("\n")
            for i in range(len(similar_names)):
                num += 1
                print(str(num) + ". " + similar_names[i][0] + " has multiple variations in their name")
            print("\nWould you like to see the different variations of each name.")
            yesOrNo = input("Yes or No: ")  # ask the user if they want to see the different variations of each name
            askAgain = True                # initialize a flag variable to control a while loop
            while askAgain != False:
                if yesOrNo == "Yes" or yesOrNo == "yes":
                    askAgain = False
                    # loop through the similar_names list and print each name in each tuple
                    for l in range(len(similar_names)):
                        for j in range(len(similar_names[l])):
                            print(similar_names[l][j])
                elif yesOrNo == "No" or yesOrNo == "no":
                    askAgain = False
                    print("\nVariations of each name will not be shown")
                else:
                    print("Invalid input!")
                    yesOrNo = input("Yes or No: ")
            askAgain2 = True
            print("\nWould you like to see the different variations of a single name.")
            yesOrNo = input("Yes or No: ")  # ask the user if they want to see the different variations of a single name
            while askAgain2 != False:
                if yesOrNo == "Yes" or yesOrNo == "yes":
                    askAgain2 = False
                    # ask the user for the index of the name they want to see
                    while position != 0:
                        position = int(input("Enter the position of the name (Enter 0 to exit): "))
                        askAgain3 = True
                        #error check
                        while askAgain3 != False:
                            if int(position) > len(similar_names):
                                print("Out of Bounds!")
                                position = int(input("Enter the position of the name (Enter 0 to exit): "))
                            elif position < 0:
                                print("Out of Bounds!")
                                position = int(input("Enter the position of the name (Enter 0 to exit): "))
                            elif position==0:
                                askAgain3 = False
                            elif int(position)<=len(similar_names):
                                askAgain3 = False
                                for i in range(len(similar_names[int(position) - 1])):
                                    print(similar_names[int(position) - 1][i])
                            else:
                                print("Incorrect input! Please try again.")
                                position = int(input("Enter the position of the name (Enter 0 to exit): "))
                #check for invalid input and check if the variations of a name want to be shown
                elif yesOrNo == "No" or yesOrNo == "no":
                    askAgain2 = False
                    print("\nVariations of a name will not be shown")
                else:
                    print("Invalid input!")
                    yesOrNo = input("Yes or No: ")
        else:
            print("\nThere are no names with similar spelling\n")