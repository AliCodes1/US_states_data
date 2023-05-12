try:
    # Import the csv module for handling CSV files
    import csv
    # Import itertools module for advanced iteration capabilities
    import itertools
    
    import subprocess
    import sys
    # Import EthnicClassifier class from the ethnicseer module
    from ethnicseer import EthnicClassifier
except ModuleNotFoundError:
    print("Installing module ethicseer")
    python = sys.executable
    subprocess.check_call([python,'-m', 'pip', 'install', 'ethnicseer==0.1.2'], stdout=subprocess.DEVNULL)
    subprocess.check_call([python,'-m', 'pip', 'install',"-U", 'scikit-learn==1.0.2'], stdout=subprocess.DEVNULL) #A requirement for ethnicseer
finally:
    from ethnicseer import EthnicClassifier
# Define a function to open a file and output the percentage of a certain ethnicity
def openfileAndOutput(fileName):
    # Print a message to indicate the purpose of the function
    print("\nGetting the percentage of a certain ethnicity!\n")
    # Create an empty list to hold names from the CSV file
    list=[]
    # Define a list of ethnicities to classify
    ethnicities=["Russian","Indian","Japanese","Vietnam","English","Italian","German","korean","Chinese","French","Middle-Eastern", "Spanish",]
    # Define a corresponding list of ethn codes for the EthnicClassifier
    ethn=['rus', 'ind', 'jap', 'vie', 'eng', 'ita', 'ger', 'kor', 'chi', 'frn', 'mea', 'spa']
    # Create a list of zeros to keep count of how many names were classified as each ethnicity
    list2=[0,0,0,0,0,0,0,0,0,0,0,0]
    # Open the CSV file and read the names from it
    with open(fileName) as csv_file:
        # Skip the first row of the file since it only contains headers
        next (csv_file)
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        # Get the first column (names) from each row in the CSV file
        names = [row[0] for row in csv_reader]
        # Add each name to the list
        num=0
        for i in range(len(names)):
            list.append(names[i])
            num+=1
        # Load a pretrained EthnicClassifier model
        ec = EthnicClassifier.load_pretrained_model()
        # Classify the names in the list using the EthnicClassifier
        result = ec.classify_names(list)
        # Count how many names were classified as each ethnicity
        for j in range(len(list)):
            for k in range(len(ethn)):
                if result[j] == ethn[k]:
                    list2[k] += 1
        # Calculate the percentage of names classified as each ethnicity and output the results
        for z in range(len(list2)):
            if int(list2[z])>0:
                avg=(int(list2[z])/num)*100
                print("{:.2f}% of the people are {}".format(avg, ethnicities[z]))
    print("\n")