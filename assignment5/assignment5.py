# Author:          Reiley Walther
# Creation Date:   March 4, 2020
# Due Date:        March 5, 2020
# Course:          CSC 223 020
# Professor Name:  Dr. Schwesinger
# Assignment:      #5
# Filename:        assignment5.py
# Purpose:         Program reads in a file, uses functions to manipulate data and then
#                  output the data in a neat, tabulated format.

import sys


# Function Name:   createList
# Description:     A function to create and utilize lists in comprehensions and other
#                  manipulation techniques to find the total numbers and percentages.
# Parameters:      aList - A list variable passed in that was read in from a csv file
#                          and needs to be split to find the separate indexes
# Return Value:    none


def createLists(aList):
	ID = []
	AJN = []
	Tip = []
	Ad = []
	Joke = []
	Nope = []
	for i in aList[1:]:
		j = i.split(',')
		ID.append(j[0])
		AJN.append(j[1])
		Tip.append(j[2])
		Ad.append(j[3])
		Joke.append(j[4])
		Nope.append(j[5])
#	print(ID)
#	print(AJN)
#	print(Tip)
#	print(Ad)
#	print(Joke)
#	print(Nope)

	AdList = len([x for x in AJN if x == "\"Ad\""])
	JokeList = len(list(filter(lambda x: x == "\"Joke\"", AJN)))
	NoneList = len(list(filter(lambda x: x == "\"None\"", AJN)))

#	print(AdList)
#	print(JokeList)
#	print(NoneList)

	print('|{:4} | {:^5} |'.format("Ad",AdList))
	print('|{:4} | {:^5} |'.format("Joke",JokeList))
	print('|{:4} | {:^5} |'.format("None",NoneList) + '\n')

# Function Name:   Main
# Description:     Main function to run the program and call subfunctions to display
#                  tabulated data
# Parameters:      None
# Return Value:    None

def main():
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

	print('|{:2} | {:3} | {:4}|'.format("Type","Total","Percent"))
	print("------------------------")

	createLists(Ls)

if __name__ == '__main__':
    main()
