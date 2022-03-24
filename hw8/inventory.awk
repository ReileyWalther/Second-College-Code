BEGIN {
  print "Make      Value";
  print "---------------";
}
{ makes[$1]+= $4; }
END {
  for(i in makes) {
    printf "%-8s $%5d\n", i, makes[i];
  }
}
