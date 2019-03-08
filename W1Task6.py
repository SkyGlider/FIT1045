#Name : Andrew Pang, Teng Sin Hui
#Date : 8 Mar 2019
#Task 6

import math #imports math module

usrname = input("Enter your name : ") #get user's name

usrlength = len(usrname) #calculate length of username
print("The length of your name is " + str(usrlength) + " characters long") #prints the answer above

#counts the number of each vowel in the username
na = usrname.count("a")
ne = usrname.count("e")
ni = usrname.count("i")
no = usrname.count("o")
nu = usrname.count("u")

#prints the number of each vowels in the username
print("no. of 'a's :" + str(na))
print("no. of 'e's :" + str(ne))
print("no. of 'i's :" + str(ni))
print("no. of 'o's :" + str(no))
print("no. of 'u's :" + str(nu))

