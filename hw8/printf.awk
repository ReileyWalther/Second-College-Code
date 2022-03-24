BEGIN {
  printf "%d %d\n", 3, 45;
  # %f defaults to 6 digits of precision
  printf "%f\n", 3.14; 
  printf "%8.3f %5d\n", 3.14,21;
  printf "%-8.3f %-5d\n", 3.14,21;
  printf "%10.3e\n", 3.14*10;
  printf "%10s %-10s%d\n","string1","string2",3;
  printf "Three squared is: %d\n",3*3;
}
