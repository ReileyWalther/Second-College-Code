BEGIN { sum=0; numb=-1 }	# initializes two variables 
{ sum += $4; numb++; }		# computes total and the number of records
END {
	printf "Average Price: %5.2f \n", (sum/numb); # prints the result in format
}
