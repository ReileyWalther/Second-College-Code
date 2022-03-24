# Name:			Reiley Walther
# Creation Date:	February 14, 2020
# Due Date:		February 21, 2020
# Course:		CSC223 020
# Professor Name:	Dr. Schwesinger
# Assignment:		#3
# Filename:		assignment3.py
# Purpose:		Python program reads in a JSON file and creates  well formatted
#			file with appropriate output.

import sys
import json
import csv
from pprint import pprint


def main():
# Tests for an input file in the command line

	if len(sys.argv) != 2:
		print("Usage: " + sys.argv[0] + " <filename>")
		sys.exit(0)
	try:
		f = open('pokedex.json')
	except FileNotFoundError:
		print("File not found")
		sys.exit(0)

# Loads contents of JSON file into a variable called data and closes file f

	data = json.load(f)
	f.close()

# Creates an outfile variable to use to write to the 'out.csv' file

	outfile = open('out.csv','w')
	outfile.write('Id,Name,Attack,Defense,HP,Sp. Attack,Sp. Defense,Speed\n')

# Singleline variable created to hold all information of the current record
# Loop through the data to find necessary information for output
# Loads information into the singleline variable
# Write the singleline variable to the outfile	
	singleline = ''
	for d in data:
		pokeID = d['id']
		pokeName = d['name']['english']
		pokeHP = d['base']['HP']
		pokeAt = d['base']['Attack']
		pokeDf = d['base']['Defense']
		pokespA = d['base']['Sp. Attack']
		pokespD = d['base']['Sp. Defense']
		pokeSpeed = d['base']['Speed']

		singleline = str(pokeID) + ',' + pokeName + ',' + str(pokeAt) + ',' +\
				 str(pokeDf) + ',' + str(pokeHP) + ',' + str(pokespA) +\
				 ',' + str(pokespD) + ',' + str(pokeSpeed) + '\n'

		outfile.write(singleline)

# Closes the outfile
	outfile.close()

#prints out the name of the created file

	print('The file created is: out.csv')

if __name__ == '__main__':
    main()
