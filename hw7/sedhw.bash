Script started on Tue 14 Apr 2020 02:21:38 PM EDT
]0;rwalt267@csitrd:~/csc252/hw7[?1034h[rwalt267@csitrd hw7]$ sed -e 's/[^,]*$//g' -e 's/[,]//g' students.txt
CS jlenn123 Lennon
IT pmcar456 McCartney
CS ghart789 Harrison
IT rstar246 Starky
CS bspri826 Springsteen
IT mjagg924 Jagger
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ echo --------------------
--------------------
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed -e 's/\w*//3' -e 's/, //g' students.txt
CS jlenn123 John 
IT pmcar456 Paul 
CS ghart789 George 
IT rstar246 Richard "Ringo" 
CS bspri826 Bruce "Boss" 
IT mjagg924 Mick
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed -e 's/\w*//3' -e 's/, //g' students.txt[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[18Pecho --------------------
--------------------
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed -e 's/\w* //2[C[1P[1P[1P[C[C[C[C[C[C[C[C[C[C[C' students.txt
CS Lennon, John 
IT McCartney, Paul 
CS Harrison, George 
IT Starky, Richard "Ringo" 
CS Springsteen, Bruce "Boss" 
IT Jagger, Mick
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed 's/\w* //2' students.txt[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[3Pecho --------------------
--------------------
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed 's/[0-9]/*/g' students.txt
CS jlenn*** Lennon, John 
IT pmcar*** McCartney, Paul 
CS ghart*** Harrison, George 
IT rstar*** Starky, Richard "Ringo" 
CS bspri*** Springsteen, Bruce "Boss" 
IT mjagg*** Jagger, Mick
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed 's/[0-9]/*/g' students.txt[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[5Pecho --------------------
--------------------
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed -e 's/[^,]*"\b/ /1' -e 's/"//g' students.txt
CS jlenn123 Lennon, John 
IT pmcar456 McCartney, Paul 
CS ghart789 Harrison, George 
IT rstar246 Starky, Ringo 
CS bspri826 Springsteen, Boss 
IT mjagg924 Jagger, Mick
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ sed -e 's/[^,]*"\b/ /1' -e 's/"//g' students.txt[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[K^C
]0;rwalt267@csitrd:~/csc252/hw7[rwalt267@csitrd hw7]$ exit
exit

Script done on Tue 14 Apr 2020 02:28:24 PM EDT
