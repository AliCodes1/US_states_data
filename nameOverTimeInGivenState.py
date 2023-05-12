#!/usr/bin/env python3
try:
    import csv
    import os
    import sys
    import subprocess
    import matplotlib.pyplot as plt
    import numpy as np
    import printAllStatesWithDictionaries as printSates
except ModuleNotFoundError:
    print("Installing module matplotlib")
    python = sys.executable
    subprocess.check_call([python,'-m', 'pip', 'install', "-U", 'matplotlib'], stdout=subprocess.DEVNULL)
finally:
    import matplotlib.pyplot as plt
    import numpy as np
    import printAllStatesWithDictionaries as printSates
    import csv
    import os
    import sys
    import subprocess



state_codes_dict = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

def nameOverTime():
    # Get user input for gender, name, and state names
    while True:
        try:
            gender = input("What is your gender (M/F)? ")
            if gender.lower() not in ['m', 'f']:
                raise ValueError("Gender must be 'M' or 'F'.")
            break
        except ValueError as e:
            print(str(e))

    while True:
        try:
            name = input("What is your name? ")
            if len(name.strip()) == 0:
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(str(e))

    while True:
        try:
            print("Please chooose from the given states:")
            printSates.printStateNames()
            state_names = input("Enter a comma-separated list of state names: ")
            state_codes = []
            for state in state_names.split(','):
                state = state.strip()
                if state in state_codes_dict:
                    state_codes.append(state_codes_dict[state])
                elif len(state) > 0:
                    raise ValueError(f"{state} is not a valid state name.")
            if len(state_codes) == 0:
                raise ValueError("No valid state names entered.")
            break
        except ValueError as e:
            print(str(e))


    counts = {}  # use a dictionary to store counts for each year

    # specify the file path to the Organized data folder
    data_path = "Data files/OrganizedStates/"

    for state_code in state_codes:
        # navigate to the folder for the current state
        state_folder = os.path.join(data_path, state_code.upper())
        if not os.path.exists(state_folder):
            print(f"Error: Folder {state_folder} not found.")
            print("Make sure the folder exists and is in the correct format.")
            continue
        # loop through the male and female folders
        for gender_folder in ["male", "female"]:
            gender_path = os.path.join(state_folder, gender_folder)
            if not os.path.exists(gender_path):
                break
            
            # loop through the files in the folder
            for filename in os.listdir(gender_path):
                if not filename.endswith(".txt"):
                    continue
                
                # open the file and read the rows
                filepath = os.path.join(gender_path, filename)
                try:
                    with open(filepath) as f:
                        reader = csv.reader(f)
                        next(reader)  # skip the header row
                        for row in reader:
                            if row[0] == name:
                                count = int(row[1])
                                year = filename[-8:-4]  # extract the year from the filename
                                if year in counts:
                                    counts[year] += count
                                else:
                                    counts[year] = count
                except FileNotFoundError:
                    print(f"Error: File {filename} not found.")
                    print("Make sure the file exists and is in the correct format.")
                    break

    # check if name appears in the selected state or not
    if state_code not in [code for code in state_codes_dict.values() if code in state_codes]:
        print(f"No records found for {name} in {state_codes_dict[state_code]}.")
    if counts:
        print(f"{name} appears in the selected states as follows:")
        for year, count in counts.items():
            print(f"{year}: {count}")
    else:
        print(f"No records found for {name} in the selected states.")  

    years = np.array(list(counts.keys()))
    nameFreq = np.array(list(counts.values()))
    #print(f"{list(counts.keys())}\n{counts.values()}")

    plt.plot(years, nameFreq)
    plt.xlabel("Years (1910-2021)")
    plt.ylabel("Frequency of name")
    plt.title(f"Frequency of {name} from {years[0]} to {years[-1]}")
    plt.show()


