BEGIN { print "" } 
# computes the data to work with into arrays
NR>1 { lists[$1] += $4; sums[$1] += 1; avgs[$1]=(lists[$1]/sums[$1]); }
NR=2 {carcount = ""; }
NR=2 {carvalue = ""; }
count = sums[0];
maxval = lists[0];

# loops through lists and compares to find the output to produce and assigns them
{for(i in lists) {
	if(sums[i]>count){
		count = sums[i];
		carcount = $1;
	}
	if(lists[i]>maxval) {
		maxval = lists[i];
		carvalue = i
	}
}
}
# produces the two lines out output with the correct data required
END{
	printf "%-s has %-d car(s) on the lot\n", carcount, count;
	printf "%-s has $%-5.2f in inventory\n", carvalue, maxval;
}
