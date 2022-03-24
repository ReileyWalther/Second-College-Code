BEGIN { 	# sets up the header
	print "Make     Total  Average";
	print "-----------------------";
}
# computes the tables results into arrays
NR>1 { lists[$1] += $4; sums[$1] += 1; avgs[$1]=(lists[$1]/sums[$1]); } 
END {
	# loops through the arrays and prints them neatly
	for(i in lists){
		printf "%-8s %5d %8.2f\n", i, lists[i], avgs[i];
	}
}
