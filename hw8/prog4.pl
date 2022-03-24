
# loops through the file
while($line=<STDIN>) { 

# skips first line which is a header
next if $. < 2;
chomp $line;

# slpits the line to find and align different data
@tests = split(/\s+/, $line);
# finds a total value and the number of records
$tots = $tots + $tests[3];
$nums++;
}

# outputs the required average
printf "Average Price: %5.2f\n", ($tots/$nums);

