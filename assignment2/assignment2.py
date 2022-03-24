# Name:           Reiley Walther
# Creation Date:  February 8, 2020
# Due Date:       February 14, 2020
# Course:         CSC223 020
# Professor Name: Dr. Schwesinger
# Assignment:     #2
# Filename:       assignment2.py
# Purpose:        Python program calculates the mean, range, variance and gets data from
#                 files to compute and prints all out.

import sys

# TODO document the functions according the department standards

# Description: 	Function to calculate the mean of a list passed in
# Parameters:	data - a list of floating point values passed in for mean calculation
# Return value:	avg - function returns avg which is the mean/average of the list
def mean(data):
	sum_data = sum(data)
	avg = sum_data/len(data)
	return avg
	pass

# Description:  Function finds the range of the data of the list passed in
# Parameters:   data - a list of floating point values passed in to find the range
# Return value: (maxdata-mindata) - the range value for the list from the lowest to the
# 		highest number in the list
def rng(data):
	maxdata = max(data)
	mindata = min(data)
	return maxdata-mindata
	pass

# Description:  Function finds the variance of the data of the list passed in
# Parameters:   data - a list of floating point values passed in to find the variance
# Return value:	(figure/(datalength-1)) - the value of the variance which is calculated
# 		by taking the sum of the value minus the mean all squared divided by 
# 		the length of the data
def variance(data):
	datamean = mean(data)
	datalength = len(data)
	
	sumvars = []
	for i in data:
		sumvars.append((i-datamean) ** 2)
	figure = sum(sumvars)
	return figure/(datalength-1)
	pass

# Description:	Function takes a string representing a file name and returns a list
# 		of floating point numbers from the file.
# Parameters:	filename - a string passed in as a filename and function attempts to
# 		open the file.
# Return Value:	nums - a list either of floating point numbers or an empty list if
# 		the file doesn't open or contins a non-floating point value.
def get_data(filename):
	nums = []
	try:
		datfile = open(filename,'r')
	except FileNotFoundError:
		return nums

	info = datfile.read()
	datfile.close()

	L = info.split()
	nums = []
	for item in L:
		try:
			i = float(item)
		except ValueError:
			nums = []
			return nums
		nums.append(i)
	return nums
	pass

def main():
	if len(sys.argv) != 2:
		print("Usage: " + sys.argv[0] + " <filename>")
		sys.exit(0)
	data = get_data(sys.argv[1])
	if data:
		print("The mean is: ", mean(data))
		print("The range is: ", rng(data))
		print("The variance is: ", variance(data))
	pass

# DO NOT EDIT ANYTHING BELOW THIS LINE
if __name__ == '__main__':
    main() # call the main function

