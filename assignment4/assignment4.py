# Author:          Reiley Walther
# Creation Date:   February 25, 2020
# Due Date:        Febraury 28, 2020
# Course:          CSC 223 020
# Professor Name:  Dr. Schwesinger
# Assignment:      #4
# Filename:        assignment4.py
# Purpose:         Python file uses a CSV file to print out the Name of associated with
#                  the max speed, the Name associated with the five highest HP values
#                  and the mean of Attack value of all data provided with names starting
#                  with an M.

import sys
import csv


# Function Name:   maxSpeed
# Description:     Function to split the list in order to manipulate, compare the speeds
#                  and return the name parallel to the highest speed.
# Parameters:      aList - list: A list of each line of the csv file before split again 
#                                for manipulation.
# Return Value:    name: returns the name of the record that has the highest speed

def maxSpeed(aList):
	newList = []
	maxsp = 0
	name = ''
	for i in aList[1:]:
		lines = i.split(',')
		if (int(lines[-1]) > int(maxsp)):
			maxsp = lines[-1]
			name = lines[1]
	return name


# Function Name:   HPvalues
# Description:     A function that splits a list passed in, creates two more lists and 
#                  combines the list using zip to determine the top 5 highest HP scores
#                  in the list and returns a list of the 5 names.
# Parameters:      aList - list: A list of each line of the csv file before split again
#                                for manipulation.
# Return Value:    result: a list of 5 names which are associated with the 5 highest HP
#                          scores

def HPvalues(aList):
	nameList = []
	HPlist = []
	result = []
	for i in aList[1:]:
		lines = i.split(',')
		HPlist.append(int(lines[4]))
		nameList.append(lines[1])

	bList = list(zip(HPlist,nameList))
	bList.sort(reverse=True)

	for i in bList[0:5]:
		result.append(i[1])

	return result


# Function Name:   avAttack
# Description:     A function that takes a list passed in, splits it for 
#                  manipulation, creates two new lists and tests if a name starts with a
#                  specific letter, then find the mean of all their attack stats and
#                  return the average.
# Parameters:      aList - list: A list of each line of the csv file before split again
#                                for manipulation.
# Return Value:    added/count: the total count of all the attack stats of all records 
#                  with names starting with M divided by the number of records

def avAttack(aList):
	Lname = []
	attack = []
	for i in aList[1:]:
		lines = i.split(',')
		Lname.append(lines[1])
		attack.append(lines[2])

	added = 0
	count = 0
	idx = 0
	for i in Lname:
		if (i[0].upper() == "M"):
			added += int(attack[idx])
			count += 1
		idx += 1

	return(added/count)

# Function Name:   Main
# Description:     Main function to run the program and call subfunctions
# Parameters:      None
# Return Value:    None

def main():
# Tests for an input file in the command line

	if len(sys.argv) != 2:
		print("Usage: " + sys.argv[0] + " <filename>")
		sys.exit(0)
	try:
		f = open(sys.argv[1],'r')
	except FileNotFoundError:
		print("File not found")
		sys.exit(0)

	L = f.read()
	f.close()

	Ls = L.split('\n')
	del Ls[-1]
	del Ls[-1]

	name = maxSpeed(Ls)
	top5 = HPvalues(Ls)
	number = avAttack(Ls)	

	print('')
	print('Name of the max speed entry: ' + name)
	print('Five highest HP values: ' + str(top5))
	print('Mean of Attack: ' + str(number))

if __name__ == '__main__':
    main()
