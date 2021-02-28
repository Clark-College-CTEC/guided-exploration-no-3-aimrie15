# Guided Exploration No. 3
# Alexandra Imrie

# imports random library
import random

# empty list to store rap names
possible_names = []

# open rap-names-output and write to it
outputFile = open('rap-names-output.txt', 'w')


with open('rap-names.txt', 'r') as dataFile:
    # Opens rap-names for read access
    for name in dataFile:
        # Append names to list and file, strip off line feed
        possible_names.append(name.rstrip())

# User input
count = int(input('How many rap names would you like to create? '))
# User input
parts = int(input('How many parts should the name contain? '))

for i in range(count):
    # New empyt list to store generated names
    name_parts = []
    # Loop through number of times user requested
    for j in range(parts):
        # Append names to empty lists, generate a random number from the list, length of list -1 because python starts at 0.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# Write names to file and join them into a sentence, each name on a new line
outputFile.write(f"{' '.join(name_parts)}\n")
# Prints names to python terminal and also joins them together by a space
print(f"{' '.join(name_parts)}")

# Close the file
outputFile.close()
